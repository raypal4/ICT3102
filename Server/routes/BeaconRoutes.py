from flask import Blueprint, jsonify, request
from domain.BeaconControl import BeaconControl
import pybreaker

# Initialization
router = Blueprint("BeaconRoutes", __name__)

BeaconControl = BeaconControl()
route_breaker = pybreaker.CircuitBreaker(fail_max=5, reset_timeout=30)

@router.route("/extractbeacon", methods=['GET', 'POST'])
@route_breaker
def extractBeacon():
    staff_id = int(request.args.get('staff_id'))
    start_time = int(request.args.get('start_time'))
    end_time = int(request.args.get('end_time'))

    locations = BeaconControl.retrieve_staff_location(
        staff_id, start_time, end_time)
    return jsonify({
        "location": locations
    })

@router.route("/newbeacondetect", methods=['GET', 'POST'])
@route_breaker
def newBeaconDetect():
    user_address = int(request.args.get('user_address'))
    beacon_address = request.args.get('beacon_address')
    rssi = int(request.args.get('rssi'))
    BeaconControl.new_beacon_detect(user_address, beacon_address, rssi)
    return f"New Beacon Detection Added"

@router.route("/retrieveformonitoring", methods=['GET', 'POST'])
@route_breaker
def retrieveForMonitoring():
    data = BeaconControl.retrieve_all_staff()
    return jsonify({
        "data": data
    })