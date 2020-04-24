
from PyQt5.QtGui import QColor
from NetworkDisplay import *
from PyQt5 import QtCore, QtGui, QtWidgets

from SimulationInstance import SimulationInstance

# Defines exception hook for better error messages
def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

'''
    Creates the user interface for the application. 
'''

class Ui_RaymondsAlgorithm(object):

    def __init__(self):
        self.instance = SimulationInstance()

    '''
        Generates GUI made by PyQt Designer. No modifications were made to this method.
    '''

    def setupUi(self, RaymondsAlgorithm):
        RaymondsAlgorithm.setWindowIcon(QtGui.QIcon("Images/executableIcon.png"))
        RaymondsAlgorithm.setObjectName("RaymondsAlgorithm")
        RaymondsAlgorithm.resize(680, 800)
        RaymondsAlgorithm.setStyleSheet("background-color: rgb(197, 197, 197);")
        RaymondsAlgorithm.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(RaymondsAlgorithm)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.simulationTimeValue = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.simulationTimeValue.sizePolicy().hasHeightForWidth())
        self.simulationTimeValue.setSizePolicy(sizePolicy)
        self.simulationTimeValue.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.simulationTimeValue.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.simulationTimeValue.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.simulationTimeValue.setText("")
        self.simulationTimeValue.setObjectName("simulationTimeValue")
        self.horizontalLayout_3.addWidget(self.simulationTimeValue)
        self.simulationTimeSlider = QtWidgets.QSlider(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.simulationTimeSlider.sizePolicy().hasHeightForWidth())
        self.simulationTimeSlider.setSizePolicy(sizePolicy)
        self.simulationTimeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.simulationTimeSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.simulationTimeSlider.setTickInterval(10)
        self.simulationTimeSlider.setObjectName("simulationTimeSlider")
        self.horizontalLayout_3.addWidget(self.simulationTimeSlider)
        self.simulationTimeStaticLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.simulationTimeStaticLabel.sizePolicy().hasHeightForWidth())
        self.simulationTimeStaticLabel.setSizePolicy(sizePolicy)
        self.simulationTimeStaticLabel.setStyleSheet("font: 8pt \"Terminal\";")
        self.simulationTimeStaticLabel.setObjectName("simulationTimeStaticLabel")
        self.horizontalLayout_3.addWidget(self.simulationTimeStaticLabel)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 2, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setStyleSheet("font: 8pt \"Terminal\";")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 4, 2, 1, 1)
        self.startSimulationBtn = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.startSimulationBtn.setStyleSheet("font: 24pt \"Terminal\";")
        self.startSimulationBtn.setIconSize(QtCore.QSize(40, 40))
        self.startSimulationBtn.setObjectName("startSimulationBtn")
        self.gridLayout.addWidget(self.startSimulationBtn, 3, 2, 1, 1)
        self.animationTime = QtWidgets.QLCDNumber(self.centralwidget)
        self.animationTime.setStyleSheet("background-color: rgb(255, 0, 0);\n"
                                         "")
        self.animationTime.setObjectName("animationTime")
        self.gridLayout.addWidget(self.animationTime, 2, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setStyleSheet("font: 7pt \"Terminal\";")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 2, 1, 1)
        self.animationDisplay = QtWidgets.QWidget(self.centralwidget)
        self.animationDisplay.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.animationDisplay.setObjectName("animationDisplay")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.animationDisplay)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout.addWidget(self.animationDisplay, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.initHolderLabel = QtWidgets.QLabel(self.centralwidget)
        self.initHolderLabel.setStyleSheet("font: 8pt \"Terminal\";")
        self.initHolderLabel.setObjectName("initHolderLabel")
        self.horizontalLayout_2.addWidget(self.initHolderLabel)
        self.initHolderBox = QtWidgets.QSpinBox(self.centralwidget)
        self.initHolderBox.setObjectName("initHolderBox")
        self.horizontalLayout_2.addWidget(self.initHolderBox)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 2, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("font: 8pt \"Terminal\";")
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 2, 1, 1)
        self.numNodesText = QtWidgets.QLabel(self.centralwidget)
        self.numNodesText.setStyleSheet("font: 8pt \"Terminal\";")
        self.numNodesText.setFrameShape(QtWidgets.QFrame.Box)
        self.numNodesText.setFrameShadow(QtWidgets.QFrame.Raised)
        self.numNodesText.setObjectName("numNodesText")
        self.gridLayout_2.addWidget(self.numNodesText, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("font: 8pt \"Terminal\";")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setStyleSheet("font: 8pt \"Terminal\";")
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 3, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setStyleSheet("font: 8pt \"Terminal\";")
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 4, 2, 1, 1)
        self.compSTDEVSlider = QtWidgets.QSlider(self.centralwidget)
        self.compSTDEVSlider.setOrientation(QtCore.Qt.Horizontal)
        self.compSTDEVSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.compSTDEVSlider.setTickInterval(10)
        self.compSTDEVSlider.setObjectName("compSTDEVSlider")
        self.gridLayout_2.addWidget(self.compSTDEVSlider, 2, 1, 1, 1)
        self.reqFrequencySlider = QtWidgets.QSlider(self.centralwidget)
        self.reqFrequencySlider.setOrientation(QtCore.Qt.Horizontal)
        self.reqFrequencySlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.reqFrequencySlider.setTickInterval(10)
        self.reqFrequencySlider.setObjectName("reqFrequencySlider")
        self.gridLayout_2.addWidget(self.reqFrequencySlider, 3, 1, 1, 1)
        self.compMeanSlider = QtWidgets.QSlider(self.centralwidget)
        self.compMeanSlider.setOrientation(QtCore.Qt.Horizontal)
        self.compMeanSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.compMeanSlider.setTickInterval(10)
        self.compMeanSlider.setObjectName("compMeanSlider")
        self.gridLayout_2.addWidget(self.compMeanSlider, 1, 1, 1, 1)
        self.tranSpeedSlider = QtWidgets.QSlider(self.centralwidget)
        self.tranSpeedSlider.setOrientation(QtCore.Qt.Horizontal)
        self.tranSpeedSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.tranSpeedSlider.setTickInterval(10)
        self.tranSpeedSlider.setObjectName("tranSpeedSlider")
        self.gridLayout_2.addWidget(self.tranSpeedSlider, 4, 1, 1, 1)
        self.numNodeOption = QtWidgets.QSpinBox(self.centralwidget)
        self.numNodeOption.setObjectName("numNodeOption")
        self.gridLayout_2.addWidget(self.numNodeOption, 0, 1, 1, 1)
        self.computationMeanVal = QtWidgets.QLabel(self.centralwidget)
        self.computationMeanVal.setText("")
        self.computationMeanVal.setObjectName("computationMeanVal")
        self.gridLayout_2.addWidget(self.computationMeanVal, 1, 0, 1, 1)
        self.ComputationSTDEVVal = QtWidgets.QLabel(self.centralwidget)
        self.ComputationSTDEVVal.setText("")
        self.ComputationSTDEVVal.setObjectName("ComputationSTDEVVal")
        self.gridLayout_2.addWidget(self.ComputationSTDEVVal, 2, 0, 1, 1)
        self.reqFreqVal = QtWidgets.QLabel(self.centralwidget)
        self.reqFreqVal.setText("")
        self.reqFreqVal.setObjectName("reqFreqVal")
        self.gridLayout_2.addWidget(self.reqFreqVal, 3, 0, 1, 1)
        self.transSpeedVal = QtWidgets.QLabel(self.centralwidget)
        self.transSpeedVal.setText("")
        self.transSpeedVal.setObjectName("transSpeedVal")
        self.gridLayout_2.addWidget(self.transSpeedVal, 4, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setStyleSheet("font: 8pt \"Terminal\";")
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 3, 0, 4, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.startAnimationBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startAnimationBtn.setStyleSheet("font: 8pt \"Terminal\";")
        self.startAnimationBtn.setObjectName("startAnimationBtn")
        self.horizontalLayout.addWidget(self.startAnimationBtn)
        self.pauseAnimationBtn = QtWidgets.QPushButton(self.centralwidget)
        self.pauseAnimationBtn.setStyleSheet("font: 8pt \"Terminal\";")
        self.pauseAnimationBtn.setObjectName("pauseAnimationBtn")
        self.horizontalLayout.addWidget(self.pauseAnimationBtn)
        self.resetAnimationBtn = QtWidgets.QPushButton(self.centralwidget)
        self.resetAnimationBtn.setStyleSheet("font: 8pt \"Terminal\";")
        self.resetAnimationBtn.setObjectName("resetAnimatioBtn")
        self.horizontalLayout.addWidget(self.resetAnimationBtn)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.outPutConsole = QtWidgets.QTextBrowser(self.centralwidget)
        self.outPutConsole.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "border-color: rgb(0, 255, 0);")
        self.outPutConsole.setObjectName("outPutConsole")
        self.gridLayout.addWidget(self.outPutConsole, 0, 2, 1, 1)
        RaymondsAlgorithm.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RaymondsAlgorithm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 680, 18))
        self.menubar.setObjectName("menubar")
        RaymondsAlgorithm.setMenuBar(self.menubar)

        self.retranslateUi(RaymondsAlgorithm)
        QtCore.QMetaObject.connectSlotsByName(RaymondsAlgorithm)

        self.customizationsActions()

    '''
        Modifies and updates objects created by the designer. Assigns default and domain values. 
    '''
    def customizationsActions(self):

        self.progressBar.setValue(0)
        self.outPutConsole.setTextColor(QColor(255, 255, 0))
        self.outPutConsole.append('=================================================   \n ' +
                                  '                              MESSAGE LOG                  \n ' +
                                  '=================================================')

        self.startAnimationBtn.clicked.connect(self.startAnimation)
        self.pauseAnimationBtn.clicked.connect(self.pauseAnimation)
        self.resetAnimationBtn.clicked.connect(self.resetAnimation)
        self.startSimulationBtn.clicked.connect(self.startSimulation)

        # Computation Mean Slider
        self.compMeanSlider.setTickInterval(10)
        self.compMeanSlider.setMinimum(0)
        self.compMeanSlider.setMaximum(20)
        self.compMeanSlider.setSliderPosition(3)
        self.compMeanSlider.valueChanged.connect(self.instanceChange)

        # Standard Deviation Slider
        self.compSTDEVSlider.setMinimum(0)
        self.compSTDEVSlider.setMaximum(10)
        self.compSTDEVSlider.setSliderPosition(1)
        self.compSTDEVSlider.valueChanged.connect(self.instanceChange)

        # Request Frequency Slider
        self.reqFrequencySlider.setMinimum(1)
        self.reqFrequencySlider.setMaximum(50)
        self.reqFrequencySlider.setSliderPosition(10)
        self.reqFrequencySlider.valueChanged.connect(self.instanceChange)

        # Transmission Speed Slider
        self.tranSpeedSlider.setTickInterval(50)
        self.tranSpeedSlider.setMinimum(0)
        self.tranSpeedSlider.setMaximum(1000)
        self.tranSpeedSlider.setSliderPosition(500)
        self.tranSpeedSlider.valueChanged.connect(self.instanceChange)

        # Length of the simulation that is done
        self.simulationTimeSlider.setTickInterval(10)
        self.simulationTimeSlider.setMinimum(10)
        self.simulationTimeSlider.setMaximum(100)
        self.simulationTimeSlider.setSliderPosition(30)
        self.simulationTimeSlider.valueChanged.connect(self.instanceChange)

        # Selecting the number of nodes in the simulation
        self.numNodeOption.setMinimum(1)
        self.numNodeOption.setMaximum(15)
        self.numNodeOption.setValue(5)
        self.numNodeOption.valueChanged.connect(self.instanceChange)

        # Setting initial instance values
        self.computationMeanVal.setText("3")
        self.ComputationSTDEVVal.setText("1")
        self.reqFreqVal.setText("10")
        self.transSpeedVal.setText("500")
        self.simulationTimeValue.setText("30")

        self.computationMeanVal.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ComputationSTDEVVal.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.reqFreqVal.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.transSpeedVal.setFrameShape(QtWidgets.QFrame.StyledPanel)


        width = self.animationDisplay.frameGeometry().width()
        height = self.animationDisplay.frameGeometry().height()
        self.networkAnimation = MyDynamicMplCanvas(self, parent=self.animationDisplay, width=width,
                                                   height=height, dpi=200)
        self.gridLayout_5.addWidget(self.networkAnimation)

        self.initHolderBox.valueChanged.connect(self.instanceChange)
        self.initHolderBox.setMinimum(-1)
        self.initHolderBox.setMaximum(15)
        self.initHolderBox.setValue(-1)

    '''
        Provide lables to the objects created by the designer 
    '''
    def retranslateUi(self, RaymondsAlgorithm):
        _translate = QtCore.QCoreApplication.translate
        RaymondsAlgorithm.setWindowTitle(_translate("RaymondsAlgorithm", "Raymonds Algorithm Simulator"))
        self.simulationTimeStaticLabel.setText(_translate("RaymondsAlgorithm", "Simulation Time"))
        self.startSimulationBtn.setText(_translate("RaymondsAlgorithm", "Run Simulation!"))
        self.label_6.setText(_translate("RaymondsAlgorithm", "CPSC 441 @ https://github.com/MasonLegere/raymondMutEx"))
        self.initHolderLabel.setText(_translate("RaymondsAlgorithm", "Initial Holder (-1 random)"))
        self.label_2.setText(_translate("RaymondsAlgorithm", "Computation STDEV"))
        self.numNodesText.setText(_translate("RaymondsAlgorithm", "# of Nodes"))
        self.label.setText(_translate("RaymondsAlgorithm", "Computation Mean"))
        self.label_3.setText(_translate("RaymondsAlgorithm", "Request Frequency"))
        self.label_4.setText(_translate("RaymondsAlgorithm", "Transmission Speed"))
        self.label_5.setText(_translate("RaymondsAlgorithm", " Values:"))
        self.startAnimationBtn.setText(_translate("RaymondsAlgorithm", "Start Animation"))
        self.pauseAnimationBtn.setText(_translate("RaymondsAlgorithm", "Pause Animation"))
        self.resetAnimationBtn.setText(_translate("RaymondsAlgorithm", "Reset Animation"))

    '''
        Method signalled whenever an instance value is change in the UI. 
        Affects of changing the instance are only seen after the simulation 
        has been restarted. 
    '''
    def instanceChange(self):

        self.computationMeanVal.setText(str(self.compMeanSlider.value()))

        self.ComputationSTDEVVal.setText(str(self.compSTDEVSlider.value()))
        self.reqFreqVal.setText(str(self.reqFrequencySlider.value()))
        self.transSpeedVal.setText(str(self.tranSpeedSlider.value()))
        self.simulationTimeValue.setText(str(self.simulationTimeSlider.value()))

        self.instance.computation_stdev = self.compSTDEVSlider.value()
        self.instance.computation_mean = self.compMeanSlider.value()
        self.instance.frequency_mean = 1 / self.reqFrequencySlider.value()
        self.instance.transmission_speed = self.tranSpeedSlider.value()
        self.instance.num_nodes = self.numNodeOption.value()
        self.instance.initialHolderNum = self.initHolderBox.value()
        self.instance.simulationTime = self.simulationTimeSlider.value()

    '''
        To start the DES simulation using the information currently by the instance. 
        Starting a simulation while an animation will cause it to stop. This is due 
        to the memory store structure used for dataframes. To avoid this twice the amount 
        of storage would be needed. 
        of storage would be needed. 
    '''
    def startSimulation(self):
        # Making sure the most recent values are being used:
        if self.instance.num_nodes - 1 < self.instance.initialHolderNum:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Invalid Option for Initial Holder: Node does not exist')
            error_dialog.exec_()
        else:
            self.instanceChange()
            self.networkAnimation.pushBack()
            self.instance.initializeTree()
            self.networkAnimation.attachLogger()
            self.outPutConsole.append('Simulation Complete \n ')
            self.instance.start_simulation(self.instance.simulationTime)

    '''
        Start the animation for the more recently conducted simulation. This is done by starting the timer over. 
        In the case where no recent simulation has been run a new instance we
    '''

    def startAnimation(self):
        self.networkAnimation.startTimer()

    '''
        Pause the timer for the animation, staying on the current "DataFrame" 
    '''

    def pauseAnimation(self):
        self.networkAnimation.timer.stop()

    """
        Reset to the most recent first frame in the most previously ran instance. In the case where a new simulation 
        was completed at the time reset was pressed it will have the same affect as if "startAnimation" was selected.
    """

    def resetAnimation(self):
        self.networkAnimation.resetFrame()


if __name__ == "__main__":
    import sys

    sys.excepthook = except_hook
    app = QtWidgets.QApplication(sys.argv)
    RaymondsAlgorithm = QtWidgets.QMainWindow()
    ui = Ui_RaymondsAlgorithm()
    ui.setupUi(RaymondsAlgorithm)
    RaymondsAlgorithm.show()
    sys.exit(app.exec_())
