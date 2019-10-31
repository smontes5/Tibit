# Beginning of simulator.py

import base
import random
import sys

def main():


    baseObject = base.database()

    if sys.argv == "-h":
        message = "Required command line arguments:\n"
        message += "<collectionName>    the name of the collection to fill with data\n"
        message += "Optional command line arguments:\n"
        message += "<documentName>      name of a specific document to fill with data\n"
        message += "-a                  fill all necessary data points\n"
        message += "-h      help\n"





def randomValue(lowerBound, upperBound, type, decimalPoints):
    if type == "int":
        value = random.randint(lowerBound, upperBound)
    elif type == "double" or type == float:
        value = random.uniform(lowerBound, upperBound)
    return value

