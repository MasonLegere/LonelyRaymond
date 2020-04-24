from AnimationLogger import AnimationLogger
from lib.Node import *
import numpy as np
import simpy
import random as rand
import networkx as nx


class SimulationInstance:

    def __init__(self, transmission_speed=100, num_nodes=1, computation_mean=10, computation_stdev=5, simulationTime = 30,
                 frequency_mean=0.1,
                 initial_holder=-1):

        self.simulationTime = simulationTime
        self.transmission_speed = transmission_speed
        self.computation_mean = computation_mean
        self.computation_stdev = computation_stdev
        self.frequency_mean = frequency_mean
        self.num_nodes = num_nodes
        self.initialHolderNum = initial_holder
        self.initialized = False

    def initializeTree(self):
        self.env = simpy.Environment()
        self.initialized = True
        self.undirG = nx.generators.trees.random_tree(self.num_nodes)
        self.G = self.undirG.to_directed()
        self.animation_logger = AnimationLogger(self)

        self.msg_log = []
        self.nodes = []

        x_pos = rand.randint(0, 1000)
        y_pos = rand.randint(0, 1000)
        position = np.array([x_pos, y_pos])
        if self.initialHolderNum == -1:
            self.initialHolderNum = rand.randint(0, self.num_nodes - 1)

        # Select a node at random to be the holder
        initial_holder = Node(position, self.initialHolderNum, self)
        self.initialHolderNum = initial_holder.number
        initial_holder.setHolder(initial_holder)
        self.nodes.append(initial_holder)
        self.assign_directions(initial_holder, self.G)

    '''
        Assigns directions to the spanning tree associated with the spanning tree G. This is done 
        by expanding about the node holding the token, then recursively expanding about is children. 
        In each expansion we assign direction towards the original node.
        
    '''

    def assign_directions(self, parent, prev_index=-1):

        nhbrs = self.undirG.neighbors(parent.number)
        old_edges = []

        for node in nhbrs:
            if node != prev_index:
                x_pos = rand.randint(0, 1000)
                y_pos = rand.randint(0, 1000)
                position = np.array([x_pos, y_pos])
                new_node = Node(position, node, self, parent)
                old_edges.append((parent.number, node))
                # self.G.remove_edge(parent.number, node)

                self.nodes.append(new_node)
                self.assign_directions(new_node, parent.number)
        self.G.remove_edges_from(old_edges)


    '''
        Activates the PEM methods for each Node as well as the AnimationLogger.
    '''
    def start_simulation(self, simulation_time):


        pipe = simpy.FilterStore(self.env)
        self.env.process(self.animation_logger.log_update(self.msg_log))

        for node in self.nodes:
            self.env.process(node.receive_message(self.env, pipe, self.msg_log))
            self.env.process(node.generate_request(self.env, pipe, self.msg_log))
        self.env.run(until=simulation_time)
