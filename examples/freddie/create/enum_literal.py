import requests

url = "http://127.0.0.1:8000/freddie/outbox"

# JSON activity definition
json_data = {
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Create",
  "id": "http://127.0.0.1:8000/freddie/activities/e10li30",
  "actor": "http://127.0.0.1:8000/freddie/",
  "to": ["http://127.0.0.1:8001/marie/"],
  "object": {
    "type": "EnumerationLiteral",
    "id": "http://127.0.0.1:8000/freddie/enumerationlits/e1l2i3",
    "name": "Private",
    "value": "2",
    "owner": "http://127.0.0.1:8000/freddie/enumerations/e1n2u3"
  },
  "target": "http://127.0.0.1:8000/freddie/domainmodel/a1b2c3"
}

# Send the request
response = requests.post(url, json=json_data)
print(f"Status Code: {response.status_code}")
print(f"Response Body: {response.text}")