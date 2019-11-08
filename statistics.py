import json
import datetime
from datetime import timedelta
from dateutil.parser import parse

"""
Find and print the error rate in bytes with input of errored bits, good bits, and time in seconds 
"""
def calcErrorRate(bbits, gbits, time):
	tbits = bbits + gbits
	bbytes = bbits/8
	gbytes = gbits/8
	tbytes = tbits/8
	errorRate = bbytes/tbytes
	
	print("Error rate is " + str(errorRate) + " calculated over " + str(time) + " seconds.")
"""
Find the time elapsed in seconds where s2 is the json data of the later time stamp olt and s1 is the earlier
"""	
def timeElapsedSeconds(s1, s2):
	#t1 = datetime.datetime.strptime(s1["Time"], '%Y-%m-%d %H:%M:%S.%f')
	#t2 = datetime.datetime.strptime(s2["Time"], '%Y-%m-%d %H:%M:%S.%f')
	t1 = parse(s1["Time"])
	t2 = parse(s2["Time"])
	elapsed = (t2-t1).total_seconds()
	#es = elapsed.seconds
	return elapsed
"""
Display the error statistics of a time stamp d
"""
def displayErrorStats(d):
	s1 = d["OLT-PON"]["RX FEC Uncorrectable Blocks"]
	s2 = d["OLT-PON"]["RX Errored BIP Bits"]
	s3 = d["OLT-PON"]["RX Errored BIP Blocks"]
	s4 = d["OLT-PON"]["RX HEC Errors"]
	
	print("Received FEC uncorrectable blocks " + str(s1))
	print("Received Errored BIP Bits " + str(s2))
	print("Received Errored BIP Blocks " + str(s3))
	print("Received HEC Errors " + str(s4))
"""
From OLT 70b3d5523156
"""
with open("OLT-stamp1.json", "rt") as file:
	stamp1 = json.load(file)

with open("OLT-stamp2.json", "rt") as file:
	stamp2 = json.load(file)
a = 1
b = 1
t = timeElapsedSeconds(stamp1, stamp2)	
calcErrorRate(a, b, t)
print("Displaying error stats for time stamp 2 ")
displayErrorStats(stamp2)


