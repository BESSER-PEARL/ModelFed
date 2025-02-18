from pydantic import HttpUrl
from models import (
    MvDomainModel, MvClass, MvProperty,
    MvMethod, MvPackage, MvParameter, MvEnumeration,
    MvEnumerationLiteral, MvGeneralization, Activity,
    MvBinaryAssociation, MvGrant
)
from pyecore.ecore import EAttribute, EPackage, EClass
from storage import get_object, save_object
from model_slot.pyEcore.helpers import map_type, parse_multiplicity

def update_domain_model(obj: MvDomainModel, target: HttpUrl) -> None:
    """Update a DomainModel from a dictionary object."""
    model = get_object(obj.id)

    if getattr(obj, "name", None) is not None:
        model.name = obj.name

    # Use a loop to update multiple fields dynamically
    # for key in ["name", "types", "associations", "packages", "generalizations"]:
    #     value = getattr(obj, key, None)
    #     if value is not None:
    #         setattr(model, key, set(value) if isinstance(value, list) else value)

def update_class(obj: MvClass, target: HttpUrl) -> None:
    """Update a Class in PyEcore."""
    class_obj = get_object(obj.id)

    if obj.name is not None:
        class_obj.name = obj.name
    if obj.isAbstract is not None:
        class_obj.abstract = obj.isAbstract

    if obj.attributes is not None:
        attrs = [get_object(attr) for attr in obj.attributes]
        # Remove old attributes
        for feature in list(class_obj.eStructuralFeatures):
            if isinstance(feature, EAttribute):
                class_obj.eStructuralFeatures.remove(feature)
        # Add new attributes
        class_obj.eStructuralFeatures.extend(attrs)

def update_property(obj: MvProperty, target: HttpUrl) -> None:
    """Update a Property - EAttribute in PyEcore."""
    property_obj = get_object(id_=obj.id)

    if obj.name is not None:
        property_obj.name = obj.name

    if obj.isId is not None:
        property_obj.iD = bool(obj.isId)

    # Handle multiplicity
    if obj.multiplicity is not None:
        mult = parse_multiplicity(obj.multiplicity)
        property_obj.lower = mult[0]
        property_obj.upper = mult[1]

    # Handle elementType
    if obj.elementType is not None:
        type_ = get_object(id_=obj.elementType, raise_error=False)
        if type_ is None:
            type_ = map_type(obj.elementType)
        property_obj.eType = type_

def update_bin_association(obj: MvBinaryAssociation, target: HttpUrl):
    association = get_object(id_=obj.id)

    # Update ends
    if obj.ends is not None:
        pass


def update_enumeration(obj: MvEnumeration, target: HttpUrl):
    enum = get_object(id_=obj.id)

    if obj.name is not None:
        enum.name = obj.name

    if obj.literals is not None:
        literals = []
        for lit in obj.literals:
            enum_literal = get_object(lit.id)
            literals.append(enum_literal)
        enum.literals = literals

def update_enumeration_literal(obj: MvEnumerationLiteral, target: HttpUrl):
    literal = get_object(id_=obj.id)

    if obj.name is not None:
        literal.name = obj.name

    if obj.owner is not None:
        new_owner = get_object(id_=obj.owner)
        new_owner.literals.append(literal)

    if obj.value is not None:
        literal.value = obj.value

def update_generalization(obj: dict, target: HttpUrl) -> None:
    """Update a Generalization from a dictionary object."""
    generalization = get_object(id_=obj.id)
    old_general = generalization[0]
    old_specific = generalization[1]
    old_specific.eSuperTypes.remove(old_general)

    new_general = get_object(id_=obj.general)
    new_specific = get_object(id_=obj.specific)

    new_specific.eSuperTypes.append(new_general)

    # Update the generalization in the storage
    save_object(obj.id, [new_general, new_specific])

def update_package(obj: MvPackage, target: HttpUrl):
    package = get_object(id_=obj.id)

    if obj.name is not None:
        package.name = obj.name

    if obj.elements is not None:
        subpackages = []
        elements = []
        for element_id in obj.elements:
            element = get_object(id_=element_id)
            if isinstance(element, EPackage):
                subpackages.append(element)
            elif isinstance(element, EClass):
                elements.append(element)
        package.eSubpackages = subpackages
        package.eClassifiers = elements

# Map of object types to their update functions
type_handlers = {
    "DomainModel": update_domain_model,
    "Class": update_class,
    "Property": update_property,
    "BinaryAssociation": update_bin_association,
    "Enumeration": update_enumeration,
    "EnumerationLiteral": update_enumeration_literal,
    "Generalization": update_generalization,
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
