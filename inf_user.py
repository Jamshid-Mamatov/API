import requests as requests

from pprint import pprint
import json 

response=requests.get('https://jsonplaceholder.typicode.com/users')

data=response.json()

main_infor={}


for user_data in data:

    main_infor[user_data['id']]=[]

    name=user_data['name']
    email=user_data['email']
    city=user_data['address']['city']
    company_name=user_data['company']['name']

    main_infor[user_data['id']].append(name)

    main_infor[user_data['id']].append(email)

    main_infor[user_data['id']].append(city)

    main_infor[user_data['id']].append(company_name)

pprint(main_infor)
    




