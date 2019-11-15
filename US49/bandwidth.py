
import base
import json
import pymongo
import re

# This is the <Bandwidth> class that will be used to find the total bandwidth usage across all OLT's within the network.

class Bandwidth:
    def __init__(self):
        self.sentName = "TX Total Octets"
        self.receivedName = "RX Total Octets"
        self.baseObject = base.database()


# This function gathers all of the bandwidth (in octets) for each OLT-NNI and return the list of values.

    def findAllPONBandwidth(self, collectionList, type, interval):
        interval = int(interval/5)
        bandwidthUse = []
        for collectionString in collectionList:
            collection = self.baseObject.getCollection(collectionString)
            for _ in range(interval):
                if type == "TX":
                    type = self.sentName
                elif type == "RX":
                    type = self.receivedName
                value = self.baseObject.getOLTStat(collection, "OLT-PON", "OLT-PON", type)
                bandwidthUse.append({collectionString: value})
        return bandwidthUse


# This function gathers all of the bandwidth (in octets) for each OLT-PON and return the list of values.

    def findAllNNIBandwidth(self, collectionList, type, interval):
        interval = int(interval/5)
        baseObject = base.database()
        bandwidthUse = []
        for collectionString in collectionList:
            collection = baseObject.getCollection(collectionString)
            for _ in range(interval):
                Unicast = baseObject.getOLTStat(collection, "OLT-NNI", "OLT-NNI", type +" Multicast Octets")
                Multicast = baseObject.getOLTStat(collection, "OLT-NNI", "OLT-NNI", type + " Unicast Octets")
                Broadcast = baseObject.getOLTStat(collection, "OLT-NNI", "OLT-NNI", type + " Broadcast Octets")
                value = Unicast + Multicast + Broadcast
                bandwidthUse.append({collectionString: value})
        return bandwidthUse


    def merge(self, elements):
        if len(elements) <= 1:
            return elements
        halfway = int(len(elements)/2)
        length = int(len(elements))
        list1 = elements[0:halfway]
        list2 = elements[halfway:length]
        #print(list1)
        #print(list2)
        list1 = self.merge(list1)
        list2 = self.merge(list2)
        #print("final sort "+ str(list1))
        #print("final sort " + str(list2))
        finalList = self.sort(list1, list2)
        #print(finalList)
        return finalList

    def sort(self, list1, list2):
        total = list1 + list2
        max = len(total)
        finalList = []
        counter1 = 0
        counter2 = 0
        for _ in range(max):
            if counter1 >= len(list1):
                finalList.append(list2[counter2])
                counter2 += 1
                continue
            if counter2 >= len(list2):
                finalList.append(list1[counter1])
                counter1 += 1
                continue
            if list(list1[counter1].values()) >= list(list2[counter2].values()):
                finalList.append(list1[counter1])
                counter1 += 1
            else:
                finalList.append(list2[counter2])
                counter2 += 1

        return finalList


# This function ports the supplied data to a JSON file with the name "Bandwidth".
    def portToJSON(self, data):
        print(data)
        bandwidth = {}
        with open("Bandwidth.json", "w") as file:
            for element in data:
                key = str(list(element.keys()))
                key = re.sub("\[", "", key)
                key = re.sub("]", "", key)
                value = str(list(element.values()))
                value = re.sub("\[", "", value)
                value = re.sub("]", "", value)
                bandwidth[key] = value
            json.dump(bandwidth, file)


# This function ports the supplied data to a MongoDB collection with the name "Bandwidth".
    def portToMongoDB(self, data):
        collection = self.baseObject.database["Bandwidth"]
        collection.insert_one({"test": "1"})
        for element in data:
            key = str(list(element.keys()))
            key = re.sub("\[", "", key)
            key = re.sub("]", "", key)
            value = str(list(element.values()))
            value = re.sub("\[", "", value)
            value = re.sub("]", "", value)
            bandwidth = {key: value}
            collection.insert_one(bandwidth)


# This is the main function where the functionality is tested.

def main():
    print("main")
    bandwidthObejct = Bandwidth()
    collectionList = ["STATS-OLT-70b3d5523156", "STATS-OLT-70b3d552349c", "STATS-OLT-70b3d55235ca",
                      "STATS-OLT-70b3d552360c"]
    TXBandwidthPON = bandwidthObejct.findAllPONBandwidth(collectionList, "TX", 5)
    RXBandwidthPON = bandwidthObejct.findAllPONBandwidth(collectionList, "RX", 5)
    TXBandwidthNNI = bandwidthObejct.findAllNNIBandwidth(collectionList, "RX", 5)
    #print(TXBandwidthPON)
    #print(RXBandwidthPON)
    print(TXBandwidthNNI)
    data = bandwidthObejct.merge(TXBandwidthNNI)
    bandwidthObejct.portToJSON(data)
    bandwidthObejct.portToMongoDB(data)
    #print(TXBandwidth)



main()

# End of bandwidth.py
