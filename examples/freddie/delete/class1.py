import requests

url = "http://127.0.0.1:8000/freddie/outbox"

# JSON activity definition
json_data = {
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Delete",
  "id": "http://127.0.0.1:8000/freddie/activities/de2b2c210",
  "actor": "http://127.0.0.1:8000/freddie/",
  "to": ["http://127.0.0.1:8001/marie/"],
  "object": {
    "type": "Class",
    "id": "http://127.0.0.1:8000/freddie/classes/a1b2c3"
  },
  "target": "http://127.0.0.1:8000/freddie/domainmodel/a1b2c3"
}

# Send the request
response = requests.post(url, json=json_data)
print(f"Status Code: {response.status_code}")
print(f"Response Body: {response.text}")
