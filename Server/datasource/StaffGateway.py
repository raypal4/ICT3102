import pymongo
from datasource.Database import Database
import time
class StaffGateway:
    # Static
    __StaffCollection = Database.db["staff"]

    # Get all staff locations 
    def retrieve_all_staff(self):
        collection = StaffGateway.__StaffCollection
        return list(collection.find({}))

    # retrieve all locations detected within the timestamp for one user
    def retrieve_staff_location(self, id, start_time, end_time):
        collection = StaffGateway.__StaffCollection
        allStaffVisitedLocations = collection.find_one({"staff_id": id})["location"]

        temp = []
        for item in allStaffVisitedLocations:
            # if timestamp is greater then the endtime, break out of the loop. Dont need to check the rest
            if int(item["timestamp"]) > end_time:
                break
            if start_time <= int(item["timestamp"]) <= end_time:
                temp.append(item)

        return temp

    # add new location based on user and detected beacon to the db
    def add_new_staff_location(self, user_address, level, location, rssi, beacon_address):
        new_location = {
            "level": level,
            "location": location,
            "timestamp": int(time.time()),
            "rssi": rssi,
            "mac": beacon_address
        }
        collection = StaffGateway.__StaffCollection
        try:
            collection.find_one_and_update(
                {"staff_id": user_address}, 
                {"$push": 
                    {"location": 
                        {"$each": [new_location], "$position": 0}
                    }
                }, upsert=True
            )
            return True
        except Exception as e:
            print(e)
