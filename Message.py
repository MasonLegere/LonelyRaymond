import numpy
from simpy import Process
import simpy
from MessageType import *


class Message:
    transmission_speed = 1.0

    def __init__(self, receiver, message_type, sender=None):
        self.sender = sender
        self.receiver = receiver
        self.message_type = message_type

# # PEM
# @classmethod
# def send_message(cls, receiver, message_type, sender=None):
#     print(type(receiver))
#     if message_type != personal_request:
#         print(Message.transmission_time(sender, receiver))
#         yield Message.env.timeout(Message.trasmission_time(sender, receiver))
#     receiver.run(message_type, sender)
#
# @classmethod
# def transmission_time(cls, sender, receiver):
#     # Transmission time assumed to be linear at the moment as  function
#     # Euclidean distance between the sender and receiver
#     sender_pos, receiver_pos = (sender.position, receiver.position)
#     return numpy.linalg.norm(sender_pos - receiver_pos)
