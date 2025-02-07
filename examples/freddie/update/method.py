import requests

url = "http://127.0.0.1:8000/freddie/outbox"

# JSON activity definition
json_data = {
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Update",
  "id": "http://127.0.0.1:8000/freddie/activities/m4c6o8",
  "actor": "http://127.0.0.1:8000/freddie/",
  "to": ["http://127.0.0.1:8001/marie/"],
  "object": {
    "type": "Method",
    "id": "http://127.0.0.1:8000/freddie/methods/m7e8t9",
    "name": "new_average",
    "owner": "http://127.0.0.1:8000/freddie/classes/a1b2c3",
    "parameters": ["http://127.0.0.1:8000/freddie/parameters/p7a8r9"]
  },
  "target": "http://127.0.0.1:8000/freddie/domainmodel/a1b2c3"
}

# Send the request
response = requests.post(url, json=json_data)
print(f"Status Code: {response.status_code}")
print(f"Response Body: {response.text}")