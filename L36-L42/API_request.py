

import requests
import json


# with open("record.json", "r") as file:
#     record = file.read()

# print(type(record))

# data = json.loads(record)

# print(type(data))

# print(data)


URL = 'https://jsonplaceholder.typicode.com/posts'

response = requests.get(URL)
assert response.ok


print(type(response.text))
# print(response.text)

data = json.loads(response.text)
print(type(data))

print(data[0])
