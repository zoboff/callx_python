# coding=utf8

from PyQt5.QtWidgets import QApplication
import sys
import window_kiosk
import argparse
from callx import State

# Title
TITLE = "CallX Python Example: Screen capture"

class MyApp(QApplication):
    
    def __init__(self, argv):
        self.MainWindow = None
        QApplication.__init__(self, argv)

    # ============================================================================================
    # Signals
    # ============================================================================================
    def onStartComplited(self):
        #self.MainWindow.callx_widget.ocx.XDeselectCamera()
        self.MainWindow.callx_widget.ocx.XSetCameraByIndex(0)
        self.MainWindow.callx_widget.ocx.XSelectMicByIndex(0)
        self.MainWindow.callx_widget.ocx.XSelectSpeakerByIndex(0)

    def onStateChanged(self, prev_state, new_state):
        if prev_state == State.Login and new_state == State.Normal:
            print('** Start Screen Capture')
            self.MainWindow.callx_widget.ocx.startScreenCapture('1')
            self.MainWindow.callx_widget.ocx.call('3@ruj2m.trueconf.name')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--server", dest="server", help="Server IP.", type=str)
    parser.add_argument("-u", "--user", dest="user", help="TrueConf ID.", type=str)
    parser.add_argument("-p", "--password", dest="password", help="Password.", type=str)
    args = parser.parse_args()
    app = MyApp(sys.argv)
    # Window
    app.MainWindow = window_kiosk.KioskWidget(TITLE, args.server, args.user, args.password)
    # connect to signal
    app.MainWindow.callx_widget.startComplited.connect(app.onStartComplited)
    app.MainWindow.callx_widget.stateChanged.connect(app.onStateChanged)    
    
    # show
    app.MainWindow.show()
    sys.exit(app.exec_())
