import requests
import json

pro = open('./data/project.json')
pro_data = list(json.load(pro))

BASE = "http://127.0.0.1:5000/"

for i in pro_data:
   keys = ("user_id", "name", "budget", "description")
   data = dict([(key,i[key]) for key in keys])
   response = requests.put(BASE + "pro/" + str(i["id"]), data)
   print(response.json())


response = requests.get(BASE + "pro/1")
print(response.json())

response = requests.patch(BASE + "pro/1", {"name":'RTF'})
print(response.json())

response = requests.get(BASE + "pro/1")
print(response.json())