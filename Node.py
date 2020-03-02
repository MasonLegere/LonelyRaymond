from simpy import Process
from simpy import *
from numpy import array
import random
from Message import *

'''
 This acts as a complete implementation of Raymond's algorithm 
 for an arbitrary number of number of nodes. 
 
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

    transmission_speed = 1.0

    # Position is [x,y] vector
    def __init__(self, position, number, env, holder=None, request_freq = 0.1, computation_mean = 10.0, computation_stdev = 2.0):

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
        self.env = env
        self.number = number
        self.queue = []
        self.asked = 0
        self.using = 0
        self.left = 0
        self.request_freq = request_freq
        self.computation_mean = computation_mean
        self.computation_stdev = computation_stdev
        self.nhbrs = None

    def set_nhbrs(self, nhbrs):
        self.nhbrs = nhbrs

    def setHolder(self, holder):
        self.holder = holder

    # PEM
    # This function can not be broken up into smaller pieces due
    # to the limitations of generator functions in Python
    def receive_message(self, env, pipe):
        while True:
            # Only read those messages addressed to myself

            msg = yield pipe.get(lambda message: message.receiver == self and (message.message_type != personal_request
                                                                               or env.now != self.left))
            if msg.message_type == personal_request:
                self.queue.append(self)
            # resource request for a node
            elif msg.message_type == resource_request:
                self.queue.append(msg.sender)
            # Node has received the token from a neighbour
            elif msg.message_type == pass_key:
                self.holder = self

            print('at time %d: %s received message: %s.' %
                  (env.now, self.number, str(msg.message_type)))

            if self.holder == self and len(self.queue) != 0:
                self.holder = self.queue.pop(0)
                self.asked = 0
                if self.holder == self:
                    self.using = 1
                    # Entering the critical section
                    # TODO change to non-constant time amount
                    print('I am in the critical section' + str(self.number) + '   ' + str(self.env.now))
                    # Doing work in the critical section
                    yield self.env.timeout(10)
                    self.left = env.now
                    print('I am leaving ' + str(self.number) + '  ' + str(self.env.now))
                    # Node exits the critical section
                    self.using = 0

                    # When exiting the CS check to see if there are nodes
                    # waiting for the resource, and if so, and pass the key
                    # Note that because we assume that nodes will not

                    if self.holder == self and len(self.queue) != 0:
                        self.holder = self.queue.pop(0)
                        self.asked = 0
                        print('I got here!')
                        pipe.put(Message(self.holder, pass_key, self))

                    # Send request to the new holder in the case where there is more
                    # than one outstanding node on the queue.
                    if self.holder == self and len(self.queue) != 0 and self.asked == 0:
                        # TODO add calculation for sending speed
                        pipe.put(Message(self.holder, resource_request, self))
                        self.asked = 1

                else:
                    # TODO add calculation for sending speed
                    yield env.timeout()
                    pipe.put(Message(self.holder, pass_key, self))
            # make request

            if self.holder != self and len(self.queue) != 0 and self.asked == 0:
                # TODO add calculation for sending speed
                print('I make a request')
                pipe.put(Message(self.holder, resource_request, self))
                self.asked = 1

    def send_message(self, env, pipe):
        while True:
            yield env.timeout(random.expovariate(self.request_freq))
            msg = Message(self, personal_request)
            # Used to ensure that a node does not keep adding itself to the queue
            # when it is already waiting for the resource.
            # This is an assumption made in Raymond's algorithm.
            if pipe.items.count(self) == 0:
                pipe.put(msg)

    '''
        Finds the transmission time to send a message from Node "self" to Node "receiver" 
        using the node independent transmission speed. 
    '''
    def tranmission_time(self, receiver):


