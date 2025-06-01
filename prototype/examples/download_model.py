import requests

url = "http://127.0.0.1:8001/generate_model"

# JSON activity definition
json_data = {
  "model_id": "http://127.0.0.1:8000/userA/domainmodel/a1b2c3",
  "file_path": "model_test/example_model.py"
}

# Send the request
response = requests.post(url, json=json_data)
print(f"Status Code: {response.status_code}")
print(f"Response Body: {response.text}")