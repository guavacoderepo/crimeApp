from pymongo import MongoClient

mongourl = "mongodb+srv://guava:guava@cluster0.ukn1jcw.mongodb.net/?retryWrites=true&w=majority"


try:
    mongodb = MongoClient(mongourl).crimeApp
    print("connection successful...")
except:
    print("Connection error...")
    pass


def insert_item(data):
    return mongodb.newsData.insert_one(data)

def fetch_all():
    return mongodb.newsData.find()

def update_item():
    pass

def delete_item():
    pass


def find_item():
    pass


d = fetch_all()

print([n for n in d])