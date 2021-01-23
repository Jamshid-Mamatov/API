import requests as requests

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

    



