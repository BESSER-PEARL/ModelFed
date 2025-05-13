import json
import requests
import time
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description="Simulate model federation activities.")
parser.add_argument("--scenario", type=str, required=True, help="Scenario ID to use (e.g., 1 or 2)")
parser.add_argument("--data", type=str, default="activities.json", help="Path to data.json file")
parser.add_argument("--scenarios", type=str, default="scenarios.json", help="Path to scenarios.json file")
args = parser.parse_args()

# Load activity data
with open(args.data, "r", encoding="utf-8") as f:
    all_activities = json.load(f).get("activities", [])

# Load scenarios
with open(args.scenarios, "r", encoding="utf-8") as f:
    scenarios = json.load(f)

# Get selected scenario
activity_scenario = scenarios.get(args.scenario)
if not activity_scenario:
    print(f"Scenario {args.scenario} not found in {args.scenarios}")
    exit(1)

# Execute in the specified oscenario
for i in activity_scenario:
    if i < 0 or i >= len(all_activities):
        print(f"Invalid activity index: {i}. Skipping.")
        continue

    activity = all_activities[i]
    time.sleep(0.1)
    actor_url = activity.get("actor", "")
    if actor_url:
        if not actor_url.endswith("/"):
            actor_url += "/"

        output_url = actor_url.rstrip("/") + "/outbox/"

        try:
            response = requests.post(output_url, json=activity)
            print(f"POST to {output_url}")
            print(f"Status Code: {response.status_code}")
            print(f"Response Body: {response.text}\n")
        except requests.exceptions.RequestException as e:
            print(f"Failed to POST to {output_url}: {e}\n")
    else:
        print("Skipping activity with no actor URL.\n")

# Generate besser model code
url = "http://127.0.0.1:8000/generate_model"

json_data = {
  "model_id": "http://127.0.0.1:8000/admin/domainmodel/digital_product_passport",
  "file_path": "validation/exp_1_DPP_scenario/output_model/dpp_besser_model.py"
}

# Send the request
response = requests.post(url, json=json_data)
print(f"Status Code: {response.status_code}")
print(f"Response Body: {response.text}")