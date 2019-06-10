import json
from pymongo import MongoClient

with open("data-assetRoutes.json", 'r') as f:
    objs = json.load(f)

    client = MongoClient('10.20.4.30', 27017)
    db = client.sdcc
    for o in objs:
        db.AssetRoutes.insert_one(o)

print("fuck ")
