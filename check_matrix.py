# coding=utf8

from PyQt5.QAxContainer import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, QRect, pyqtSignal
from PyQt5.QtMultimedia import *
import sys
from PyQt5.Qt import QVideoWidget, QUrl, Qt
from callx import CallXWidget, State
import os.path
import argparse
import json
import config

# Title
TITLE = "CallX Python Test: Matrix"


# Main Window
class KioskWidget(QWidget):

    def __init__(self):
        self.layout = None
        self.callx_widget = None
        self.done = False

        QAxWidget.__init__(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle(TITLE)
        self.move(100, 100)  
        self.resize(640, 360)
        #self.setStyleSheet("background-color:black;")
        # layout
        self.layout = QHBoxLayout(self)
        self.setLayout(self.layout)
        # CallX
        self.callx_widget = CallXWidget(self, config.SERVER, config.USER, config.PASSWORD, camera_index = 0, debug_mode=True)
        self.layout.addWidget(self.callx_widget.ocx)
        # 
        self.left_frame = QFrame(self)
        self.layout.addWidget(self.left_frame)
        # frame layout
        self.frame_layout = QVBoxLayout(self)
        self.left_frame.setLayout(self.frame_layout)
        # M 0
        self.btn_matrixType0 = QPushButton('matrixType = 0')
        self.btn_matrixType0.clicked.connect(self.on_clickMartix0)
        self.frame_layout.addWidget(self.btn_matrixType0)
        # M 1
        self.btn_matrixType1 = QPushButton('matrixType = 1')
        self.btn_matrixType1.clicked.connect(self.on_clickMartix1)
        self.frame_layout.addWidget(self.btn_matrixType1)
        # M 2
        self.btn_matrixType2 = QPushButton('matrixType = 2')
        self.btn_matrixType2.clicked.connect(self.on_clickMartix2)
        self.frame_layout.addWidget(self.btn_matrixType2)
        # M 3
        self.btn_matrixType3 = QPushButton('matrixType = 3')
        self.btn_matrixType3.clicked.connect(self.on_clickMartix3)
        self.frame_layout.addWidget(self.btn_matrixType3)
        # M 4
        self.btn_matrixType4 = QPushButton('matrixType = 4')
        self.btn_matrixType4.clicked.connect(self.on_clickMartix4)
        self.frame_layout.addWidget(self.btn_matrixType4)
        # M 5
        self.btn_matrixType5 = QPushButton('matrixType = 5')
        self.btn_matrixType5.clicked.connect(self.on_clickMartix5)
        self.frame_layout.addWidget(self.btn_matrixType5)
        # M 6
        self.btn_matrixType6 = QPushButton('matrixType = 6')
        self.btn_matrixType6.clicked.connect(self.on_clickMartix6)
        self.frame_layout.addWidget(self.btn_matrixType6)        

        # connect to signals
        self.callx_widget.stateChanged.connect(self.onStateChanged)
        self.callx_widget.IncomingChatMessage.connect(self.onIncomingChatMessage)

    # ============================================================================================
    # Signals
    # ============================================================================================
    def onStateChanged(self, callx, prev_state, new_state):
        pass

    def onIncomingChatMessage(self, peerId, peerDn, message, time):
        pass
    # ============================================================================================

    def on_clickMartix0(self):
        self.callx_widget.ocx.setSettings('{"defaultP2PMatrix" : 0}')
        pass

    def on_clickMartix1(self):
        self.callx_widget.ocx.setSettings('{"defaultP2PMatrix" : 1}')
        pass

    def on_clickMartix2(self):
        self.callx_widget.ocx.setSettings('{"defaultP2PMatrix" : 2}')
        pass

    def on_clickMartix3(self):
        self.callx_widget.ocx.setSettings('{"defaultP2PMatrix" : 3}')
        pass

    def on_clickMartix4(self):
        self.callx_widget.ocx.setSettings('{"defaultP2PMatrix" : 4}')
        pass

    def on_clickMartix5(self):
        self.callx_widget.ocx.setSettings('{"defaultP2PMatrix" : 5}')
        pass

    def on_clickMartix6(self):
        self.callx_widget.ocx.setSettings('{"defaultP2PMatrix" : 6}')
        pass
    # ============================================================================================

# end of class CallXWindow(QWidget)

if __name__ == '__main__':
    # Check required variables
    if (not config.SERVER) or (not config.USER) or (not config.PASSWORD):
        print('Please set variables to connect and authorize. List variables: SERVER, USER, PASSWORD.')
        sys.exit()
    else:
        app = QApplication(sys.argv)
        MainWindow = KioskWidget()
        MainWindow.show()
        sys.exit(app.exec_())
