from pymongo import MongoClient

class MongoDBClient:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MongoDBClient, cls).__new__(cls)
            cls._instance.client = MongoClient('mongodb://localhost:27017/')
            cls._instance.mongo_db = cls._instance.client['inventory_db']
        return cls._instance

    @property
    def collection(cls):
        return cls._instance.mongo_db['products']
