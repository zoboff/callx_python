# encode=utf8
'''
Created on 22 11 2018 

@author: zobov
'''
from PyQt5.QAxContainer import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject
import sys

TITLE = "CallX Example"
TrueConfCallX_Class = '{27EF4BA2-4500-4839-B88A-F2F4744FE56A}'

SERVER = '' # empty - connect to TrueConf Online cloud
USER = '<trueconf id>'
PASSWORD = '<password>'

class CallXWindow(QWidget):

    def __init__(self):
        QAxWidget.__init__(self)
        self.setWindowTitle(TITLE)
        self.move(400, 30)
# end of class CallXWindow(QWidget)


class ActiveXExtend(QObject):
    
    def __init__(self, view):
        super().__init__()
        self.view = view
        self.ocx = QAxWidget(TrueConfCallX_Class)

        self.ocx.move(0, 0)
        self.ocx.setFixedSize(640, 375)
        self.ocx.setParent(self.view)
        self.ocx.show()

        # receive ActiveX event 
        self.ocx.OnXAfterStart.connect(self._OnXAfterStart)
        self.ocx.OnServerConnected[str].connect(self._OnServerConnected)
        self.ocx.OnLogin[str].connect(self._OnLogin)
        self.ocx.OnInviteReceived[str].connect(self._OnInviteReceived)
        self.ocx.OnXError[int, str].connect(self._OnXError)
        self.ocx.OnXLoginError[int].connect(self._OnXLoginError)

    # Events
    def _OnXAfterStart(self):
        print("**receive OnXAfterStart")
        # select devices
        self.ocx.XSetCameraByIndex(0)
        self.ocx.XSelectMicByIndex(0)
        self.ocx.XSelectSpeakerByIndex(0)
        # connect to server
        self.ocx.connectToServer(SERVER)
    
    def _OnServerConnected(self, eventDetails):
        print("**receive OnServerConnected")
        print(eventDetails)
        # login
        self.ocx.login(USER, PASSWORD)
    
    def _OnLogin(self, eventDetails):
        print("**receive OnLogin")

    def _OnInviteReceived(self, eventDetails):
        print("**receive OnInviteReceived")
        print(eventDetails)
        # accept any
        self.ocx.accept()

    def _OnXError(self, errorCode, errorMsg):
        print("**receive OnXError")
        print('{}. Code: {}'.format(errorMsg, errorCode))

    def _OnXLoginError(self, errorCode):
        print("**receive OnXLoginError")
        if errorCode == 8:
            print('Support for SDK Applications is not enabled on this server')
        else:
            print('Login error. Code: {}'.format(errorCode))
# end of class ActiveXExtend(QObject):


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = CallXWindow()
    axwin = ActiveXExtend(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
