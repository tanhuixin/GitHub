#import mysql.connector
import time
from datetime import datetime as dt
import paho.mqtt.client as mqtt
import json
from time import strftime
import pytz
import logging
import os
import schedule



PCS_Devices = [
    ["Name",	"MAC",	"Status"],
    ["T1-T238","A4:E5:7C:49:F4:80", "F"],
    ["T1-T233","A4:E5:7C:49:F5:04", "T"]
    ]
    counter = 0
print(counter)
import time
while True:
for i in PCS_Devices:
    for j in i:  
        print(j,end = " ")
    time.sleep(1)
     counter += 1
    print(counter)

if PCS_Devices[1][1] == "A4:E5:7C:49:F4:80":
    PCS_Devices[1][3] = PCS_Devices[1][3]+1
        

if PCS_Devices[2][1] == "A4:E5:7C:49:F5:04":
    PCS_Devices[2][3] = PCS_Devices[2][3]+1
    time.sleep(5)

#print(PCS_Devices.)