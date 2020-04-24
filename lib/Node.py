import math

import random
from lib.Message import *

import numpy as np

'''
 This acts as a complete implementation of Raymond's algorithm for distributed mutual 
 exclusion for an arbitrary number of number of nodes. Further this architecture can 
 be expanded to fit an arbitrary number of resources. Simulation parameters are included 
 for more realistic and interesting results.
 
 Note: - Currently there is no support for a different number of resources 
         but this can easily be resolved by creating new message types.
       - Within this implementation the nodes within the spanning tree
         do not need to keep track of their neighbours as long as the 
         "holder" field has be initialized correctly. 
'''

class Node:

    '''
        The transmission speed for sending messages between different Nodes.
        Used for calculating the transmission time between nodes.
    '''


    # Position is [x,y] vector
    def __init__(self, position, number, instance, holder=None):

        '''
        holder := relative position of the token relative to the node
        position := (x,y) position used for calculating transmission times
        number := unique integer for specifying a node, using for debugging and
                 log purposes
        queue := FIFO queue of token requests form neighbours or the node itself
        asked := boolean value for whether a request has been sent out a neighbouring
                node
        using := boolean value to denote whether the node is currently operating in the
                critical section
        left := Time in the global environment when the node last left the CS. Not
                included under the standard implementation of Raymond's algorithm but
                used here to ensure meet the assumption that nodes will not keep adding
                themselves to their own queue.
        nhbrs := The neighbour within the spanning tree list. Currently not needed
                in the implementation but will be helpful for plotting.

        ==============================================================================
                                     Simulation parameters:
        ===============================================================================

        request_frequency := alpha paramter used within the poisson distribution for the
                            personal generation of resource requests
                Reading on Poisson Process:
                        https://towardsdatascience.com/the-poisson-distribution-and-poisson-process-explained-4e2cb17d459
        computation_mean := The average amount of time that the Node will hold resource when it enters the critical
                            section.
        computation_stdev := The standard deviation for the amount of time a Node will hold the resource from the
                            mean amount "computation_mean".

        '''

        self.holder = holder
        self.position = position
        self.number = number
        self.queue = []
        self.asked = 0
        self.using = 0
        self.left = 0

        # simulation parameters and environment
        self.G = instance.G
        self.env = instance.env
        self.request_freq = instance.frequency_mean
        self.computation_mean = instance.computation_mean
        self.computation_stdev = instance.computation_stdev
        self.transmission_speed = instance.transmission_speed

        # debugging variable
        self.nhbrs = None

    def __str__(self):
        return " "+str(self.number) + " " + str(self.holder.number) + " " + str(self.position)

    def set_nhbrs(self, nhbrs):
        self.nhbrs = nhbrs

    def setHolder(self, holder):
        self.holder = holder

    # PEM
    # This function can not be broken up into smaller pieces due
    # to the limitations of generator functions in Python
    def receive_message(self, env, pipe, pipe_log):
        while True:
            # Only read those messages addressed to myself

            msg = yield pipe.get(lambda message: message.receiver == self)
            if msg.message_type == MessageType.personal_request:
                self.queue.append(self)

            # resource request for a node
            elif msg.message_type == MessageType.resource_request:
                self.queue.append(msg.sender)

            # Node has received the token from a neighbour
            elif msg.message_type == MessageType.pass_key:
                self.holder = self

            if self.holder == self and len(self.queue) != 0:
                self.holder = self.queue.pop(0)
                self.asked = 0


                if self.holder == self:

                    self.using = 1
                    # Entering the critical section
                    # Amount of time spent in the critical section is determined via a uniform distribution
                    pipe_log.append(Message(self, MessageType.enteringCS, self.env.now))
                    yield self.env.timeout(abs(np.random.normal(self.computation_mean, self.computation_stdev)))
                    pipe_log.append(Message(self, MessageType.exitingCS, self.env.now))
                    self.left = env.now
                    # Node exits the critical section
                    self.using = 0

                    # When exiting the CS check to see if there are nodes
                    # waiting for the resource, and if so, and pass the key
                    # Note that because we assume that nodes will not

                    if self.holder == self and len(self.queue) != 0:
                        self.holder = self.queue.pop(0)
                        self.asked = 0
                        self.switch_direction(self.holder, self)
                        msg = Message(self.holder, MessageType.pass_key, env.now, self)
                        pipe_log.append(msg)
                        yield env.timeout(msg.trans_time)
                        pipe.put(msg)


                    # Send request to the new holder in the case where there is more
                    # than one outstanding node on the queue.
                    if self.holder != self and len(self.queue) != 0 and self.asked == 0:
                        msg = Message(self.holder, MessageType.resource_request, env.now, self)
                        pipe_log.append(msg)
                        yield env.timeout(msg.trans_time)
                        pipe.put(msg)
                        self.asked = 1

                else:

                    self.switch_direction(self.holder, self)
                    msg = Message(self.holder, MessageType.pass_key, env.now, self)
                    pipe_log.append(msg)
                    yield env.timeout(msg.trans_time)
                    pipe.put(msg)


            # make request
            if self.holder != self and len(self.queue) != 0 and self.asked == 0:
                msg = Message(self.holder, MessageType.resource_request, env.now, self)
                pipe_log.append(msg)
                yield env.timeout(msg.trans_time)
                pipe.put(msg)

                self.asked = 1


    def generate_request(self, env, pipe, pipe_log):

        while True:
            yield env.timeout(-math.log(1.0 - random.random()) / self.request_freq)
            msg = Message(self, MessageType.personal_request, env.now)
            # Used to ensure that a node does not keep adding itself to the queue
            # when it is already waiting for the resource.
            # This is an assumption made in Raymond's algorithm.
            if self not in self.queue and env.now != self.left and self.using == 0:
                pipe.put(msg)
                pipe_log.append(msg)

    '''
        Changes direction in direct graph from one -> two to: two -> one
    '''
    def switch_direction(self, one, two):
        self.G.add_edge(two.number, one.number)
        self.G.remove_edge(one.number, two.number)


