from pydantic import HttpUrl
from models import (
    MvDomainModel, MvClass, MvProperty,
    MvMethod, MvPackage, MvParameter, MvEnumeration,
    MvEnumerationLiteral, MvGeneralization, Activity,
    MvBinaryAssociation, MvGrant
)
from storage import get_object, delete_object, delete_grant
from model_slot.pyEcore.helpers import find_package_for_class, find_containing_class

def delete_domain_model(obj: MvDomainModel, target: HttpUrl) -> None:
    """Delete a DomainModel."""
    delete_object(obj.id)

def delete_class(obj: MvClass, target: HttpUrl) -> None:
    """Delete a Class."""
    target_class = get_object(obj.id)

    # Remove class from the domain model or subpackages
    domain_model = get_object(target)
    package_owner = find_package_for_class(domain_model, target_class)
    package_owner.eClassifiers.remove(target_class)

    delete_object(obj.id)

    # Remove class attributes and references from temporal storage
    for attr in target_class.eStructuralFeatures:
        delete_object(attr.id)


'''
    # Remove class from generalizations
    for gen in domain_model.generalizations:
        gen.general = None if gen.general == target_class else gen.general
        gen.specific = None if gen.specific == target_class else gen.specific
'''

def delete_property(obj: MvProperty, target: HttpUrl) -> None:
    """Delete a Property."""
    target_prop = get_object(obj.id)
    domain_model = get_object(target)

    containing_class = find_containing_class(domain_model, target_prop)

    if containing_class:
        containing_class.eStructuralFeatures.remove(target_prop)

    delete_object(obj.id)

'''
def delete_bin_association(obj: MvBinaryAssociation, target: HttpUrl) -> None:
    """Delete a BinaryAssociation."""
    target_asso = get_object(obj.id)

    # Remove association in the domain model
    domain_model = get_object(target)
    domain_model.associations = {asso for asso in domain_model.associations if asso != target_asso}

    # Delete end owner
    for end in target_asso.ends:
        end.owner = None

    delete_object(obj.id)

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

    delete_object(obj.id)

def delete_enumeration_literal(obj: MvEnumerationLiteral, target: HttpUrl) -> None:
    """Delete an EnumerationLiteral."""
    target_literal = get_object(obj.id)

    if target_literal.owner is not None:
        enum = target_literal.owner
        enum.literals = {literal for literal in enum.literals if literal != target_literal}

    delete_object(obj.id)

def delete_generalization(obj: MvGeneralization, target: HttpUrl) -> None:
    """Delete a Generalization."""
    # Remove generalization from the domain model
    target_gen = get_object(obj.id)
    domain_model = get_object(target)
    domain_model.generalizations = {gen for gen in domain_model.generalizations if gen != target_gen}

    delete_object(obj.id)

def delete_method(obj: MvMethod, target: HttpUrl) -> None:
    """Delete a Method."""
    target_method = get_object(obj.id)

    if target_method.owner is not None:
        cls = target_method.owner
        cls.methods = {method for method in cls.methods if method != target_method}

    if target_method.parameters is not None:
        for param in target_method.parameters:
            param.owner = None

    delete_object(obj.id)

def delete_parameter(obj: MvParameter, target: HttpUrl) -> None:
    """Delete a Parameter."""
    target_param = get_object(obj.id)

    if target_param.owner is not None:
        method = target_param.owner
        method.parameters = {param for param in method.parameters if param != target_param}

    delete_object(obj.id)

def delete_package(obj: MvPackage, target: HttpUrl) -> None:
    """Delete a Package."""
    # Remove package from the domain model
    target_package = get_object(obj.id)
    domain_model = get_object(str(target))
    domain_model.packages = {package for package in domain_model.packages if package != target_package}

    delete_object(obj.id)

'''
def remove_grant(obj: MvGrant, target: HttpUrl) -> None:
    """Delete a Grant."""
    delete_grant(obj.id)

# Map of object types to their update and delete functions
type_handlers = {
    "DomainModel": (delete_domain_model),
    "Class": (delete_class),
    "Property": (delete_property),
    # "BinaryAssociation": (delete_bin_association),
    # "Enumeration": (delete_enumeration),
    # "EnumerationLiteral": (delete_enumeration_literal),
    # "Generalization": (delete_generalization),
    # "Method": (delete_method),
    # "Parameter": (delete_parameter),
    # "Package": (delete_package),
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
