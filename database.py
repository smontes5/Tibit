# beginning of database.py

import pymongo


def main():

    #       Create the necessary Mongo object that is used to connect to the server. Then create the database, along
    # with the <networkUsage> collection that will be used to hold the network's usage data.

    mongoObject = pymongo.MongoClient("mongodb://127.0.0.1:27017")
    dataBase = mongoObject["network"]
    networkUsage = dataBase["networkUsage"]
    stats1 = {"network": 1, "usage": 90, "id": 1}
    stats2 = {"network": 1, "usage": 90, "id": 2}
    stats3 = {"network": 1, "usage": 50, "id": 3}
    stats4 = {"network": 1, "usage": 50, "id": 4}
    networkUsage.drop()


    #       Insert the documents into the collection and then call the calculateNetworkCongestion() function in order
    # to see if the combined network use is enough to trigger the print to the console.

    networkUsage.insert_one(stats1)
    networkUsage.insert_one(stats2)
    networkUsage.insert_one(stats3)
    networkUsage.insert_one(stats4)
    congested = calculateNetworkCongestion(networkUsage)
    location = None
    if congested:
        location = calculateBottleNeck(networkUsage)
    if location is not None:
        arrayOfValues = findValues(networkUsage, location)
        arrayOfNewValues = fixBottleNeck(arrayOfValues[0], arrayOfValues[1])
        updateDatabase(arrayOfNewValues, networkUsage)


def calculateNetworkCongestion(network):
    """ Calculate the average network usage from the MongoDB stats collection and print it to the console.

    :param network: This is the network collection in the MongoDB server.
    :return: True if the total network congestion is 70 or greater (70% or more).
    """

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


def calculateBottleNeck(network):
    """ This finds all of the network id's who "usage" data within the collection is over 70 (70%).

    :param network: This is the network collection in the MongoDB server.
    :return: A list of all the network id's that have "usage" over 70 (70%).
    """

    listOfStats = network.find({"network": 1})
    bottleNeckLocation = []
    for key in listOfStats:
        if int(key["usage"]) > 70:
            bottleNeckLocation.append(key["id"])
    printList(bottleNeckLocation)
    return bottleNeckLocation


def findValues(network, bottleneckLocation):
    """ Find the value of excess network usage (over 70%) and the amount of free resources (network usage below 70%)

    :param network: This is the network collection in the MongoDB server.
    :param bottleneckLocation: A list of network id's that have 70 (70%) or more network usage.
    :return: An array of two dictionaries, one which contains the excess network usage, and the other that contains
            the amount of free resources.
    """

    networkNeeded = {}
    freeNetworkLoad = {}
    count = 0
    listOfStats = network.find({"network": 1})
    for key in listOfStats:
        if key["usage"] < 70:
            freeNetworkLoad[key["id"]] = 70 - key["usage"]
    for key in bottleneckLocation:
        count += 1
        networkNeeded[key] = network.find_one({"id": key})["usage"] - 70
    array = [freeNetworkLoad, networkNeeded]
    return array


def fixBottleNeck(freeNetworkLoad, networkNeeded):
    """ Fix the bottlenecks of the network (as best as possible) by taking excess network usage on one id/node, and
    offloading to others with less usage.

    :param freeNetworkLoad: This is the dictionary of id's and the amount of excess network usage they have.
    :param networkNeeded: This is the dictionary of id's and the amount of needed network usage they have.
    :return: An array containing the updated freeNetworkLoad and networkNeeded dictionaries.
    """

    for free in freeNetworkLoad:
        for need in networkNeeded:
            tempNeed = networkNeeded[need] - freeNetworkLoad[free]
            tempFree = freeNetworkLoad[free] - networkNeeded[need]
            networkNeeded[need] = tempNeed
            freeNetworkLoad[free] = tempFree
            if int(freeNetworkLoad[free]) < 0:
                freeNetworkLoad[free] = 0
            if int(networkNeeded[need]) < 0:
                networkNeeded[need] = 0
    array = [freeNetworkLoad, networkNeeded]
    return array


def updateDatabase(array, collection):
    """ Update the collection with the new, calculated values.

    :param array: This is the array of updated values that are used for calculations when updating the collection.
    :param collection: This is the collection that will be updated.
    :return: None
    """

    for id in array[0]:
        collection.update_one({"id": id}, {"$set": {"usage": int(70 - array[0][id])}})

    for id in array[1]:
        collection.update_one({"id": id}, {"$set": {"usage": int(array[1][id] + 70)}})


def printList(list):
    """ Print the supplied list to the console.

    :param list: This is the list that will be printed.
    :return: None
    """

    for element in list:
        print("id is: "+str(element))


main()

