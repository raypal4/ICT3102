import pymongo
from pymongo import ssl_support
import os

class Database:
    client = pymongo.MongoClient(os.environ["MONGOSCONNECTIONSTRING"])
    db = client["ICT3102"]