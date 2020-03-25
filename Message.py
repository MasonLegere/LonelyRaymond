import numpy
from simpy import Process
import simpy
from MessageType import *


class Message:
    transmission_speed = 1.0

    def __init__(self, receiver, message_type, sender=None, time_sent = -1):
        self.sender = sender
        self.receiver = receiver
        self.message_type = message_type
        self.time_sent = time_sent


