# Beginning of simulator.py

import random
import sys

import base


errorTypes = ["packet drop", "bandwidth spike", "error cascade"]


def main():

    baseObject = base.database()
    if sys.argv[1] == "-h":
        message = "Required command line arguments:\n"
        message += "<collectionName>    the name of the collection to fill with data\n"
        message += "Optional command line arguments:\n"
        message += "<errorType>         a specific error type that willS be created types are:\n"
        message += "                    packet drop, bandwidth spike, error cascade"
        message += "-h                  help\n"
        print(message)
        sys.exit(0)

    collectionName = ""
    errorType = None
    if len(sys.argv) == 3:
        collectionName = sys.argv[1]
        errorType = sys.argv[2]
    if len(sys.argv) == 2:
        collectionName = sys.argv[1]
    if len(sys.argv) == 1:
        print("Error enter the name of the collection you want to populate data with see -h for help")
        sys.exit(0)


    generateRandomFile(collectionName)


def randomValue(lowerBound, upperBound, type, decimalPoints):
    if type == "int":
        value = random.randint(lowerBound, upperBound)
    elif type == "double" or type == float:
        value = random.uniform(lowerBound, upperBound)
    return value

#   This is the beginning of the OLT generation that Arthur is doing in order to

def generateRandomFile(collectionName, errorType):
    print("Arthur task")
    if errorType is None:
        print("default")
        #defaultGeneration()
    elif errorType == "packet drop":
        print("packet drop")
        #packetDrop()
    elif errorType == "bandwidth spike":
        print("bandwidth spike")
        #bandwidthSpike()
    elif errorType == "error cascade":
        print("error cascade")
        #errorCascade()

main()