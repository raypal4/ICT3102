from flask import jsonify
from datasource.Database import Database

class BeaconGateway:
    # Static
    __BeaconCollection = Database.db["beacons"]

    temp_beacon_map = {
        "DE69F34B12FB": "Lvl 1 Fire Fighting Lobby",
        "D7EBDC5A92B9": "Lvl 1 Fire Fighting Lobby",
        "C43298D4E8B2": "Lvl 1 Fire Fighting Lobby",
        "F3B1B290486D": "Student Club",
        "D975F28047B3": "Foyer",
        "DB45ECD1DF33": "Foyer",
        "ECAC7EDCDF93": "LT2A Lobby",
        "D7BFA52AA899": "LT2A Lobby",
        "D249FA5CECA0": "LT2B Lobby",
        "FDC14F4F7ED4": "LT2B Lobby",
        "CC1DC599C10B": "LT2B Lobby",
        "D4A58BB6DCAD": "SR2A Lobby",
        "E0A4F1CBF31C": "SR2A Lobby",
        "CC2F5B7F9677": "SR2A Lobby",
        "DFBC60C04884": "SR2A Lobby",
        "E180324B7C78": "SR2A Lobby",
        "F5C3E08B32D5": "SR2A Lobby",
        "D48A42D20BE1": "Lvl 2 Lift Lobby",
        "C343BC7CCF92": "Lvl 2 Lift Lobby",
        "D1B4D89B73A7": "Lvl 4 Fire fighting Lobby",
        "EC4FB474B11C": "Lvl 4 Fire fighting Lobby",
        "F3514C561E0B": "SR4G Lobby",
        "D2622D4F854E": "SR4G Lobby",
        "CF1EBCE74C9C": "SR4G Lobby",
        "CCE3EFDACB52": "SR4A Lobby",
        "DA2D5CCB9488": "SR4G Lobby",
        "D470075FDA87": "SR4G Lobby",
        "DF037DD86E53": "SR4H Lobby",
        "CCF3E1C929FD": "SR4G Lobby",
        "E1EB15371D96": "SR4E Lobby",
        "F112F03A720D": "SR4G Lobby",
        "ED23CBDF8B80": "SR4G Lobby",
        "FA55EB6C23B4": "SR4A Lobby",
        "D20FB4E0B1D5": "SR4A Lobby",
        "C6D01D6A3FF4": "Lvl 4 Lift Lobby",
        "F4D13305DE3A": "Lvl 4 Lift Lobby",
        "D92C9A57F7CB": "SR5D Lobby",
        "FDF4813F84DB": "Lvl 5 Fire fighting Lobby",
        "EB3E5754BFBB": "SR5F Lobby",
        "DEE4570CB343": "SR5H Lobby",
        "F744E95AFEB4": "SR5D Lobby",
        "EED4DE089809": "SR5C Lobby",
        "F1E0D560AEFA": "Lvl 5 Lift Lobby",
        "E4AEB8791C91": "Lvl 5 Lift Lobby",
        "C53B43C6340A": "Lvl 5 Lift Lobby",
        "C153830706A5": "Lvl 5 Lift Lobby",
        "EF708283108E": "Lvl 5 Fire fighting Lobby",
        "FED95EF5D4C7": "Lvl 5 Fire fighting Lobby",
        "F1D6EC1553CD": "SR5F Lobby",
        "E7F82CE7B318": "SR5C Lobby",
        "DF69B5035B33": "Lvl 6 Fire fighting Lobby",
        "F3FBA538EC62": "Lvl 6 Fire fighting Lobby",
        "DA17557BCB38": "SR6A Lobby",
        "F85E688B4B72": "SR6B Lobby",
        "F28C771A175B": "SR6H Lobby",
        "E1A0FBAEA144": "Lvl 6 Fire fighting Lobby",
        "ECE7966F39E9": "SR6E Lobby",
        "C22D0D9E578C": "SR6H Lobby",
        "DF1D0A9FE1E0": "SR6G Lobby",
        "F40C85E05D70": "SR6H Lobby",
        "EEF85E5BDCED": "SR6A Lobby",
        "F68644A3A846": "SR6A Lobby",
        "C48190F6DE4A": "SR6H Lobby",
        "D17221428784": "SR6H Lobby",
        "DDA334403026": "SR6H Lobby",
        "C00123E26D45": "Lvl 6 Lift Lobby",
        "ECA9A0061008": "Lvl 6 Lift Lobby",
        "F798B9A7AC28": "ROOM 1",
        "EB89094E2F11": "ROOM 2",
        "DB6073C9C0A4": "ROOM 3",
        "F32ED305DB62": "ROOM 4",
        "C88FA9B10AE8": "ROOM 5",
        "EAC3938DDA2": "Level 7 Fire fighting Lobby",
        "D59761B61C6C": "Level 7 Fire fighting Lobby",
        "DB7ADA9F387B": "Level 7 Fire fighting Lobby",
        "CF8061AE8B38": "SR7B Lobby",
        "EF20D5A8BD8": "SR7B",
        "EB5F5BDD1443": "SR7C Lobby",
        "CA4C2D0DA8BD": "SR7C Lobby",
        "CBCE44CC874E": "SR7C",
        "E268B2A4AE9A": "SR7C Lobby",
        "CD5116F790EE": "SR7D Lobby",
        "EC5D57A6C8F3": "SR7D Lobby",
        "D6C01807A019": "SR7D",
        "F511F9E15121": "SR7D",
        "C4C4C1329EA2": "SR7D Lobby",
        "E466B99CB95F": "SR7D Lobby",
        "FB1868AB3E1B": "SR7E",
        "F2BA496C4BD1": "SR7E Lobby",
        "D319E655E91C": "SR7E Lobby",
        "EBFA572D1DC2": "MR 7A",
        "FDF33DAEE5A4": "MR 7A",
        'D11DC16A4F98': "MR 7A",   
        "C2BF4E1F0E2A": "Level 7 Lift Lobby",
        "C639BBBE3557": "Level 7 Lift Lobby",
        "DB0896A9CC33": "Level 7 Lift Lobby",
        "C2A628384B08": "Team 6 Beacon 1",
        "EB7376833609": "Team 6 Beacon 2",   
    }

    # retrieve beacon location based on mac address
    def get_location_details(self, beacon_address):
        collection = BeaconGateway.__BeaconCollection
        beacon = collection.find_one({"mac_address": beacon_address})
        beaconLocation = beacon["location"]
        beaconLevel = beacon["level"]
        return {
            "beaconLocation": str(beaconLocation),
            "beaconLevel": str(beaconLevel)
        }

