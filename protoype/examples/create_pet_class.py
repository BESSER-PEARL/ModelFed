import requests

url = "http://127.0.0.1:8000/userA/outbox"

# JSON activity definition
json_data = {
  "@context": [
    "https://www.w3.org/ns/activitystreams",
    "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
  ],
  "type": "Create",
  "id": "http://127.0.0.1:8000/userA/activities/c1l2s3",
  "actor": "http://127.0.0.1:8000/userA/",
  "to": ["http://127.0.0.1:8001/userB/"],
  "object": {
    "type": "Class",
    "id": "http://127.0.0.1:8000/userA/classes/a1b2c3",
    "name": "Pet"
  },
  "target": "http://127.0.0.1:8000/userA/domainmodel/a1b2c3",
  "timestamp": "2025-05-11T15:31:45Z"
}

# Send the request
response = requests.post(url, json=json_data)
print(f"Status Code: {response.status_code}")
print(f"Response Body: {response.text}")