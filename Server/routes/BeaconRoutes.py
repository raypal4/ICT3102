from flask import Blueprint, jsonify, request
from domain.Thread import Thread
from domain.ThreadController import ThreadController
from domain.BeaconControl import BeaconControl
# Initialization
router = Blueprint("BeaconRoutes", __name__)

# Globals
ThreadCounter = 0
ThreadController = ThreadController()
BeaconControl = BeaconControl()

@router.route("/extractbeacon", methods=['GET', 'POST'])
def extractBeacon():
    staff_id = int(request.args.get('staff_id'))
    start_time = int(request.args.get('start_time'))
    end_time = int(request.args.get('end_time'))

    locations = BeaconControl.retrieve_staff_location(staff_id, start_time, end_time)
    return jsonify({
        "location": locations
    })

@router.route("/newbeacondetect", methods=['GET','POST'])
def newBeaconDetect():
    # user_address = request.args.get('user_address')
    # beacon_address = request.args.get('beacon_address')
    BeaconControl.new_beacon_detect("C2A628384B08")
    return f"New Beacon Detection Added" 

### Test routes for beacon creation ###
# Start Beacon detected every 10 seconds 
@router.route("/starttestbeaconcreation")
def start_test_thread():
    global ThreadCounter, ThreadController

    if ThreadCounter <= 0:
        instance = Thread(1, "testBeaconDetection", ThreadController)
        instance.start()
        ThreadCounter += 1
        return "adding in beacons every 10 second hopefully"
    else:
        return "thread to creation detections already running"

# Stop Beacon detection
@router.route("/stoptestbeaconcreation")
def stop_test_thread():
    global ThreadCounter, ThreadController
    ThreadController.stop()
    ThreadCounter -= 1
    return "thread stopped"

