import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from Message import *
import matplotlib.animation

from Node import Node
from NodeLogger import NodeLogger


class AnimationProcess:

    def __init__(self, instance, delay_amount):

        self.G = instance.G
        self.pos = nx.spring_layout(self.G)
        self.delay_amount = delay_amount
        self.fig, self.ax = plt.subplots(figsize=(6, 4))
        self.instance = instance
        self.logger = NodeLogger(instance)


    def log_update(self, msg, pipe):

        old_messages = []
        new_messages = []

        while True:
            previous_time = self.instance.env.now

            # Add all messages that have just been sent to the queue
            while previous_time + self.delay_amount < self.instance.env.now:
                msg = yield pipe.get()
                trans_time = msg.sender.transmission_time(msg.receiver)
                new_messages.append((msg.sender.number, msg.receiver, msg.message_type, msg.time_sent, trans_time))

            # Remove messages from he queue that have reached their destination
            for msg in old_messages:
                if msg[3] + msg[4] > previous_time:
                    old_messages.remove(msg)

            old_messages = old_messages + new_messages
            self.logger.msglog.append(old_messages)


    def frame_update(self, message):


    def update(num):

