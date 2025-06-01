from pydantic import HttpUrl
from models import (
    MvDomainModel, MvClass, MvProperty,
    MvMethod, MvPackage, MvParameter, MvEnumeration,
    MvEnumerationLiteral, MvGeneralization, Activity,
    MvBinaryAssociation, MvGrant
)
from storage import get_object, delete_object_by_id, delete_grant, delete_object
from utils import check_permission

def delete_domain_model(obj: MvDomainModel, target: HttpUrl) -> None:
    """Delete a DomainModel."""
    delete_object_by_id(obj.id)

def delete_class(obj: MvClass, target: HttpUrl) -> None:
    """Delete a Class."""
    target_class = get_object(obj.id)

    # Remove class from the domain model
    domain_model = get_object(target)
    domain_model.types = {typ for typ in domain_model.types if typ != target_class}

    #Remove attributes and methods of the class
    if target_class.attributes:
        for attr in target_class.attributes:
            delete_property(attr, target)
    if target_class.methods:
        for method in target_class.methods:
            delete_method(method, target)

    # Remove generalizations
    for gen in domain_model.generalizations.copy():  # Iterate over a copy
        if gen.general == target_class or gen.specific == target_class:
            domain_model.generalizations.discard(gen)
            delete_object(gen)

    # Remove class from packages
    for package in domain_model.packages:
        package.classes = {cls for cls in package.classes if cls != target_class}

    # Remove class from properties, methods, and parameters
    for cls in domain_model.get_classes():
        if cls.attributes:
            for attr in cls.attributes:
                if attr.owner and attr.owner == target_class:
                    attr.owner = None
                if attr.type and attr.type == target_class:
                    attr.type = None
        if cls.methods:
            for method in cls.methods:
                if method.owner and method.owner == target_class:
                    method.owner = None
                if method.type and method.type == target_class:
                    method.type = None
                if method.parameters:
                    for param in method.parameters:
                        if param.type and param.type == target_class:
                            param.type = None

    # Remove class from associations
    for asso in domain_model.associations:
        for end in asso.ends:
            end.type = None if end.type == target_class else end.type

    delete_object_by_id(obj.id)

def delete_property(obj: MvProperty, target: HttpUrl) -> None:
    """Delete a Property."""
    target_prop = get_object(obj.id)

    if target_prop.owner:
        owner = target_prop.owner
        if type(owner).__name__ == "Class":
            owner.attributes = {attr for attr in owner.attributes if attr != target_prop}
        elif type(owner).__name__ in {"Association", "BinaryAssociation"}:
            owner.ends = {end for end in owner.ends if end != target_prop}
    delete_object_by_id(obj.id)

def delete_bin_association(obj: MvBinaryAssociation, target: HttpUrl) -> None:
    """Delete a BinaryAssociation."""
    target_asso = get_object(obj.id)

    # Remove association in the domain model
    domain_model = get_object(target)
    domain_model.associations = {asso for asso in domain_model.associations if asso != target_asso}

    # Delete end owner
    for end in target_asso.ends:
        end.owner = None

    delete_object_by_id(obj.id)

def delete_enumeration(obj: MvEnumeration, target: HttpUrl) -> None:
    """Delete an Enumeration."""
    target_enum = get_object(obj.id)

    # Remove enumeration from the domain model
    domain_model = get_object(str(target))
    domain_model.types = {typ for typ in domain_model.types if typ != target_enum}

    # Remove enumeration from properties, methods, and parameters
    for cls in domain_model.get_classes():
        if cls.attributes:
            for attr in cls.attributes:
                if attr.type and attr.type == target_enum:
                    attr.type = None
        if cls.methods:
            for method in cls.methods:
                if method.type and method.type == target_enum:
                    method.type = None
                if method.parameters:
                    for param in method.parameters:
                        if param.type and param.type == target_enum:
                            param.type = None

    delete_object_by_id(obj.id)

def delete_enumeration_literal(obj: MvEnumerationLiteral, target: HttpUrl) -> None:
    """Delete an EnumerationLiteral."""
    target_literal = get_object(obj.id)

    if target_literal.owner is not None:
        enum = target_literal.owner
        enum.literals = {literal for literal in enum.literals if literal != target_literal}

    delete_object_by_id(obj.id)

def delete_generalization(obj: MvGeneralization, target: HttpUrl) -> None:
    """Delete a Generalization."""
    # Remove generalization from the domain model
    target_gen = get_object(obj.id)
    domain_model = get_object(target)
    domain_model.generalizations = {gen for gen in domain_model.generalizations if gen != target_gen}

    delete_object_by_id(obj.id)

def delete_method(obj: MvMethod, target: HttpUrl) -> None:
    """Delete a Method."""
    target_method = get_object(obj.id)

    if target_method.owner is not None:
        cls = target_method.owner
        cls.methods = {method for method in cls.methods if method != target_method}

    if target_method.parameters is not None:
        for param in target_method.parameters:
            delete_parameter(param, target)

    delete_object_by_id(obj.id)

def delete_parameter(obj: MvParameter, target: HttpUrl) -> None:
    """Delete a Parameter."""
    target_param = get_object(obj.id)

    if target_param.owner is not None:
        method = target_param.owner
        method.parameters = {param for param in method.parameters if param != target_param}

    delete_object_by_id(obj.id)

def delete_package(obj: MvPackage, target: HttpUrl) -> None:
    """Delete a Package."""
    # Remove package from the domain model
    target_package = get_object(obj.id)
    domain_model = get_object(target)
    domain_model.packages = {package for package in domain_model.packages if package != target_package}

    delete_object_by_id(obj.id)

def remove_grant(obj: MvGrant, target: HttpUrl) -> None:
    """Delete a Grant."""
    delete_grant(obj.id)

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
    "Grant": (remove_grant),
}

def delete(activity: Activity):
    """Delete an object dynamically based on its type."""
    obj = activity.object
    obj_type = obj.type
    target = activity.target

    if obj_type in type_handlers:
        return type_handlers[obj_type](obj, target)

    raise ValueError(f"Unknown object type: {obj_type}")
