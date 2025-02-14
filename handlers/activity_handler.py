import importlib

# Function to dynamically import the correct module based on platform
def get_activity_handlers(platform):
    if platform not in ["besser", "pyEcore"]:
        raise ValueError("Invalid platform. Choose 'besser' or 'pyEcore'.")

    module_name = f"model_slot.{platform}"
    module = importlib.import_module(module_name)  # Dynamically import the module

    return {
        "Create": module.create,
        "Update": module.update,
        "Delete": module.delete,
    }

# Define the valid object types
valid_types = {
    "DomainModel",
    "Class",
    "Property",
    "BinaryAssociation",
    "Generalization",
    "Method",
    "Parameter",
    "Package",
    "Enumeration",
    "EnumerationLiteral",
    "Grant",
}

def process_activity(activity, platform):
    """
    Executes the activity in the server based on the selected platform.
    """
    try:
        activity_handlers = get_activity_handlers(platform)

        if activity.type in activity_handlers:
            if activity.object.type in valid_types:
                activity_handlers[activity.type](activity)
                return {"status": "success", "message": f"Object {activity.type.lower()}d successfully."}
            return {"status": "error", "message": f"Unsupported object type: {activity.object['type']}"}

        return {"status": "error", "message": f"Unsupported activity type: {activity.type}"}

    except Exception as e:
        return {"status": "error", "message": f"Error processing activity: {str(e)}"}
