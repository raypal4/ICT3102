import time
from flask import Request
from flask.globals import request
from domain.BeaconControl import BeaconControl

class ThreadController:
    def __init__(self):
        self.ExitThread = True
        self.BeaconControl = BeaconControl()

    def startWork(self, name):
        self.ExitThread = False
        while self.ExitThread == False:
            # temp function to simulate becaons detections
            self.BeaconControl.new_beacon_detect(0, "C2A628384B08")
            time.sleep(10)

    def stop(self):
        self.ExitThread = True

