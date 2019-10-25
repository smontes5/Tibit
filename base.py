# beginning of base.py

import pymongo


class database:

    def __init__(self):
        """ This initializes the mongo object and the database object.

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
            documents = collection.find(str({key + ": True"}))
            return documents
        document = collection.find_one(str({key +": " +value}))
        return document


    def getAllDocuments(self, collection, key, value):
        """ This returns the all documents within the collection that match the key value pair. If only a key is
        given then return all documents that contain that key.

        :param collection: This is the collection that the document is in.
        :param key: This is one of the keys in the document.
        :param value: This is the value of the key supplied in the parameter.
        :return: A list of the documents that contains the key value pair within the document.
        """

        if value is None:
            documents = collection.find(str({key + ": True"}))
            return documents
        documents = collection.find({key: value})
        return documents


    def findAllValues(self, documents, key):
        """ This returns all of the values of the specified key in the documents. If the key cannot be found in any of
        the documents, None is returned.

        :param documents: These are the documents that contain the specified key.
        :return: A list of the key value pairs of all of the documents or None if it is empty.
        """
        valueList = None
        for document in documents:
            valueList = document[key]
        return valueList


    def updateValues(self, documents, key, values):
        """ This updates all of the specified key value pairs within the specified documents.

        :param documents: This is the list of documents that will be updated.
        :param key: This is the list of keys whose values will be updated.
        :return:
        """

        # Will update this method and work on it more tomorrow.
        for document in documents:
            document.update({key: values})


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

    def shaping(self):
        shapeRate = self.getOLTData("Shape Rate")
        if shapeRate > 50:
            shapeRate = shapeRate -10
        shapeRate = {"Shape Rate": shapeRate}
        self.updateOLTData(shapeRate)
        return None