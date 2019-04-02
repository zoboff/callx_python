# Usage example of the TrueConf SDK for Windows on Python 3.6

# Install PyQt5
> pip install pyqt5

## screen_capture.py 💻
Demostration of the screen capture

### How to run
Change next constants
```
CAPTURED_SCREEN = '1'
OTHER_USER_ID = '3@ruj2m.trueconf.name'
```

**Command:**

python screen_capture.py -s *SERVER_IP* -u *TRUECONF_ID* -p *PASSWORD*

**Example:**
```
python screen_capture.py -s "192.168.62.157" -u "1" -p "12345"
```

## get_devices.py 📹🔊🎤
Output list of devices on console: cams, mics and speakers

### How to run
**Command:**

python get_devices.py
