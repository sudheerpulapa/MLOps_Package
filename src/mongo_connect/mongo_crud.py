from pymongo import MongoClient
import logging

logger = logging.getLogger(__name__)

class MongoDB:
    def __init__(self, uri, database_name):
        self.client = MongoClient(uri)
        self.db = self.client[database_name]
        logger.info(f"Connected to MongoDB database: {database_name}")

    def insert_one(self, collection_name, document):
        collection = self.db[collection_name]
        result = collection.insert_one(document)
        logger.info(f"Inserted document into {collection_name}: {result.inserted_id}")
        return result.inserted_id

    def find(self, collection_name, query):
        collection = self.db[collection_name]
        documents = collection.find(query)
        logger.info(f"Found documents in {collection_name}: {documents}")
        return list(documents)

    def update_one(self, collection_name, query, update):
        collection = self.db[collection_name]
        result = collection.update_one(query, update)
        logger.info(f"Updated document in {collection_name}: {result.modified_count} modified")
        return result.modified_count

    def delete_one(self, collection_name, query):
        collection = self.db[collection_name]
        result = collection.delete_one(query)
        logger.info(f"Deleted document from {collection_name}: {result.deleted_count} deleted")
        return result.deleted_count
