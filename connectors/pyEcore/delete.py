from pydantic import HttpUrl
from models import (
    MvDomainModel, MvClass, MvProperty,
    MvMethod, MvPackage, MvParameter, MvEnumeration,
    MvEnumerationLiteral, MvGeneralization, Activity,
    MvBinaryAssociation, MvGrant
)
from storage import get_object, delete_object_by_id, delete_grant, delete_object
from connectors.pyEcore.helpers import find_containing_class, remove_supertype, remove_reference, remove_literal, remove_subpackage

def delete_domain_model(obj: MvDomainModel, target: HttpUrl) -> None:
    """Delete a DomainModel."""
    delete_object_by_id(obj.id)

def delete_class(obj: MvClass, target: HttpUrl) -> None:
    """Delete a Class."""
    target_class = get_object(obj.id)

    # Remove generalizations or supertype references
    domain_model = get_object(target)
    remove_supertype(domain_model, target_class)

    # Remove class from the domain model or subpackages
    target_class.eContainer().eClassifiers.remove(target_class)

    delete_object_by_id(obj.id)

    # Remove class attributes and references from temporal storage
    for attr in target_class.eStructuralFeatures:
        delete_object_by_id(attr.id)

def delete_property(obj: MvProperty, target: HttpUrl) -> None:
    """Delete a Property."""
    target_prop = get_object(obj.id)
    domain_model = get_object(target)

    containing_class = find_containing_class(domain_model, target_prop)

    if containing_class:
        containing_class.eStructuralFeatures.remove(target_prop)

    delete_object_by_id(obj.id)

def delete_bin_association(obj: MvBinaryAssociation, target: HttpUrl) -> None:
    """Delete a BinaryAssociation."""
    target_asso = get_object(obj.id)
    domain_model = get_object(target)

    for reference in target_asso:
        remove_reference(domain_model, reference)

    delete_object_by_id(obj.id)

def delete_enumeration(obj: MvEnumeration, target: HttpUrl) -> None:
    """Delete an Enumeration."""
    target_enum = get_object(obj.id)

    # Remove enumeration from the domain model
    target_enum.eContainer().eClassifiers.remove(target_enum)

    # # Remove enumeration from properties, methods, and parameters
    # for cls in domain_model.get_classes():
    #     if cls.attributes:
    #         for attr in cls.attributes:
    #             if attr.type and attr.type == target_enum:
    #                 attr.type = None
    #     if cls.methods:
    #         for method in cls.methods:
    #             if method.type and method.type == target_enum:
    #                 method.type = None
    #             if method.parameters:
    #                 for param in method.parameters:
    #                     if param.type and param.type == target_enum:
    #                         param.type = None

    if target_enum.eLiterals:
        for literal in target_enum.eLiterals:
            delete_object(literal)

    delete_object_by_id(obj.id)

def delete_enumeration_literal(obj: MvEnumerationLiteral, target: HttpUrl) -> None:
    """Delete an EnumerationLiteral."""
    target_literal = get_object(obj.id)

    domain_model = get_object(target)
    remove_literal(domain_model, target_literal)

    delete_object_by_id(obj.id)

def delete_generalization(obj: MvGeneralization, target: HttpUrl) -> None:
    """Delete a Generalization."""
    # Remove generalization or superType reference from the specific class
    general_class = get_object(obj.id)[0]
    specific_class = get_object(obj.id)[1]

    specific_class.eSuperTypes.remove(general_class)

    delete_object_by_id(obj.id)

def delete_package(obj: MvPackage, target: HttpUrl) -> None:
    """Delete a Package."""
    target_package = get_object(obj.id)
    domain_model = get_object(target)

    remove_subpackage(domain_model, target_package)

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
