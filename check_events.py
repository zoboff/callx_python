# coding=utf8

from PyQt5.QAxContainer import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
import sys
from PyQt5.Qt import QVideoWidget, QUrl, Qt
from callx import CallXWidget, State
import os.path
import argparse
import json

# ================================================================
# Required variables: server IP, user_id (TrueConf ID), password
# ================================================================
SERVER = '' # server.name URL or server IP
USER = '<trueconf id>'
PASSWORD = '<password>'
# ================================================================

# Title
TITLE = "CallX Python Example: Check CallX Events"

EVENTS = [
"OnXNotify",
"OnXAfterStart",
"OnServerConnected",
"OnLogin",
"OnInviteReceived",
"OnXError",
"OnXLoginError",
"OnIncomingChatMessage",
"OnXChangeState",
"OnXTerminate",
"OnXStartFail",
"OnAbookUpdate",
"OnAppUpdateAvailable",
"OnChangeVideoMatrixReport",
"OnConferenceCreated",
"OnConferenceDeleted",
"OnContactBlocked",
"OnContactDeleted",
"OnContactUnblocked",
"OnHardwareChanged",
"OnDetailInfo",
"OnDeviceModesDone",
"OnIncomingRequestToPodiumAnswered",
"OnInviteRequestSent",
"OnInviteSent",
"OnLogout",
"OnReceiversInfoUpdated",
"OnRecordRequest",
"OnRecordRequestReply",
"OnRejectReceived",
"OnRejectSent",
"OnRemarkCountDown",
"OnRequestInviteReceived",
"OnRoleChanged",
"OnSelfSSInfoUpdate",
"OnServerConnected",
"OnServerDisconnected",
"OnSettingsChanged",
"OnSlideShowStart",
"OnSlideShowStop",
"OnStopCalling",
"OnUpdateAvatar",
"OnUpdateCameraInfo",
"OnUpdateParticipantList",
"OnRestrictionsChanged",
"OnVideoMatrixChanged",
"OnOffHookPressed",
"OnHangUpPressed",
"OnJabraHookOffPressed",
"OnJabraHangUpPressed",
"OnXCommandExecution",
"OnSlideShowInfoUpdate",
"OnStart",
"OnXLogin",
"OnXFileStatusChange",
"OnXFileSendError",
"OnXFileReceiveProgress",
"OnXFileReceive",
"OnXFileSend",
"OnCommandReceived",
"OnBroadcastPictureStateChanged",
"OnCallHistoryUpdated",
"OnCmdAddToAbook",
"OnCmdAddToGroup",
"OnCmdBlock",
"OnCmdChatClear",
"OnCmdCreateGroup",
"OnCmdRemoveFromAbook",
"OnCmdRemoveFromGroup",
"OnCmdRemoveGroup",
"OnCmdRenameGroup",
"OnCmdRenameInAbook",
"OnCmdUnblock",
"OnCommandSent",
"OnFileAccepted",
"OnFileConferenceSent",
"OnFileRejected",
"OnFileSent",
"OnFileTransferAvailable",
"OnGroupsUpdate",
"OnIncomingGroupChatMessage",
"OnGroupChatMessageSent",
"OnChatMessageSent",
"OnTestAudioCapturerStateUpdated",
"OnAudioCapturerRmsLevelUpdated",
"OnToneDial"
]


# Main Window
class KioskWidget(QWidget):

    def __init__(self, monitor: int = 0):
        self.layout = None
        self.callx_widget = None
        self.video = None
        self.player = None
        self.playlist = None
        self.monitor = monitor
        self.done = False
        self.events_log = {}
        EVENTS.sort()

        QAxWidget.__init__(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle(TITLE)
        self.move(0, 0)  
        self.resize(640, 360)
        # layout
        self.layout = QHBoxLayout(self)
        self.setLayout(self.layout)
        # === CallX widget
        self.callx_widget = CallXWidget(self, SERVER, USER, PASSWORD, camera_index = 0, debug_mode=True)
        self.layout.addWidget(self.callx_widget.ocx)
        # connect to signals
        self.callx_widget.stateChanged.connect(self.onStateChanged)
        self.callx_widget.IncomingChatMessage.connect(self.onIncomingChatMessage)
        # events
        self.callx_widget.onEvent.connect(self.onCallXEvent)
        self.callx_widget.onEventArg.connect(self.onCallXEventArg)
        # === listEventsWidget
        self.listEventsWidget = QListWidget()
        self.initListEventsWidget() # add all events
        self.listEventsWidget.clicked.connect(self.listEventsWidget_clicked)
        self.layout.addWidget(self.listEventsWidget)
        # === textWidget    
        self.textWidget = QTextEdit()
        self.layout.addWidget(self.textWidget)  

    def initListEventsWidget(self):
        for event in EVENTS:
            item = QListWidgetItem(event)
            item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            item.setCheckState(False)
            self.listEventsWidget.addItem(item)
            #self.listEventsWidget.insertItem(self.listEventsWidget.count(), event)
    # ============================================================================================
    # Signals
    # ============================================================================================
    def onStateChanged(self, prev_state, new_state):
        if self.callx_widget.debug_mode:
            print('Signal onStateChanged: "{}" -> "{}"'.format(prev_state, new_state))

    def onIncomingChatMessage(self, peerId, peerDn, message, time):
        pass
    # ============================================================================================
    def listEventsWidget_clicked(self, qmodelindex):
        item = self.listEventsWidget.currentItem()
        if item.text() in self.events_log:
            txt = "\n\n".join(self.events_log[item.text()])
            self.textWidget.setText(txt)
        else:
            self.textWidget.setText("")

    def onCallXEvent(self, name):
        self.events_log.setdefault(name, [name])
        items_list = self.listEventsWidget.findItems(name, Qt.MatchExactly)
        for item in items_list:
            item.setCheckState(True) 

    def onCallXEventArg(self, name, arg):
        self.events_log.setdefault(name, [])
        self.events_log[name].append(str(arg))

# end of class CallXWindow(QWidget)

if __name__ == '__main__':
    # command line
    ##  monitor
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--monitor", dest="monitor",
                    help="Index of the monitor.", type=int)
    args = parser.parse_args()
    monitor = args.monitor
    # Check required variables
    if (not SERVER) or (not USER) or (not PASSWORD):
        print('Please set variables to connect and authorize. List variables: SERVER, USER, PASSWORD.')
        sys.exit()
    else:
        app = QApplication(sys.argv)
        MainWindow = KioskWidget(monitor)
        MainWindow.show()
        sys.exit(app.exec_())
