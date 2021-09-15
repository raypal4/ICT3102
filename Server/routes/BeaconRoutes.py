from flask import Blueprint, jsonify, request
from datasource.StaffGateway import StaffGateway

# Initialization
router = Blueprint("BeaconRoutes", __name__)

@router.route("/extractbeacon", methods=['GET', 'POST'])
def extractbeacon():
    staff_id = int(request.args.get('staff_id'))
    start_time = int(request.args.get('start_time'))
    end_time = int(request.args.get('end_time'))

    locations = StaffGateway().retrieve_staff_location(staff_id, start_time, end_time)
    return jsonify({
        "location": locations
    })