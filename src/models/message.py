import numpy as np


class MessageType:
    personal_request, resource_request, pass_key, enteringCS, exitingCS = range(5)


'''
    Represents the datatype that is sent between messages. Used for animation as well as Raymond Algorithm Logic. 
'''


class Message:

    def __init__(self, receiver, message_type, time_sent, sender=None):
        self.sender = sender
        self.receiver = receiver
        self.message_type = message_type
        self.time_sent = time_sent

        if message_type == MessageType.resource_request or message_type == MessageType.pass_key:
            self.trans_time = self.transmission_time(sender, receiver)

    '''
        Finds the transmission time to send a message from Node "self" to Node "receiver" 
        using the node independent transmission speed. 
    '''

    @staticmethod
    def transmission_time(sender, receiver):
        dist = np.linalg.norm(sender.position - receiver.position)
        return dist / sender.transmission_speed
