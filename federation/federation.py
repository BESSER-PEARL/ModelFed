import requests
import json
import threading
from fastapi.encoders import jsonable_encoder

def send_activity(url: str, activity_data: dict):
    """Send the activity to a remote inbox asynchronously."""
    url = url.rstrip('/') + '/inbox/' if not url.endswith('/inbox/') else url

    try:
        response = requests.post(
            url,
            json=activity_data,
            headers={"Content-Type": "application/ld+json"}
        )
        response.raise_for_status()
        print(f"✅ Activity successfully federated to {url}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to federate activity to {url}: {str(e)}")

def federate_activity(activity_data: dict):
    """Federates an activity in a separate thread."""
    #activity_data = jsonable_encoder(activity)
    to_urls = activity_data.get("to", [])

    if not to_urls:
        print("⚠ No recipients to federate the activity.")
        return

    # Start a new thread to handle federation without blocking main execution
    def async_federate():
        for url in to_urls:
            threading.Thread(target=send_activity, args=(url, activity_data), daemon=True).start()

    threading.Thread(target=async_federate, daemon=True).start()
