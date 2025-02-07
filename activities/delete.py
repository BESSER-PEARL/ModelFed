from pydantic import HttpUrl
from models import Activity
from storage import get_object, delete_object
from utils import map_type

def delete_domain_model(obj: dict, target: HttpUrl) -> None:
    """Delete a DomainModel."""
    delete_object(obj["id"])

def delete_class(obj: dict, target: HttpUrl) -> None:
    """Delete a Class."""
    cls_id = obj["id"]

    # Remove class from the domain model
    domain_model = get_object(str(target))
    domain_model.types = {typ for typ in domain_model.types if typ.id != cls_id}

    # Remove class from generalizations
    for gen in domain_model.generalizations:
        gen.general = None if gen.general.id == cls_id else gen.general
        gen.specific = None if gen.specific.id == cls_id else gen.specific

    # Remove class from packages
    for package in domain_model.packages:
        package.classes = {cls for cls in package.classes if cls.id != cls_id}

    # Remove class from properties, methods, and parameters
    for cls in domain_model.get_classes():
        if cls.attributes:
            for attr in cls.attributes:
                if attr.owner and attr.owner.id == cls_id:
                    attr.owner = None
                if attr.type and attr.type.id == cls_id:
                    attr.type = None
        if cls.methods:
            for method in cls.methods:
                if method.owner and method.owner.id == cls_id:
                    method.owner = None
                if method.type and method.type.id == cls_id:
                    method.type = None
                if method.parameters:
                    for param in method.parameters:
                        if param.type and param.type.id == cls_id:
                            param.type = None

    # Remove class from associations
    for asso in domain_model.associations:
        for end in asso.ends:
            end.type = None if end.type.id == cls_id else end.type

    delete_object(cls_id)

def delete_property(obj: dict, target: HttpUrl) -> None:
    """Delete a Property."""
    prop_obj = get_object(obj["id"])

    if prop_obj.owner:
        owner = prop_obj.owner
        if type(owner).__name__ == "Class":
            owner.attributes = {attr for attr in owner.attributes if attr.id != obj["id"]}
        elif type(owner).__name__ == "Association" or "BinaryAssociation":
            owner.ends = {end for end in owner.ends if end.id != obj["id"]}
    delete_object(obj["id"])

def delete_bin_association(obj: dict, target: HttpUrl) -> None:
    """Delete a BinaryAssociation."""
    asso_id = obj["id"]

    # Remove class from the domain model
    domain_model = get_object(str(target))
    domain_model.associations = {asso for asso in domain_model.associations if asso.id != asso_id}

    association = get_object(id_=obj["id"])
    for end in association.ends:
        end.owner = None

    delete_object(asso_id)

def update_enumeration(obj: dict, target: HttpUrl):
    enum = get_object(id_=obj["id"])

    for key in ["name"]:
        if key in obj:
            setattr(enum, key, obj[key])

    if "literals" in obj:
        enum.literals = {get_object(literal) for literal in obj["literals"]}

def delete_enumeration(obj: dict, target: HttpUrl) -> None:
    """Delete an Enumeration."""
    enum_id = obj["id"]

    # Remove enumeration from the domain model
    domain_model = get_object(str(target))
    domain_model.types = {typ for typ in domain_model.types if typ.id != enum_id}

    # Remove enumeration from properties, methods, and parameters
    for cls in domain_model.get_classes():
        if cls.attributes:
            for attr in cls.attributes:
                if attr.type and attr.type.id == enum_id:
                    attr.type = None
        if cls.methods:
            for method in cls.methods:
                if method.type and method.type.id == enum_id:
                    method.type = None
                if method.parameters:
                    for param in method.parameters:
                        if param.type and param.type.id == enum_id:
                            param.type = None

    delete_object(enum_id)

def delete_enumeration_literal(obj: dict, target: HttpUrl) -> None:
    """Delete an EnumerationLiteral."""
    literal_obj = get_object(obj["id"])

    if literal_obj.owner:
        enum = literal_obj.owner
        enum.literals = {literal for literal in enum.literals if literal.id != obj["id"]}

    delete_object(obj["id"])

def delete_generalization(obj: dict, target: HttpUrl) -> None:
    """Delete a Generalization."""
    # Remove generalization from the domain model
    domain_model = get_object(str(target))
    domain_model.generalizations = {gen for gen in domain_model.generalizations if gen.id != obj["id"]}

    delete_object(obj["id"])

def delete_method(obj: dict, target: HttpUrl) -> None:
    """Delete a Method."""
    method_obj = get_object(obj["id"])

    if method_obj.owner:
        cls = method_obj.owner
        cls.methods = {method for method in cls.methods if method.id != obj["id"]}

    if method_obj.parameters:
        for param in method_obj.parameters:
            param.owner = None

    delete_object(obj["id"])

def delete_parameter(obj: dict, target: HttpUrl) -> None:
    """Delete a Parameter."""
    parameter_obj = get_object(obj["id"])

    if parameter_obj.owner:
        method = parameter_obj.owner
        method.parameters = {param for param in method.parameters if param.id != obj["id"]}

    delete_object(obj["id"])

def delete_package(obj: dict, target: HttpUrl) -> None:
    """Delete a Package."""
    # Remove package from the domain model
    domain_model = get_object(str(target))
    domain_model.packages = {package for package in domain_model.packages if package.id != obj["id"]}

    delete_object(obj["id"])

# Map of object types to their update and delete functions
type_handlers = {
    "DomainModel": (delete_domain_model),
    "Class": (delete_class),
    "Property": (delete_property),
    "BinaryAssociation": (delete_bin_association),
    "Enumeration": (delete_enumeration),
    "EnumerationLiteral": (delete_enumeration_literal),
    "Generalization": (delete_generalization),
    "Method": (delete_method),
    "Parameter": (delete_parameter),
    "Package": (delete_package),
}

def delete(activity: Activity):
    """Delete an object dynamically based on its type."""
    obj = activity.object
    obj_type = obj.get("type")
    target = activity.target

    if obj_type in type_handlers:
        return type_handlers[obj_type](obj, target)

    raise ValueError(f"Unknown object type: {obj_type}")
