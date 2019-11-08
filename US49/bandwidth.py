
import base
import pymongo

# This is the <Bandwidth> class that will be used to find the total bandwidth usage across all OLT's within the network.

class Bandwidth:
    def __init__(self):
        self.sentName = "TX Total Octets"
        self.receivedName = "RX Total Octets"


# This function gathers all of the TX bandwidth (in octets) for each OLT and returns the list of values.

    def findAllTXBandwidth(self, collectionList, interval):
        interval = int(interval/5)
        baseObject = base.database()
        bandwidthUse = []
        for collectionString in collectionList:
            collection = baseObject.getCollection(collectionString)
            for _ in range(interval):
                print(collection)
                document = baseObject.getOneDocument(collection, self.sentName, None)
                print(list(document))
                pair = baseObject.findAllPairs(document, "")
                print(pair)
                value = pair[0][self.sentName]
                bandwidthUse.append({collection: value})
        return bandwidthUse


# This is the main function where the functionality is tested.

def main():
    print("main")
    bandwidthObejct = Bandwidth()
    collectionList = [""]
    TXBandwidth = bandwidthObejct.findAllTXBandwidth(collectionList, 5)
    print(TXBandwidth)


main()

# End of bandwidth.py
