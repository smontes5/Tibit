# beginning of OLT.py

import pymongo

class OLT:

    def getOLTData(self, specificData):
        dataBase = self.database
        collection = dataBase.self.collection
        OLTdata = collection.find(specficData)
        return OLTData

    def updateOLTData(self, specificData):
        dataBase = self.database
        collection = dataBase.self.collection
        OLTdata = collection.update(specificData)
        return None

    def shaping(self):
        shapeRate = getOLTData("Shape Rate")
        if shapeRate > 50
            shapeRate = shapeRate -10
        shapeRate = {"Shape Rate": shapeRate}
        updateOLTData(shapeRate)
        return None