from pymongo import MongoClient


mongourl = "mongodb+srv://crimeapp:crimeapp@crimeapp.r6hqoud.mongodb.net/?retryWrites=true&w=majority"

try:
    mongodb = MongoClient(mongourl).crimeApp
    print("connection successful...")
except:
    print("Connection error...")
    pass



def insert_item(data):
    return mongodb.crimenews.insert_one(data)

def fetch_all():
    return mongodb.crimenews.find()

def update_item():
    pass

def delete_item():
    pass


def find_item():
    pass
