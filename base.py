# beginning of base.py

import pymongo
import copy


class database:

    def __init__(self):
        """ This initializes the Mongo object and the database object.

        """
        self.mongoObject = pymongo.MongoClient("mongodb://127.0.0.1:27017")
        self.database = self.mongoObject["tibit_pon_controller"]


    def getCollection(self, collectionName):
        """ This returns the collection that is queried by the user

        :param collectionName: This is the name of the collection required.
        :return: Collection that has the specified <collectionName>.
        """

        collection = self.database[collectionName]
        return collection


    def getOneDocument(self, collection, key, value):
        """ This returns the first found document within the collection that matches the key value pair. If only the key
        is given then return all of the documents that contain that key.

        :param collection: This is the collection that the document is in.
        :param key: This is one of the keys in the document.
        :param value: This is the value of the key supplied in the parameter.
        :return: Document that contains the key value pair within the document or just the key pair if that is all that
                is given.
        """

        if value is None:
            documents = collection.find({key: "True"})
            return documents
        document = collection.find_one({key: value})
        return document


    def getAllDocuments(self, collection, key, value):
        """ This returns the all documents within the collection that match the key value pair. If only a key is
        given then return all documents that contain that key.
        Reference for $exists: True query operator: https://docs.mongodb.com/manual/reference/operator/query/exists/
        at line 59.

        :param collection: This is the collection that the document is in.
        :param key: This is one of the keys in the document.
        :param value: This is the value of the key supplied in the parameter.
        :return: A list of the documents that contains the key value pair within the document.
        """

        if value is None:
            documents = collection.find({key: {"$exists": "True"}})
            return documents
        documents = collection.find({key: value})
        return documents


    def findAllPairs(self, documents, key):
        """ This returns all of the key values of the specified keys in the documents. If the key cannot be found in any
        of the documents, None is returned.

        :param documents: These are the documents that contain the specified key.
        :return: A list of the key value pairs of all of the documents or None if it is empty.
        """
        valueList = []
        for document in documents:
                temparray = {key: document[key]}
                valueList.append(temparray)
        return valueList


    def updateValues(self, collection, originalElements, newElements):
        """ This updates all of the specified key value pairs within the specified collections.

        :param collection: This is the collection of documents that will be updated.
        :param newElements: This is the list of elements whose values will be sent to the
        :return: None
        """

        for originalElement, newElement in zip(originalElements, newElements):
            collection.update_one(originalElement, {"$set": newElement})
        return None


    def deleteObjects(self, collection, elements):
        """ This function deletes either the collections specified (if <elements> param is not specified) or all of the
        key value pairs in the collections if the <elements> param is given.

        :param collection: This is the collection that will be deleted or the list of key value pairs that
                            will be deleted.
        :param elements: This is the list of key value pairs that will be deleted.
        :return: None
        """

        if elements is None:
            collection.dump()
        print(elements)
        collection.delete_many(elements)


    def changedatabase(self, databaseName):
        """ This changes the database to the new database as specified by <databaseName>.

        :param databaseName: This is the name of the database that will be used within the class.
        :return: None
        """

        self.database = self.mongoObject(databaseName)


class OLT:

    def getOLTData(self, specificData):
        dataBase = self.database
        collection = dataBase.self.collection
        OLTdata = collection.find(specificData)
        return self.OLTData

    def updateOLTData(self, specificData):
        dataBase = self.database
        collection = dataBase.self.collection
        OLTdata = collection.update(specificData)
        return None


def main():
    """ This is the main function that tests the functionality of the database class.

    :return: None
    """
    db = database()
    collection = db.getCollection("")
    print(collection)
    documents = db.getOneDocument(collection, "Time", "2019-10-23 23:51:28.097540")
    print(documents)
    documents = db.getAllDocuments(collection, "Time", None)
    print(documents)
    listOfValues = db.findAllPairs(documents, "Time")
    listOfNewValues = copy.deepcopy(listOfValues)
    listOfNewValues[0]["Time"] = 10
    print(listOfValues)
    print(listOfNewValues)
    print(listOfValues)
    db.updateValues(collection, listOfValues, listOfNewValues)
    print(listOfValues)
    db.deleteObjects(collection, {"Time": 10})


#main()