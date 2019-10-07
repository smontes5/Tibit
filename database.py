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
    stats1 = {"network": 1, "usage": 90, "id": 1}
    stats2 = {"network": 1, "usage": 90, "id": 2}
    stats3 = {"network": 1, "usage": 60, "id": 3}
    stats4 = {"network": 1, "usage": 50, "id": 4}

    print("doing network usage")
    networkUsage.drop()


    #       Insert the documents into the collection and then call the calculateNetworkCongestion() function in order
    # to see if the combined network use is enough to trigger the print to the console.

    networkUsage.insert_one(stats1)
    networkUsage.insert_one(stats2)
    networkUsage.insert_one(stats3)
    networkUsage.insert_one(stats4)
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


#       Find which network (via their id's) who's usage statistics are above 70% and save them to a list

def calculateBottleNeck(network):
    print("inside function")
    listOfStats = network.find({"network": 1})
    bottleNeckLocation = []
    for key in listOfStats:
        if int(key["usage"]) > 70:
            print(str(key["usage"]))
            bottleNeckLocation.append(key["id"])
    printList(bottleNeckLocation)
    findValues(network, bottleNeckLocation)
    return bottleNeckLocation


#       This returns a dictionary of network values and the amount of free resources they have (below 70%) to give to
# other networks.

def findValues(network, bottleneckLocation):
    networkNeeded = {}
    freeNetworkLoad = {}
    count = 0
    listOfStats = network.find({"network": 1})
    for key in listOfStats:
        if key["usage"] < 70:
            freeNetworkLoad[count] = {key["id"]: 70 - key["usage"]}
            count += 1
    for key in bottleneckLocation:
        print(count)
        networkNeeded[count] = {key: network.find_one({"id": key})["usage"] - 70}
        count += 1
        print(network.find_one({"id": key})["usage"])
    print(networkNeeded)
    print(freeNetworkLoad)
    fixBottleNeck(freeNetworkLoad, networkNeeded)


#       Fix the bottleneck by assigning network usage to other network's

def fixBottleNeck(freeNetworkLoad, networkNeeded):
    print(networkNeeded)
    print(freeNetworkLoad)
    for free in freeNetworkLoad:
        for need in networkNeeded:
            print(need)
            print(free)
#            need["usage"] = need["usage"] - free["usage"]
 #           free = free["usage"] - need["usage"]
 #           if need["usage"] < 0:
 #               need["usage"] = 0
 #           if free["usage"] < 0:
 #               free["usage"] = 0



#       Print function to print a list

def printList(list):
    for element in list:
        print("id is: "+str(element))


main()

