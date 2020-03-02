from simpy import Process
from simpy import *
from numpy import array
from Message import *


class Node:

    # Position is [x,y] vector
    def __init__(self, position, number, env, holder=None):
        self.holder = holder
        self.position = position
        self.env = env
        self.number = number
        self.queue = []
        self.asked = 0
        self.using = 0
        self.left = 0

    def setNhbrs(self, nhbrs):
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
                    pipe.put(Message(self.holder, pass_key, self))
            # make request
            # print('I make a requesttt')

            if self.holder != self and len(self.queue) != 0 and self.asked == 0:
                # TODO add calculation for sending speed
                print('I make a request')
                pipe.put(Message(self.holder, resource_request, self))
                self.asked = 1

    def send_message(self, env, pipe):
        while True:
            yield env.timeout(10)
            msg = Message(self, personal_request)
            # Used to ensure that a node does not keep adding itself to the queue
            # when it is already waiting for the resource.
            # This is an assumption made in Raymond's algorithm.
            if pipe.items.count(self) == 0:
                pipe.put(msg)
