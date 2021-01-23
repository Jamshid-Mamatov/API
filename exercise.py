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

        person={}
        if gender=='male' and x!=5:
            x+=1
            person[name]=city
            information['males'].append(person)   
            
        elif gender=='female' and y!=5 :
            y+=1
            person[name]=city
            information['females'].append(person)


f=open('main.txt','w')
f.write(str(information))


