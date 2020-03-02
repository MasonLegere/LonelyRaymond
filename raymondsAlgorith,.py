import MessageType
from Message import Message
from Node import Node
from RequestMaker import *
import numpy as np
import simpy
from MessageType import *

env = simpy.Environment()
Message.transmission_speed = 2.0
Message.env = env
time = 10
nodes = []
pipe = simpy.FilterStore(env, capacity = 100)
node1 = Node(np.asarray([0,1]), 1, env)
node1.setHolder(node1)
nodes.append(node1)
node2 = Node(np.asarray([0,2]), 2, env, holder=node1)
nodes.append(node2)

env.process(node1.receive_message(env, pipe))
env.process(node1.send_message(env, pipe))

env.process(node2.receive_message(env,pipe))
env.process(node2.send_message(env,pipe))

env.run(100)



# env.process(np.asarray([0,1]))


