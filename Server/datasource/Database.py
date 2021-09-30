import pymongo
from pymongo import ssl_support

class Database:
    client = pymongo.MongoClient(
        "mongodb+srv://ray:password1234@cluster0.xhxln.mongodb.net/ICT3102?retryWrites=true&w=majority", ssl_cert_reqs=ssl_support.CERT_NONE)
    db = client["ICT3102"]