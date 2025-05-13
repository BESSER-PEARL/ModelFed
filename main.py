import logging
import argparse
import uvicorn
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.templating import Jinja2Templates
from besser.utilities import domain_model_to_code, sort_by_timestamp
from models import Activity
from federation import federate_activity
from storage import get_inbox, get_outbox, save_outbox_activity, save_inbox_activity, get_object
from handlers.activity_handler import process_activity

# Logging setup
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

PLATFORM = ""
app = FastAPI()

# Templates
templates = Jinja2Templates(directory="templates")

# Global exception handler to capture detailed error information
@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    # Log error details
    logger.error(f"Error in request: {request.url.path}")
    logger.error(f"Error details: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": f"An error occurred: {exc.detail}"}
    )

# Route to receive activities for the 'outbox'
@app.post("/{username}/outbox")
async def post_user_outbox(request: Request, username: str):
    try:
        # Parse request JSON
        activity_data = await request.json()

        # Convert JSON data to an Activity object
        activity = Activity(**activity_data)

        # Process the activity
        response = process_activity(activity, PLATFORM)

        # Add the activity to the user's outbox
        save_outbox_activity(username, activity_data)

        # Federation of activities if there are recipients
        if activity.to:
            federate_activity(activity_data)

        return response

    except Exception as e:
        logger.error(f"Error in 'outbox': {str(e)}")
        raise HTTPException(status_code=400, detail=f"Invalid activity format: {str(e)}") from e

# Route to get the user's activities (inbox and outbox)
@app.get("/{username}/activities")
async def get_user_outbox(username: str, request: Request):
    outbox = get_outbox(username)
    inbox = get_inbox(username)
    return templates.TemplateResponse("activities.html", 
        {"request": request, "outbox": outbox, 'user': username, 'inbox': inbox})

# Route to receive an activity in the 'inbox'
@app.post("/{username}/inbox")
async def receive_activity(username: str, request: Request):
    try:
        # Parse request JSON
        activity_data = await request.json()

        # Convert JSON data to an Activity object
        activity = Activity(**activity_data)

        # Add the activity to the user's inbox
        save_inbox_activity(username, activity_data)

        # Process the activity
        response = process_activity(activity, PLATFORM)
        return response

    except Exception as e:
        logger.error(f"Error processing activity: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Failed to process activity: {str(e)}")

# Route to get the user's inbox
@app.get("/{username}/inbox")
async def get_user_inbox(username: str):
    return {"username": username, "inbox": get_inbox(username)}

# Route to get the user's Besser model
@app.get("/{username}/besser_model/{m_id}")
async def get_besser_model(username: str, m_id: str):
    # Get the domain model object
    model_id = "http://127.0.0.1:8000/" + username + "/domainmodel/" + m_id
    model = get_object(id_=model_id)

    output = f"Contents of model '{model.name}':\n"

    # Iterate over all classes in the model
    if model.get_classes():
        for class_ in sort_by_timestamp(model.get_classes()):
            output += f"\n  Class: {class_.name}\n"

            # Iterate over the attributes of the class
            if class_.attributes:
                output += "    Attributes:\n"
                for attr in sort_by_timestamp(class_.attributes):
                    output += f"      - {attr.name}: {attr.type.name}\n"

    # Iterate over all associations in the model
    if model.associations:
        for association in sort_by_timestamp(model.associations):
            output += f"\n  Association: {association.name}\n"

            # Iterate over the 'ends' (properties of the association)
            if association.ends:
                output += "    Ends:\n"
                for end in sort_by_timestamp(association.ends):
                    output += f"      - {end.name}: {end.type.name}\n"
            else:
                output += "    No ends found for this association.\n"

    # Iterate over all generalizations in the model
    if model.generalizations:
        for generalization in sort_by_timestamp(model.generalizations):
            output += "\n  Generalization:\n"
            output += f"    General: {generalization.general.name}\n"
            output += f"    Specific: {generalization.specific.name}\n"

    # Iterate over all enumerations in the model
    if model.get_enumerations():
        for enumeration in sort_by_timestamp(model.get_enumerations()):
            output += f"\n  Enumeration: {enumeration.name}\n"

            # Iterate over the enumeration literals
            if enumeration.literals:
                output += "    Literals:\n"
                for literal in sort_by_timestamp(enumeration.literals):
                    output += f"      - {literal.name}\n"

    # Iterate over all packages
    if model.packages:
        for package in sort_by_timestamp(model.packages):
            output += f"\n  Package: {package.name}\n"

            # Iterate over the classes in the package
            output += "    Elements: "
            output += ", ".join([element.name for element in sort_by_timestamp(package.elements)])
            output += "\n"

    # Return the output as plain text (with line breaks)
    return PlainTextResponse(content=output)

