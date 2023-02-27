from pymongo import MongoClient


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    # class constructor
    def __init__(self, username="afshin", password="password1", auth_db="admin", port=27017):
        # Initializing the MongoClient.
        try:
            self.client = MongoClient(f"mongodb://{username}:{password}@localhost:{port}/?authMechanism=DEFAULT&authSource={auth_db}")
            self.database = self.client["AAC"]
            self.animals_collection = self.database["animals"]
        except():
            print("Could not connect to MongoDB.")

    # C in CRUD. Create a document from the given dictionary.
    def create(self, data):
        if data is not None:
            self.animals_collection.insert_one(data)  # data should be dictionary
            return True
        else:
            return False
            raise Exception("Nothing to save, because data parameter is empty")

    # R in CRUD. Reads all documents that match the given query.
    def read(self, query):
        # Note: the _id values are not serializable and create an error when attempting to display them in a dash_table.DataTable
        # component. Since it is not valuable info for display, we exclude it from the query.
        cursor = self.animals_collection.find(query, {'_id': 0})
        # cursor is iterable
        return cursor

    # U in CRUD. Update the first document that matches the search query with the given fields
    def update(self, query, data):
        # this operator adds a field and value to a document if the field doesn't already exist.
        # Otherwise, it replaces the value of the field.
        result = self.animals_collection.update_one(query, {"$set": data})
        return result

    # D in CRUD. Remove the first document that matches the search query
    def delete(self, data):
        result = self.animals_collection.delete_one(data)
        return result
