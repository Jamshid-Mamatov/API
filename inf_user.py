import requests as requests

from pprint import pprint
import json 

response=requests.get('https://jsonplaceholder.typicode.com/users')

data=response.json()

main_infor={}


for user_data in data:

    main_infor[user_data['name']]={}

    name=user_data['name']
    email=user_data['email']
    city=user_data['address']['city']
    company_name=user_data['company']['name']

    main_infor[user_data['name']]['name']=name

    main_infor[user_data['name']]['email']=email

    main_infor[user_data['name']]['city']=city

    main_infor[user_data['name']]['company_name']=company_name


    




