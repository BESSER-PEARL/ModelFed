from besser.BUML.metamodel.structural import (
    StringType, IntegerType, DateTimeType, TimeType,
    BooleanType, FloatType, TimeDeltaType, DateType,
    Multiplicity
)
from models import Activity
from storage import get_object

def map_type(type_str):
    """Parses a string dataType and returns a PrimitiveDataType object"""
    mapping = {
        "int": IntegerType,
        "str": StringType,
        "date": DateType,
        "datetime": DateTimeType,
        "time": TimeType,
        "boolean": BooleanType,
        "float": FloatType,
        "timedelta": TimeDeltaType
    }
    return mapping.get(type_str, None)

def parse_multiplicity(multiplicity_str: str) -> Multiplicity:
    """Parses a string representation of multiplicity and returns a Multiplicity object."""

    if multiplicity_str == "*":
        return Multiplicity(0, "*")

    parts = multiplicity_str.split("..")

    if len(parts) == 1:
        min_val = max_val = int(parts[0])
    else:
        min_val = int(parts[0])
        max_val = parts[1] if parts[1] == "*" else int(parts[1])

    return Multiplicity(min_val, max_val)

def check_permission(activity: Activity) -> bool:
    """Checks if the actor has permission to perform the activity on the target."""
    domain_model = get_object(id_=str(activity.target))
    if activity.type == "Create":
        for grant in domain_model.grants:
            print(grant.user)
            print(activity.actor)
            if grant.user == str(activity.actor) and (grant.role == "admin" or grant.role == "write"):
                return True
    elif activity.type == "Update":
        for grant in domain_model.grants:
            if grant.user == activity.actor and grant.role == "admin" or "write":
                return True
    elif activity.type == "Delete":
        for grant in domain_model.grants:
            if grant.user == activity.actor and grant.role == "admin":
                return True
    return False