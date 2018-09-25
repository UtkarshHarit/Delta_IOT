import json
import requests
import re
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

while (True):
    t = open ("Temprature.csv",'a')
    l = open ("Light.csv",'a')
    h = open ("Humidity1.csv",'a')

    url_rec="https://api.thingspeak.com/channels/522645/feeds.json?results=2"
    resp=requests.get(url_rec)
    #print (resp.text)

    select = repr(resp.text)
    select = select[300:];

    pick = re.search('field1":"(.+?)",', select)
    pick2 = re.search('field2":"(.+?)",', select)
    pick3 = re.search('field3":"(.+?)"', select)

    if (pick):
        print ("Temprature recorded: "+pick.group(1))
        t.write(str(pick.group(1))+ '\n')
    if (pick2):
        print ("Light intensity recorded: "+pick2.group(1))
        l.write(str(pick2.group(1))+ '\n')
    if (pick3):
        print ("Humidity recorded: "+pick3.group(1))
        h.write(str(pick3.group(1))+ '\n')

    t.close()
    l.close()
    h.close()

    
    print("All done")
    time.sleep(10)
    

