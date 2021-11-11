import requests
import json

exp = open('./data/expense.json')
exp_data = list(json.load(exp))

data = {
        "id": 1,
        "project_id": 2,
        "category_id": 2,
        "name": "Server Maintenance",
        "description": "Server maintenance and upgrading work to incorporate BC plans",
        "amount": 30000,
        "created_at": "2021-11-04T16:00:00.000Z",
        "created_by": "Jacky",
        "updated_at": "2021-11-06T16:00:00.000Z",
        "updated_by": "Jacky"
    }

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "exp/1", data)
print(response.json())