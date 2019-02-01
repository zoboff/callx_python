# coding=utf8

from PyQt5.QAxContainer import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, QRect, pyqtSignal
from callx import CallXWidget

# Main Window
class KioskWidget(QWidget):

    def __init__(self, title, server, user, password):
        self.title = title
        self.server = server 
        self.user = user 
        self.password = password
        self.layout = None
        self.callx_widget = None
        self.video = None
        self.player = None
        self.playlist = None
        
        QAxWidget.__init__(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.move(100, 100)  
        self.resize(800, 600)
        self.setStyleSheet("background-color:black;");
        self.showMaximized()
        # layout
        self.layout = QHBoxLayout(self)
        self.setLayout(self.layout)
        # CallX
        self.callx_widget = CallXWidget(self, self.server, self.user, self.password, debug_mode=False)
        self.layout.addWidget(self.callx_widget.ocx)

# end of class CallXWindow(QWidget)
