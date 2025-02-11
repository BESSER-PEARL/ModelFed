from pydantic import HttpUrl
from models import (
    MvDomainModel, MvClass, MvProperty,
    MvMethod, MvPackage, MvParameter, MvEnumeration,
    MvEnumerationLiteral, MvGeneralization, Activity,
    MvBinaryAssociation, MvGrant
)
from storage import get_object
from utils import map_type

def update_domain_model(obj: MvDomainModel, target: HttpUrl) -> None:
    """Update a DomainModel from a dictionary object."""
    model = get_object(obj.id)

    # Use a loop to update multiple fields dynamically
    for key in ["name", "types", "associations", "packages", "generalizations", "users"]:
        value = getattr(obj, key, None)
        if value is not None:
            setattr(model, key, set(value) if isinstance(value, list) else value)

def update_class(obj: MvClass, target: HttpUrl) -> None:
    """Update a Class from a dictionary object."""
    class_obj = get_object(obj.id)

    for key, attr_name in {"name": "name", "isAbstract": "is_abstract"}.items():
        value = getattr(obj, key, None)
        if value is not None:
            setattr(class_obj, attr_name, value)

    if obj.attributes is not None:
        class_obj.attributes = {get_object(attr) for attr in obj.attributes}

def update_property(obj: MvProperty, target: HttpUrl) -> None:
    """Update a Property from a dictionary object."""
    # Common attributes to update
    common_attrs = {"name": "name", "isComposite": "is_composite", "isNavigable": "is_navigable"}

    property_obj = get_object(id_=obj.id)

    # Update common attributes
    for key, attr_name in common_attrs.items():
        value = getattr(obj, key, None)
        if value is not None:
            setattr(property_obj, attr_name, value)

    # Handle elementType
    if obj.elementType is not None:
        type_ = get_object(id_=value, raise_error=False)
        if type_ is None:
            type_ = map_type(value)
        property_obj.type = type_

def update_bin_association(obj: MvBinaryAssociation, target: HttpUrl):
    association = get_object(id_=obj.id)

    if obj.name is not None:
        association.name = obj.name

    # Update ends
    if obj.ends is not None:
        association.ends = {get_object(end) for end in obj.ends}

def update_enumeration(obj: MvEnumeration, target: HttpUrl):
    enum = get_object(id_=obj.id)

    if obj.name is not None:
        enum.name = obj.name

    if obj.literals is not None:
        enum.literals = {get_object(literal) for literal in obj.literals}

def update_enumeration_literal(obj: MvEnumerationLiteral, target: HttpUrl):
    literal = get_object(id_=obj.id)

    if obj.name is not None:
        literal.name = obj.name

def update_generalization(obj: dict, target: HttpUrl) -> None:
    """Update a Generalization from a dictionary object."""
    generalization = get_object(id_=obj.id)

    # Update general class
    if obj.general is not None:
        new_general = get_object(id_=obj.general)
        generalization.general = new_general

    # Update specific class
    if obj.specific is not None:
        new_specific = get_object(id_=obj.specific)
        generalization.specific = new_specific

def update_method(obj: MvMethod, target: HttpUrl) -> None:
    """Update a Method from a dictionary object."""
    method = get_object(id_=obj.id)

    for key, attr_name in {"name": "name", "code": "code", "isAbstract": "is_abstract"}.items():
        if getattr(obj, key, None) is not None:
            setattr(method, attr_name, getattr(obj, key))

    # Handle `elementType`
    if obj.elementType is not None:
        type_ = get_object(id_=obj.elementType, raise_error=False)
        if type_ is None:
            type_ = map_type(obj.elementType)
        method.type = type_

    # Handle parameters
    if obj.parameters is not None:
        method.parameters = {get_object(param) for param in obj.parameters}

def update_parameter(obj: MvParameter, target: HttpUrl):
    parameter = get_object(id_=obj.id)

    for key, attr_name in {"name": "name", "defaultValue": "default_value"}.items():
        value = getattr(obj, key, None)
        if value is not None:
            setattr(parameter, attr_name, value)

    # Handle `elementType`
    if obj.elementType is not None:
        type_ = get_object(id_=obj.elementType, raise_error=False)
        if type_ is None:
            type_ = map_type(obj.elementType)
        parameter.type = type_

def update_package(obj: MvPackage, target: HttpUrl):
    package = get_object(id_=obj.id)

    if obj.name is not None:
        package.name = obj.name

    if obj.classes is not None:
        package.classes = {get_object(cls) for cls in obj.classes}

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
    obj_type = obj.type
    target = activity.target

    if obj_type in type_handlers:
        return type_handlers[obj_type](obj, target)

    raise ValueError(f"Unknown object type: {obj_type}")
