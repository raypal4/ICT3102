from datasource.Database import Database

class StaffGateway:
    # Static
    __StaffCollection = Database.db["staff"]

    def retrieve_staff_location(self, id, start_time, end_time):
        collection = StaffGateway.__StaffCollection
        allStaffVisitedLocations = collection.find_one({"staff_id": id})["location"]

        temp = []
        for item in allStaffVisitedLocations:
            if start_time <= int(item["timestamp"]) <= end_time:
                temp.append(item)

        return temp
