import requests
import json

acc = open('./data/user.json')
acc_data = list(json.load(acc))

BASE = "http://127.0.0.1:5000/"

# create db for acc
for i in acc_data:
    keys = ("username","password","name","appointment")
    data = dict([(key,i[key]) for key in keys])
    response = requests.put(BASE + "acc/" + str(i["id"]), data)
    print(response)

# test get function
response = requests.get(BASE + "acc/1")
print(response.json())


