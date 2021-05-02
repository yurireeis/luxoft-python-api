from pymongo import MongoClient


def mongo_is_healthy(db_url):
    client = MongoClient(db_url)
    return client.server_info()
