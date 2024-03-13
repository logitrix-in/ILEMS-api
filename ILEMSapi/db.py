from pymongo import MongoClient

client = MongoClient("mongodb://mongo:vnFnRKqLuaPREHpGjLdYWnjCQjOAvwFY@roundhouse.proxy.rlwy.net:24947")

DB = client["db-ilems"]