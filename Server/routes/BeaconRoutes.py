from flask import Blueprint, jsonify, request
from datasource.StaffGateway import StaffGateway
from datasource.BeaconGateway import BeaconGateway

# Initialization
router = Blueprint("BeaconRoutes", __name__)

@router.route("/extractbeacon", methods=['GET', 'POST'])
def extractBeacon():
    staff_id = int(request.args.get('staff_id'))
    start_time = int(request.args.get('start_time'))
    end_time = int(request.args.get('end_time'))

    locations = StaffGateway().retrieve_staff_location(staff_id, start_time, end_time)
    return jsonify({
        "location": locations
    })

@router.route("/newbeacondetect", methods=['GET','POST'])
def newBeaconDetect():
    # user_address = request.args.get('user_address')
    # beacon_address = request.args.get('beacon_address')
    beacon_details = BeaconGateway().get_location_details("C2A628384B08")
    print(beacon_details)

    # add new beacon detection details to db
    StaffGateway().add_new_staff_location(0, beacon_details["beaconLevel"], beacon_details["beaconLocation"])
    return f"New Beacon Detection Added" 

