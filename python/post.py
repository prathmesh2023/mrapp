import requests
import json

URL = "http://127.0.0.1:8000/api/visit_create"

data = {
    'hospital_name': 'brainly',
    'doctor_name': 'challani',
    'latitude': '2.00',
    'longitude' : '1.21',
    'mr_username': 'lohar',
    'date' : '2022-03-04',
    'time': '14:12:05',
    'timestamp': '2022-03-04 14:10:19', 
    'ppt_path' : '/x.ppt'

}

json_data = json.dumps(data)

r = requests.post(url=URL, data=json_data)

data = r.json()

print(data)