# Route to retrieve and display the PyEcore model
from pyecore.ecore import EClass, EEnum
@app.get("/{username}/pyecore_model/{m_id}")
async def get_pyecore_model(username: str, m_id: str):
    model_id = "http://127.0.0.1:8000/" + username + "/domainmodel/" + m_id
    model = get_object(id_=model_id)

    output = f"Contents of model '{model.name}':\n"

    # Function to recursively explore and print package information
    def explore_package(pkg, indent=""):
        nonlocal output

        # Print the package name
        output += f"\nPackage: {pkg.name}\n"

        # Process each classifier (EClass, EEnum, etc.) within the current package
        for eclass in pkg.eClassifiers:
            if isinstance(eclass, EClass):
                # Handle EClass
                output += f"  Class: {eclass.name}\n"

                # List class attributes if any
                if eclass.eAttributes:
                    output += "    Attributes:\n"
                    for attr in eclass.eAttributes:
                        output += f"      - {attr.name}: {attr.eType.name}\n"

                # List class references if any
                if eclass.eReferences:
                    output += "    References:\n"
                    for ref in eclass.eReferences:
                        opposite_name = ref.eOpposite.name if ref.eOpposite else "None"
                        output += f"      - {ref.name}: {ref.eType.name}, Opposite: {opposite_name}\n"

                # List class supertypes if any
                if eclass.eSuperTypes:
                    output += "    Supertypes:\n"
                    for supertype in eclass.eSuperTypes:
                        output += f"      - {supertype.name}\n"

            elif isinstance(eclass, EEnum):
                # Handle EEnum
                output += f"  Enum: {eclass.name}\n"
                if eclass.eLiterals:
                    output += "    Literals:\n"
                    for literal in eclass.eLiterals:
                        output += f"      - {literal.name}\n"

        # Recursively explore subpackages
        for sub_pkg in pkg.eSubpackages:
            explore_package(sub_pkg, indent + "  ")

    # Start the exploration with the root model (main package)
    explore_package(model)

    # Return the formatted output as plain text
    return PlainTextResponse(content=output)

# Route to generate model code from the provided 'model_id'
@app.post("/generate_model")
async def generate_model(request: Request):
    try:
        body = await request.json()
        model_id = body.get("model_id")
        file_path = body.get("file_path")

        if not model_id:
            raise HTTPException(status_code=400, detail="model_id is required")

        domain_model_to_code(model=get_object(model_id), file_path=file_path)
        return {"message": "Model code generated successfully."}

    except Exception as e:
        logger.error(f"Error generating model: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Failed to generate model: {str(e)}")

# Main function to run the FastAPI server
if __name__ == "__main__":
    # Configure arguments to select platform
    parser = argparse.ArgumentParser(description="Run FastAPI server with platform-based port selection.")
    parser.add_argument("--platform", choices=["besser", "pyEcore"], required=True, help="Specify the platform (besser or pyEcore)")
    parser.add_argument("--port", type=int, default=8000, help="Port number to run the server on")
    args = parser.parse_args()

    # Select port based on the platform
    PLATFORM = args.platform
    PORT = args.port
    if PLATFORM != "besser" and PLATFORM != "pyEcore":
        logger.error("Invalid platform specified.")
        exit(1)

    # Start the app
    uvicorn.run(app, host="0.0.0.0", port=PORT)
