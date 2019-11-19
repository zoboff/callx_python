# coding=utf8
'''
The simplest minimal example for CallX
'''

from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
from callx import CallXWidget, State
import sys
import config

# Title
TITLE = "TrueConf CallX Python Test Template"


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
        self.setStyleSheet("background-color:black;")
        # layout
        self.layout = QHBoxLayout(self)
        self.setLayout(self.layout)
        # CallX
        self.callx_widget = CallXWidget(self, config.SERVER, config.USER, config.PASSWORD, camera_index = 0, debug_mode=True)
        self.layout.addWidget(self.callx_widget.ocx)

        # connect to signals
        self.callx_widget.stateChanged.connect(self.onStateChanged)
        self.callx_widget.IncomingChatMessage.connect(self.onIncomingChatMessage)

    # ============================================================================================
    # Signals
    # ============================================================================================
    def onStateChanged(self, prev_state, new_state):
        pass

    def onIncomingChatMessage(self, peerId, peerDn, message, time):
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
