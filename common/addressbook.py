# coding=utf8

import json
from PyQt5.QtGui import *
from enum import Enum

# user status
# ===
# -1      - unknown
# 0       - user offline
# 1       - avialable user 
# 2       - busy
# 5       - user is a conference owner

KEY_ADDRESSBOOK = 'abook'
KEY_STATUS = "status"
KEY_ID = "peerId"
KEY_NAME = "peerDn"

class AddressbookUserStatus(Enum):
    Unknown = -1
    Offline = 0
    Avialable = 1
    Busy = 2
    ConferenceOwner = 5

# {"peerDn": "...", "status": -1}
# {"peerId": {"peerDn": "...", "status": -1}}
class AddressBook():

    def __init__(self):
        self.data = {}
        
    def update(self, json_data):
        update_data = json.loads(json_data)
        for user in update_data[KEY_ADDRESSBOOK]:
            id = user[KEY_ID]
            dn = user[KEY_NAME]
            status = user[KEY_STATUS]
            # update data
            self.data.setdefault(id, {})
            self.data[id][KEY_NAME] = dn
            self.data[id][KEY_STATUS] = status
    
    def userStatus(self, peerId: str) -> int:
        if peerId in self.data.keys():
            return self.data[id][KEY_STATUS]
        else:
            return AddressbookUserStatus.Unknown
        
    def userExist(self, peerId: str) -> bool:
        return (peerId in self.data.keys())

    def getAllIds(self):
        yield id in self.data.keys()

    def getAllOnlineUsers(self):
        result = set()
        for id in self.data.keys():
            if self.data[id][KEY_STATUS] in [AddressbookUserStatus.Avialable.value, AddressbookUserStatus.Busy.value, AddressbookUserStatus.ConferenceOwner.value]:
                result.add(id)
                
        return result

# ===================================

# user status
# ===
# -1      - unknown
# 0       - user offline
# 1       - avialable user 
# 2       - busy
# 5       - user is a conference owner

colors = [ '#ebebeb', '#fdc086', '#7ef77b', '#386cb0', '#fbf09f', '#beaed4', '#f7ff98']
def getStatusColor(status) -> int:
    return QColor(colors[status + 1]) 
            