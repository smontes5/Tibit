# beginning of database.py

import pymongo
import math

def main():

    #       Create the necessary mongo object that is used to connect to the server. Then create the database, along
    # with the <networkUsage> collection that will be used to hold the network's usage data.

    mongoObject = pymongo.MongoClient("mongodb://127.0.0.1:27017")
    dataBase = mongoObject["network"]
    networkUsage = dataBase["networkUsage"]
    print("test")
    stats1 = {"network": 1, "usage": 70, "id": 1}
    stats2 = {"network": 1, "usage": 90, "id": 2}
    print("doing network usage")

    #       Insert the documents into the collection and then call the calculateNetworkCongestion() function in order
    # to see if the combined network use is enough to trigger the print to the console.

    networkUsage.insert_one(stats1)
    networkUsage.insert_one(stats2)
    congested = calculateNetworkCongestion(networkUsage)
    if congested:
        calculateBottleNeck(networkUsage)
    networkUsage.drop()


#   Calculate the average network usage from the mongoDB stats collection and print it to the console.

def calculateNetworkCongestion(network):
    print("in function")
    print(network)
    listOfStats = network.find({"network": 1})
    total = 0
    counter = 0
    for key in listOfStats:
        total += int(key["usage"])
        counter += 1
    congestion = total/counter
    if congestion >= 70:
        print("congestion is high "+str(congestion))
        return True
    else:
        return False


#       Find which network (via their id's) who's usage statistics are at or above 70% and save them to a list

def calculateBottleNeck(network):

    print("inside function")
    listOfStats = network.find({"network": 1})
    bottlenNeckLocation = []
    for key in listOfStats:
        if int(key["usage"]) >= 70:
            print(str(key["usage"]))
            bottlenNeckLocation.append(key["id"])
    printList(network,bottlenNeckLocation)
    return bottlenNeckLocation

#       Fix the bottleneck by assigning network usage to other network's (via their id's)

#       This code will need to be used to find all of the differences in the network usage that is below 70%, so that
# other netowrks can offload to it. Doing this will spread the load of the network out more.
def fixBottleNeck(network, bottleneckLocation):
    networkId = []
    networkLoad = {}
    #for id in bottleneckLocation:


#       Print function to print a list

def printList(list):
    for element in list:
        print("id is: "+str(element))


main()

