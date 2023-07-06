# import requests

# # URL = "http://127.0.0.1:8000/api/testing"
# URL = "http://127.0.0.1:8000/api/mruser"

# headers = {'Authorization': 'Token 8e0a790b37547b23f82b2e6074b366bb9c2386fe'}

# r = requests.get(URL, headers=headers)

# data = r.json()

# print(data)


import requests

# URL = "http://127.0.0.1:8000/api/testing"
# URL = "https://mrappdoct.pythonanywhere.com/api/mrlogin/vaibhav/123"
URL = "http://44.202.235.223/api/testing"
headers = {'Authorization': 'Token c9a98edcd98c945259269321c1e73924b5e83998'}

r = requests.get(URL, headers=headers)

data = r.json()

print(data)
