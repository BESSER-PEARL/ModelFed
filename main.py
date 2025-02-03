import os
import uvicorn
import requests
import logging
import subprocess
from fastapi.encoders import jsonable_encoder
from models import Activity, Object
from besser.BUML.metamodel.structural import *
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse, PlainTextResponse
from fastapi.templating import Jinja2Templates
from activities import create, update_class
from federation import federate_activity
from storage import get_model, get_domain_models, get_inbox, get_outbox, save_outbox_activity, save_inbox_activity
from models.modelverse import *
from besser.utilities import domain_model_to_code

# debug
logging.basicConfig(level=logging.DEBUG)

app = FastAPI()

# templates
templates = Jinja2Templates(directory="templates")

# Execute the activity in the current server
def process_activity(activity: Activity):
    if activity.type == "Create":
        if activity.object["type"] == "DomainModel":
            create(activity.object)
        
        if activity.object["type"] == "Class":
            create(activity.object)

        if activity.object["type"] == "Property":
            create(activity.object)
        
        if activity.object["type"] == "BinaryAssociation":
            create(activity.object)

        if activity.object["type"] == "Generalization":
            create(activity.object)

        if activity.object["type"] == "Method":
            create(activity.object)

        if activity.object["type"] == "Parameter":
            create(activity.object)

        if activity.object["type"] == "Package":
            create(activity.object)

        if activity.object["type"] == "Enumeration":
            create(activity.object)

        return {"status": "success", "message": "Object created successfully."}

    if activity.type == "Update":
        pass
        #update_class(activity.object, model_classes[activity.object["id"]])
        #return {"status": "success", "message": "Class updated successfully."}

    return {"status": "success", "message": "Unprocessed activity."}

@app.post("/{username}/outbox")
async def post_user_outbox(request: Request, username: str):
    try:
        # Parse the request to JSON
        activity_data = await request.json()

        # Convert JSON data to an Activity object
        activity = Activity(**activity_data)

        # Process the activity
        response = process_activity(activity)

        # Add the activity to the user outbox
        save_outbox_activity(username, activity_data)

        # Activity federation if it has recipients
        #if activity.to:
        #    federate_activity(activity)

        return response
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid activity format: {str(e)}") from e

@app.get("/{username}/activities")
async def get_user_outbox(username: str, request: Request):
    #outbox = user_outbox[username] if username in user_outbox else {}
    outbox = get_outbox(username)
    #inbox = user_inbox[username] if username in user_inbox else {}
    inbox = get_inbox(username)
    return templates.TemplateResponse("activities.html", 
        {"request": request, "outbox": outbox, 'user': username, 'inbox': inbox})

@app.post("/{username}/inbox")
async def receive_activity(username: str, request: Request):
    try:
        # Parse the request to JSON
        activity_data = await request.json()

        # Convert JSON data to an Activity object
        activity = Activity(**activity_data)

        # Add the activity to the user inbox
        save_inbox_activity(username, activity_data)
        #if username not in user_inbox:
        #    user_inbox[username] = []
        #user_inbox[username].append(activity_data)

        # Process the activity
        response = process_activity(activity)
        return response
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to process activity: {str(e)}")

@app.get("/{username}/inbox")
async def get_user_inbox(username: str):
    # Get the activities from the user inbox
    #if username not in user_inbox or len(user_inbox[username]) == 0:
    #    raise HTTPException(status_code=404, detail="Inbox is empty or user not found")

    return {"username": username, "inbox": get_inbox(username)}

@app.get("/{username}")
async def get_user(username: str):
    """
    Returns a simple JSON-LD representation of a user.
    """
    return JSONResponse(content={
        "@context": "https://www.w3.org/ns/activitystreams",
        "type": "Person",
        "id": f"https://yourdomain.com/user/{username}",
        "name": username,
        "inbox": f"https://yourdomain.com/user/{username}/inbox",
        "outbox": f"https://yourdomain.com/user/{username}/outbox",
        "followers": f"https://yourdomain.com/user/{username}/followers",
        "following": f"https://yourdomain.com/user/{username}/following",
    })

@app.get("/{username}/domainmodels")
async def get_domainmodels(username: str, request: Request):
    output = "\n".join(str(model) for model in get_domain_models().values())
    return output

@app.post("/generate_model")
async def post_user_outbox(request: Request):
    body = await request.json()
    model_id = body.get("model_id")
    domain_model_to_code(model=get_model(model_id),
                                file_path="besser_model/model.py")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
