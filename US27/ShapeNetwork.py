import json

with open("PonCntlInit.json", "rt") as file:
	jsonData = json.load(file)

print("Testing reading from  PonCntlInit.json \n")

print("Current JSON path: " + str(jsonData["JSON"]["databaseDir"]) + "\n")

print("MongoDB Host server: " + str(jsonData["MongoDB"]["host"]) + "\n")
print("MongoDB Host name: " + str(jsonData["MongoDB"]["name"]) + "\n")
print("MongoDB Host port: " + str(jsonData["MongoDB"]["port"]) + "\n")

print("current database type: " + str(jsonData["databaseType"]) + "\n")
print("current interface: " + str(jsonData["interface"]) + "\n")
