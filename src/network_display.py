import sys
import matplotlib

# Make sure that we are using QT5
from src.models.message import MessageType

matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import networkx as nx

sys._excepthook = sys.excepthook

'''
    Setting hook so that PyQt gives meaningful error messages
'''
def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class MyMplCanvas(FigureCanvas):
    def __init__(self, GUI, width, height, dpi=100, parent=None):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.ax = fig.add_subplot(111)
        self.instance = GUI.instance

        self.animationTime = GUI.animationTime
        self.outputConsole = GUI.outPutConsole
        self.progressBar = GUI.progressBar
        self.simulationTime = GUI.instance.simulationTime


        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)


class MyDynamicMplCanvas(MyMplCanvas):
    """A canvas that updates itself every second with a new plot."""

    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)

        self.frameCount = 0
        self.timer = QtCore.QTimer(self)
        self.animationTime.display(0)

    def resetFrame(self):
        self.frameCount = 0
        self.animationTime.display(0)




    def pushBack(self):
        self.timer.stop()
        self.resetFrame()

    def attachLogger(self):
        self.data = self.instance.animation_logger.log
        self.holder = self.instance.initialHolderNum

    def startTimer(self):
        if self.instance.initialized and len(self.data) > 0:
            self.pos = nx.spring_layout(self.data[0].graph_instance)
            self.timer.timeout.connect(self.update_figure)
            self.timer.start(1)

    def update_figure(self):

        self.ax.cla()
        # Every tenth frame update the time displayed

        currentTime = 0.01*self.frameCount
        if self.frameCount % 10 == 0:
            self.animationTime.display(currentTime)

        graph = self.data[self.frameCount].graph_instance
        messages = self.data[self.frameCount].message_log
        message_history = self.data[self.frameCount].message_history

        personal_requests = []
        request_transfers = []
        key_transfers = []

        for msg in message_history:
            if msg.message_type == MessageType.pass_key:
                self.outputConsole.append(
                    '>> T = ' + str(round(msg.time_sent, 1)) + ' PRIVILEGE:   ' + str(msg.sender.number) + ' -> ' + str(
                        msg.receiver.number) + '\n')
            elif msg.message_type == MessageType.personal_request:
                self.outputConsole.append(
                    '>> T = ' + str(round(msg.time_sent, 1)) + ' RESOURCE REQUEST:   ' + str(
                        msg.receiver.number) + '\n')
            elif msg.message_type == MessageType.resource_request:
                self.outputConsole.append(
                    '>> T = ' + str(round(msg.time_sent, 1)) + ' REQUEST MESSAGE:   ' + str(
                        msg.sender.number) + ' -> ' + str(
                        msg.receiver.number) + '\n')
            elif msg.message_type == MessageType.enteringCS:
                self.outputConsole.append(
                    '>> T = ' + str(round(msg.time_sent, 1)) + ' ENTERING CS:   ' + str(
                        msg.receiver.number) + '\n')
            elif msg.message_type == MessageType.exitingCS:
                self.outputConsole.append(
                    '>> T = ' + str(round(msg.time_sent, 1)) + ' EXITING CS:   ' + str(
                        msg.receiver.number) + '\n')


        self.progressBar.setValue((currentTime / self.simulationTime) * 100)

        # Nodes that asked to enter the critical section
        for msg in messages:
            if msg.message_type == MessageType.pass_key:
                key_transfers.append((msg.sender.number, msg.receiver.number))
                self.holder = msg.receiver.number
            elif msg.message_type == MessageType.personal_request:
                personal_requests.append(msg.receiver.number)
            elif msg.message_type == MessageType.resource_request:
                request_transfers.append((msg.sender.number, msg.receiver.number))



        yellow_edges = set(key_transfers)
        red_edges = set(request_transfers) - set(key_transfers)
        gray_edges = set(graph.edges()) - set(request_transfers + key_transfers)
        blue_nodes = set(personal_requests) - {self.holder}
        white_nodes = set(graph.nodes()) - set(personal_requests + [self.holder])


        '''
            Colours directed network edges corresponding to messages being sent: 

                Yellow <- privilege message being sent
                Red    <- request message being sent
                Gray   <- No messages being sent 
        '''
        nx.draw_networkx_edges(graph, pos=self.pos, edgelist=yellow_edges, width=1,
                               ax=self.ax, edge_color='y',
                               arrowstyle='fancy')

        nx.draw_networkx_edges(graph, pos=self.pos, edgelist=red_edges,
                               width=1, ax=self.ax, edge_color='r',
                               arrowstyle='fancy')

        nx.draw_networkx_edges(graph, pos=self.pos, ax=self.ax, edge_color="gray",
                               edgelist=gray_edges, width=1,
                               arrowstyle='fancy')

        '''
            Colours network node corresponding to their state: 

                Yellow <- Node holds the token
                Blue   <- Node has made a personal request
                Gray   <- Null state... nothing going on
        '''
        nx.draw_networkx_nodes(graph, pos=self.pos, nodelist=[self.holder],
                               node_color="yellow",
                               ax=self.ax,
                               with_labels=True)

        nx.draw_networkx_nodes(graph, pos=self.pos, nodelist=blue_nodes, node_color='b',
                               ax=self.ax, with_labels=True)

        n = nx.draw_networkx_nodes(graph, pos=self.pos,
                                   nodelist=white_nodes,
                                   node_color="white",
                                   ax=self.ax,
                                   with_labels=True)
        # Set the border colour of the white nodes
        # Somewhat of a hacky solution
        if n is not None:
            n.set_edgecolor("black")

        nx.draw_networkx_labels(graph, pos=self.pos, ax=self.ax, font_weight=200);
        self.draw()
        self.frameCount = (self.frameCount + 1) % len(self.data)
