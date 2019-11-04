import random
import sys
import json

#   This is the beginning of the OLT generation that Arthur is doing.
print("Enter number representing which type of file you want to generate \n");
print("1 Normal operation 2 Overperforming 3 Moderate errors 4 Complete Random \n");

# sys.argv[1]

def generateRandomFile(collectionName, errorType):
    print("Arthur task")
    if errorType == 1:
        print("default")
        generateNormal()
    elif errorType == 2:
        print("completely random")
        generateOverperforming()
    elif errorType == 3:
        print("overperforming")
        generateModErr()
    elif errorType == 4:
        print("Complete random")
        generateRandom()
		
def generateNormal():
	print("Generating a normal OLT")
	
	with open("SimTemplate.json", "rt") as file:
		jsonData = json.load(file)
	
	jsonData["OLT-TEMP"]["LASER"] = random.randint(43,50)
	jsonData["OLT-TEMP"]["XCVR"] = random.randint(60,65)
	jsonData["OLT-TEMP"]["ASIC"] = random.randint(60,65)
	
	with open("SimulationOutput.json", "w") as file:
		json.dump(jsonData, file)
	
	print("Generation finished and will be found in SimulationOutput.json ")
	
def generateOverperforming():
	print("Generating an overperforming OLT")
	
	with open("SimTemplate.json", "rt") as file:
		jsonData = json.load(file)
	
	jsonData["OLT-TEMP"]["LASER"] = random.randint(38,43)
	jsonData["OLT-TEMP"]["XCVR"] = random.randint(55,59)
	jsonData["OLT-TEMP"]["ASIC"] = random.randint(55,59)
	
	with open("SimulationOutput.json", "w") as file:
		json.dump(jsonData, file)

def generateModErr():
	print("Generating a moderately underperforming OLT")
	
	with open("SimTemplate.json", "rt") as file:
		jsonData = json.load(file)
	
	jsonData["OLT-TEMP"]["LASER"] = random.randint(50,55)
	jsonData["OLT-TEMP"]["XCVR"] = random.randint(65,70)
	jsonData["OLT-TEMP"]["ASIC"] = random.randint(65,70)
	
	with open("SimulationOutput.json", "w") as file:
		json.dump(jsonData, file)

def generateRandom():
	print("Generating complete random OLT data (probably wont make sense)")
	
	with open("SimTemplate.json", "rt") as file:
		jsonData = json.load(file)
	
	jsonData["OLT-TEMP"]["LASER"] = random.randint(0,1000)
	jsonData["OLT-TEMP"]["XCVR"] = random.randint(0,1000)
	jsonData["OLT-TEMP"]["ASIC"] = random.randint(0,1000)
	
	with open("SimulationOutput.json", "w") as file:
		json.dump(jsonData, file)
		
generateNormal()