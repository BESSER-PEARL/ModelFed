import requests

url = "http://127.0.0.1:8000/freddie/outbox"

# JSON activity definition
json_data = {
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Create",
  "id": "http://127.0.0.1:8000/freddie/activities/m1o2d3",
  "actor": "http://127.0.0.1:8000/freddie/",
  "to": ["http://127.0.0.1:8001/marie/"],
  "object": {
    "type": "DomainModel",
    "id": "http://127.0.0.1:8000/freddie/domainmodel/a1b2c3",
    "name": "MyModel",
    "summary": "This is a domain model.",
    "attributedTo": "http://127.0.0.1:8000/freddie/",
    "users": [
      "http://127.0.0.1:8000/freddie/",
      "http://127.0.0.1:8001/marie/"
    ]
  }
}

# Send the request
response = requests.post(url, json=json_data)
print(f"Status Code: {response.status_code}")
print(f"Response Body: {response.text}")