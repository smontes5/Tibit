import json

default = {
    "JSON": {
        "databaseDir": "database/", 
        "defaultDir": "database/"
    }, 
    "MongoDB": {
        "host": "127.0.0.1", 
        "name": "tibit_pon_controller", 
        "port": "27017"
    }, 
    "databaseType": "JSON", 
    "interface": "enp0s8.4090"
}

with open("PonCntlInit.json", "rt") as file:
	jsonData = json.load(file)

print("Testing reading from  PonCntlInit.json \n")

print("Current JSON path: " + str(jsonData["JSON"]["databaseDir"]) + "\n")

print("MongoDB Host server: " + str(jsonData["MongoDB"]["host"]) + "\n")
print("MongoDB Host name: " + str(jsonData["MongoDB"]["name"]) + "\n")
print("MongoDB Host port: " + str(jsonData["MongoDB"]["port"]) + "\n")

print("current database type: " + str(jsonData["databaseType"]) + "\n")
print("current interface: " + str(jsonData["interface"]) + "\n")

print("Resetting PonCntlInit.json \n")
with open("PonCntlInit.json", "w") as file:
	json.dump(default, file)
