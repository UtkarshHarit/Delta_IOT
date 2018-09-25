import json
import requests
import re

t = open ("Temprature.txt",'a')
l = open ("Light.txt",'a')
h = open ("Humidity1.txt",'a')

url_rec="https://api.thingspeak.com/channels/522645/feeds.json?results=2"
resp=requests.get(url_rec)
print (resp.text)

select = repr(resp.text)
select = select[300:];

pick = re.search('field1":"(.+?)",', select)
pick2 = re.search('field2":"(.+?)",', select)
pick3 = re.search('field3":"(.+?)"', select)

if (pick):
    print (pick.group(1))
    t.write(str(pick.group(1))+ '\n')
if (pick2):
    print (pick2.group(1))
    l.write(str(pick2.group(1))+ '\n')
if (pick3):
    print (pick3.group(1))
    h.write(str(pick3.group(1))+ '\n')

t.close()
l.close()
h.close()


print("All done")

import running
