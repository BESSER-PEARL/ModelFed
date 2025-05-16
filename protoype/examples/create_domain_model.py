import requests

url = "http://127.0.0.1:8000/userA/outbox"

# JSON activity definition
json_data = {
  "@context": [
    "https://www.w3.org/ns/activitystreams",
    "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
  ],
  "type": "Create",
  "id": "http://127.0.0.1:8000/userA/activities/m1o2d3",
  "actor": "http://127.0.0.1:8000/userA/",
  "to": ["http://127.0.0.1:8001/userB/"],
  "object": {
    "type": "DomainModel",
    "id": "http://127.0.0.1:8000/userA/domainmodel/a1b2c3",
    "name": "MyModel"
  },
  "timestamp": "2025-05-11T15:30:45Z"
}

# Headers required for ModelFed
headers = {
    "Content-Type": "application/ld+json",  # or "application/activity+json"
    "Accept": "application/ld+json"
}

# Send the request
response = requests.post(
    url,
    json=json_data,
    headers=headers
)

print(f"Status Code: {response.status_code}")
print(f"Response Body: {response.text}")