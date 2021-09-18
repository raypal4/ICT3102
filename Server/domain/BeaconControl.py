from datasource.StaffGateway import StaffGateway
from datasource.BeaconGateway import BeaconGateway

class BeaconControl:
    BeaconGateway = BeaconGateway()
    StaffGateway = StaffGateway()

    def retrieve_staff_location(self, staff_id, start_time, end_time):
        return StaffGateway.retrieve_staff_location(self, staff_id, start_time, end_time)

    def new_beacon_detect(self, beacon_address):
        beacon_details = BeaconGateway.get_location_details(self, beacon_address)
        # add new beacon detection details to db
        StaffGateway.add_new_staff_location(self, 0, beacon_details["beaconLevel"], beacon_details["beaconLocation"])