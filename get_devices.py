# coding=utf8

from PyQt5.QtWidgets import QApplication
import sys
import window
import argparse
from callx import State

# Title
TITLE = "CallX Python Example: Get Devices Lists"

class MyApp(QApplication):
    
    def __init__(self, argv):
        self.MainWindow = None
        QApplication.__init__(self, argv)

    # ============================================================================================
    # Signals
    # ============================================================================================
    def onStartComplited(self):
        print("*** Cameras")
        print(self.MainWindow.callx_widget.ocx.XGetCameraList())
        print("*** Mics")
        print(self.MainWindow.callx_widget.ocx.XGetMicList())
        print("*** Speakers")
        print(self.MainWindow.callx_widget.ocx.XGetSpeakerList())
        sys.exit()


if __name__ == '__main__':
    app = MyApp(sys.argv)
    # Window
    app.MainWindow = window.KioskWidget(TITLE, "", "", "")
    # connect to signal
    app.MainWindow.callx_widget.startComplited.connect(app.onStartComplited)

    # show
    app.MainWindow.show()
    sys.exit(app.exec_())
