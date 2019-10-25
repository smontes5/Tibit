import json

with open("pyjsontest.json", "rt") as file:
	jsonData = json.load(file)

print("Testing reading from file \n")
print("Retrieve string: " + jsonData["string"] + "\n")
print("Retrieve number: " + str(jsonData["number"]) + "\n")
print("Retrieve object: " + str(jsonData["object"])+ "\n")
print("Retrieve array: " + str(jsonData["array"]) + "\n")
print("Retrieve boolean: " + str(jsonData["boolean"]) + "\n")
print("Retrieve empty: " + str(jsonData["empty"]) + "\n")

print("Testing writing to file \n")

jsonData["string"] = "write test"
jsonData["number"] = 999
jsonData["object"] = { "object_int": 999, "object_string": "test write"}
jsonData["array"] = ["3" , "2" , "1"]
jsonData["boolean"] = False

with open("pyjsontest.json", "w") as file:
	json.dump(jsonData, file)


#print(jsonData)