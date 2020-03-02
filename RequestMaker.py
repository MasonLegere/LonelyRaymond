import numpy
from simpy import Process
import simpy
from MessageType import *

class RequestMaker():

    def __init__(self, nodes, time, message, env):
        self.nodes = nodes
        self.time = time
        self.message = message
        self.env = env

    #PEM
    def create_requests(self):
        self.message.send_message(self.nodes[0], personal_request)
        for i in range(2):
            self.message.send_message(self.nodes[i], personal_request)
            print(self.env.now)
            yield self.env.timeout(self.time)


