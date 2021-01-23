import requests as r

import json

x=0
y=0

information={}
information['males']=[]
information['females']=[]

while x!=5 or y!=5 :

    response=r.get("https://randomuser.me/api/")
    