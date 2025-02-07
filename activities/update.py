from pydantic import HttpUrl
from models import Activity
from storage import get_object
from utils import map_type

def update_domain_model(obj: dict, target: HttpUrl) -> None:
    """Update a DomainModel from a dictionary object."""
    model = get_object(obj["id"])

    # Use a loop to update multiple fields dynamically
    for key in ["name", "types", "associations", "packages", "generalizations", "users"]:
        if key in obj:
            setattr(model, key, set(obj[key]) if isinstance(obj[key], list) else obj[key])

def update_class(obj: dict, target: HttpUrl) -> None:
    """Update a Class from a dictionary object."""
    class_obj = get_object(obj["id"])

    for key, attr_name in {"name": "name", "isAbstract": "is_abstract"}.items():
        if key in obj:
            setattr(class_obj, attr_name, obj[key])

    if "attributes" in obj:
        class_obj.attributes = {get_object(attr) for attr in obj["attributes"]}

def update_property(obj: dict, target: HttpUrl) -> None:
    """Update a Property from a dictionary object."""
    # Common attributes to update
    common_attrs = {"name": "name", "isComposite": "is_composite", "isNavigable": "is_navigable"}

    property_obj = get_object(id_=obj["id"])

    # Update common attributes
    for key, attr_name in common_attrs.items():
        if key in obj:
            setattr(property_obj, attr_name, obj[key])
    # Handle `elementType`
    if "elementType" in obj:
        type_ = get_object(id_=obj["elementType"], raise_error=False)
        if type_ is None:
            type_ = map_type(obj["elementType"])
        property_obj.type = type_

def update_bin_association(obj: dict, target: HttpUrl):
    association = get_object(id_=obj["id"])

    for key in ["name"]:
        if key in obj:
            setattr(association, key, obj[key])

    # Update ends
    if "ends" in obj:
        association.ends = {get_object(end) for end in obj["ends"]}


def update_enumeration(obj: dict, target: HttpUrl):
    enum = get_object(id_=obj["id"])

    for key in ["name"]:
        if key in obj:
            setattr(enum, key, obj[key])

    if "literals" in obj:
        enum.literals = {get_object(literal) for literal in obj["literals"]}

def update_enumeration_literal(obj: dict, target: HttpUrl):
    literal = get_object(id_=obj["id"])

    for key in ["name"]:
        if key in obj:
            setattr(literal, key, obj[key])

def update_generalization(obj: dict, target: HttpUrl) -> None:
    """Update a Generalization from a dictionary object."""
    generalization = get_object(id_=obj["id"])

    # Update general class
    if "general" in obj:
        new_general = get_object(id_=obj["general"])
        generalization.general = new_general

    # Update specific class
    if "specific" in obj:
        new_specific = get_object(id_=obj["specific"])
        generalization.specific = new_specific

def update_method(obj: dict, target: HttpUrl) -> None:
    """Update a Method from a dictionary object."""
    model = get_object(id_=str(target))

    method = get_object(id_=obj["id"])
    for key, attr_name in {"name": "name", "code": "code", "isAbstract": "is_abstract"}.items():
        if key in obj:
            setattr(method, attr_name, obj[key])

    # Handle `elementType`
    if "elementType" in obj:
        type_ = get_object(id_=obj["elementType"], raise_error=False)
        if type_ is None:
            type_ = map_type(obj["elementType"])
        method.type = type_

    # Handle parameters
    if 'parameters' in obj:
        method.parameters = {get_object(param) for param in obj["parameters"]}

def update_parameter(obj: dict, target: HttpUrl):
    parameter = get_object(id_=obj["id"])

    for key in {"name": "name", "defaultValue": "default_value"}.items():
        if key in obj:
            setattr(parameter, key, obj[key])

    # Handle `elementType`
    if "elementType" in obj:
        type_ = get_object(id_=obj["elementType"], raise_error=False)
        if type_ is None:
            type_ = map_type(obj["elementType"])
        parameter.type = type_

def update_package(obj: dict, target: HttpUrl):
    package = get_object(id_=obj["id"])

    for key in {"name": "name"}.items():
        if key in obj:
            setattr(package, key, obj[key])

    if "classes" in obj:
        package.classes = {get_object(cls) for cls in obj["classes"]}

# Map of object types to their update functions
type_handlers = {
    "DomainModel": update_domain_model,
    "Class": update_class,
    "Property": update_property,
    "BinaryAssociation": update_bin_association,
    "Enumeration": update_enumeration,
    "EnumerationLiteral": update_enumeration_literal,
    "Generalization": update_generalization,
    "Method": update_method,
    "Parameter": update_parameter,
    "Package": update_package,
}

def update(activity: Activity):
    """Update an object dynamically based on its type."""
    obj = activity.object
    obj_type = obj.get("type")
    target = activity.target

    if obj_type in type_handlers:
        return type_handlers[obj_type](obj, target)

    raise ValueError(f"Unknown object type: {obj_type}")
