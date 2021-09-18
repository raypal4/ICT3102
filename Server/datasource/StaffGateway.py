import pymongo
from datasource.Database import Database
import time
class StaffGateway:
    # Static
    __StaffCollection = Database.db["staff"]

    # retrieve all locations detected within the timestamp
    def retrieve_staff_location(self, id, start_time, end_time):
        collection = StaffGateway.__StaffCollection
        allStaffVisitedLocations = collection.find_one({"staff_id": id})["location"]

        temp = []
        for item in allStaffVisitedLocations:
            if start_time <= int(item["timestamp"]) <= end_time:
                temp.append(item)
        return temp

    # add new location based on user and detected beacon to the db
    def add_new_staff_location(self, user_address, level, location):
        print(user_address, level, location)
        new_location = {
            "level": level,
            "location": location,
            "timestamp": int(time.time())
        }
        collection = StaffGateway.__StaffCollection
        try:
            collection.find_one_and_update(
                {"staff_id": user_address}, 
                {"$push": 
                    {"location": 
                        {"$each": [new_location], "$position": 0}
                    }
                }
            )
            return True
        except Exception as e:
            print(e)
