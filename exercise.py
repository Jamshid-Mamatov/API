import requests as r

import json

x=0
y=0

information={}
information['males']=[]
information['females']=[]

while x!=5 or y!=5 :

    response=r.get("https://randomuser.me/api/")

    if response.status_code==200:
        data=response.json()

        gender=data['results'][0]['gender']
        name=data['results'][0]['name']['first']
        city=data['results'][0]['location']['city']
