import MessageType
from Message import Message
from Node import Node
from RequestMaker import *
import numpy as np
import simpy
import random as rand
import networkx as nx

from MessageType import *


class SimulationInstance():
    # TODO see if frequency mean is valid

    def __init__(self, transmission_speed, num_nodes, computation_mean=10, computation_stdev=5, frequency_mean=0.1):
        self.transmission_speed = transmission_speed
        self.computation_mean = computation_mean
        self.computation_stdev = computation_stdev
        self.frequency_mean = frequency_mean
        self.num_nodes = num_nodes

        self.nodes = []
        self.env = simpy.Environment()

        self.init_nodes()

    def init_nodes(self):
        G = nx.generators.trees.random_tree(self.num_nodes)
        print(G)
        x_pos = rand.randint(0, 1000)
        y_pos = rand.randint(0, 1000)
        position = np.array([x_pos, y_pos])
        index = rand.randint(0, self.num_nodes)

        newNode = []

        initial_holder = Node(position, index, self.env, request_freq=frequency_mean, computation_mean=computation_mean,
                              computation_stdev=computation_stdev)
        listy = [n for n in G.neighbors(index)]
        initial_holder.setHolder(initial_holder)
        self.assign_directions(initial_holder, index, G)


    def assign_directions(self, parent, parent_index, G, prev_index=-1):
        listy = [n for n in G[parent_index]]
        temp_node = None
        for node in [n for n in G.neighbors(parent_index)]:
            if node != prev_index:
                x_pos = rand.randint(0, 1000)
                y_pos = rand.randint(0, 1000)
                position = np.array([x_pos, y_pos])
                temp_node = Node(position, node, self.env, holder=parent, request_freq=frequency_mean,
                                 computation_mean=computation_mean,
                                 computation_stdev=computation_stdev)
                self.nodes.append(temp_node)
                self.assign_directions(temp_node, node, parent_index)


# This code is currently being used for testing
# TODO create functionality for the generation of arbitrary spanning trees


num_nodes = 10
computation_mean = 10
computation_stdev = 10
frequency_mean = 10
transmission_speed = 2.0

instance = SimulationInstance(transmission_speed, num_nodes, computation_mean, computation_stdev, frequency_mean)
env = simpy.Environment()
time = 10
nodes = []
pipe = simpy.FilterStore(env, capacity=100)
node1 = Node(np.asarray([0, 1]), 1, env)
node1.setHolder(node1)
nodes.append(node1)
node2 = Node(np.asarray([0, 2]), 2, env, holder=node1)
nodes.append(node2)

env.process(node1.receive_message(env, pipe))
env.process(node1.generate_request(env, pipe))

env.process(node2.receive_message(env, pipe))
env.process(node2.generate_request(env, pipe))

env.run(100)

# env.process(np.asarray([0,1]))
