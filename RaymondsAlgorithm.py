from Node import Node
import numpy as np
import simpy
import random as rand
import networkx as nx



class SimulationInstance:

    def __init__(self, transmission_speed, num_nodes, computation_mean=10, computation_stdev=5, frequency_mean=0.1):

        self.G = nx.generators.trees.random_tree(num_nodes)
        self.transmission_speed = transmission_speed
        self.computation_mean = computation_mean
        self.computation_stdev = computation_stdev
        self.frequency_mean = frequency_mean
        self.num_nodes = num_nodes

        self.nodes = []
        self.env = simpy.Environment()

        self.init_nodes()

    def init_nodes(self):

        x_pos = rand.randint(0, 1000)
        y_pos = rand.randint(0, 1000)
        position = np.array([x_pos, y_pos])
        index = rand.randint(0, self.num_nodes - 1)

        # Select a node at random to be the holder
        initial_holder = Node(position, index, self, transmission_speed)
        initial_holder.setHolder(initial_holder)
        self.nodes.append(initial_holder)
        print(initial_holder)
        self.assign_directions(initial_holder, index, self.G)

    '''
        Assigns directions to the spanning tree associated with the spanning tree G. This is done 
        by expanding about the node holding the token, then recursively expanding about is children. 
        In each expansion we assign direction towards the original node.
        
    '''
    def assign_directions(self, parent, parent_index, prev_index=-1):
        print(parent_index)
        nhbrs = self.G.neighbors(parent_index)
        for node in nhbrs:
            if node != prev_index:
                x_pos = rand.randint(0, 1000)
                y_pos = rand.randint(0, 1000)
                position = np.array([x_pos, y_pos])
                new_node = Node(position, node, self, parent)
                self.nodes.append(new_node)
                self.assign_directions(new_node, node, parent_index)

    def start_simulation(self, simulation_time):
        pipe = simpy.FilterStore(self.env)

        for node in self.nodes:
            print(node)
            self.env.process(node.receive_message(self.env, pipe))
            self.env.process(node.generate_request(self.env, pipe))
        self.env.run(until=simulation_time)


num_nodes = 10
computation_mean = 10
computation_stdev = 10
frequency_mean = 0.05
transmission_speed = 1000

instance = SimulationInstance(transmission_speed, num_nodes, computation_mean, computation_stdev, frequency_mean)
instance.start_simulation(100)

