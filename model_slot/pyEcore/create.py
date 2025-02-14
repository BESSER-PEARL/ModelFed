import random
import string
from pyecore.ecore import (
    EClass, EAttribute, EReference,
    EPackage, EEnum, EEnumLiteral
)
from pydantic import HttpUrl
from models import (
    MvDomainModel, MvClass, MvProperty,
    MvMethod, MvPackage, MvParameter, MvEnumeration,
    MvEnumerationLiteral, MvGeneralization, Activity,
    MvBinaryAssociation, MvGrant
)
from utils import check_permission
from model_slot.pyEcore.helpers import map_type, parse_multiplicity
from storage import save_object, get_object, save_grant


def create_domain_model(obj: MvDomainModel, target: HttpUrl) -> None:
    """Creates a DomainModel (EPackage in PyEcore)."""
    new_model = EPackage(name=obj.name)

    save_object(obj.id, new_model)

def create_class(obj: MvClass, target: HttpUrl) -> None:
    """Creates a Class with attributes if provided."""
    params = {"name": obj.name}

    if obj.isAbstract is not None:
        params["abstract"] = obj.isAbstract

    new_class = EClass(**params)

    if obj.attributes is not None:
        attrs = []
        for attr in obj.attributes:
            attr_obj = create_property(obj=attr, target=target)
            attrs.append(attr_obj)
        new_class.eStructuralFeatures.extend(attrs)

    # Add the new class to the domain model (Epackage in PyEcore)
    domain_model = get_object(id_=target)
    domain_model.eClassifiers.append(new_class)
    save_object(obj.id, new_class)

def create_property(obj: MvProperty, target: HttpUrl) -> EAttribute:
    """Creates a Property object (EAttribute in PyEcore)."""
    params = {"name": obj.name}

    # Handle isID
    if obj.isId is not None:
        params["iD"] = bool(obj.isId)

    # Handle eType
    type_ = get_object(id_=obj.elementType, raise_error=False)
    if type_ is None:
        type_ = map_type(obj.elementType)

    # Handle multiplicity
    if obj.multiplicity is not None:
        mult = parse_multiplicity(obj.multiplicity)
    else:
        mult = [1, 1]

    params["eType"] = type_
    params["lower"] = mult[0]
    params["upper"] = mult[1]

    new_property = EAttribute(**params)

    # Add the property to its owner
    if obj.owner is not None:
        owner = get_object(obj.owner)
        owner.eStructuralFeatures.append(new_property)

    save_object(obj.id, new_property)
    return new_property

def create_bin_association(obj: MvBinaryAssociation, target: HttpUrl) -> None:
    """Creates a Binary Association (EReference in PyEcore)"""
    end1 = obj.ends[0]
    cls1 = get_object(id_=end1.elementType)
    end2 = obj.ends[1]
    cls2 = get_object(id_=end2.elementType)

    new_association1 = None
    new_association2 = None
    new_asso = []

    # Create EReferece if end1 is navigable
    if end1.isNavigable is None or bool(end1.isNavigable) is True:
        # Handle multiplicity
        if end1.multiplicity is not None:
            mult = parse_multiplicity(end1.multiplicity)
        else:
            mult = [1, 1]
        new_association1 = EReference(name=end1.name,
                                      eType=cls2,
                                      lower=mult[0],
                                      upper=mult[1])
        cls1.eStructuralFeatures.append(new_association1)
        new_asso.append(new_association1)

    # Create EReference if end2 is navigable (eOppposite if its bidirectional)
    if end2.isNavigable is None or bool(end2.isNavigable) is True:
        # Handle multiplicity
        if end2.multiplicity is not None:
            mult = parse_multiplicity(end2.multiplicity)
        else:
            mult = [1, 1]

        oposite = new_association1 if new_association1 is not None else None
        new_association2 = EReference(name=end2.name,
                                      eType=cls1,
                                      lower=mult[0],
                                      upper=mult[1],
                                      eOpposite=oposite)

        cls2.eStructuralFeatures.append(new_association2)
        new_asso.append(new_association2)

    # Add the new association to the EClass
    save_object(obj.id, new_asso)


def create_generalization(obj: MvGeneralization, target: HttpUrl) -> None:
    """Creates a Generalization"""
    general_class = get_object(id_=obj.general)
    specific_class = get_object(id_=obj.specific)

    specific_class.eSuperTypes.append(general_class)

    # Store the new generalization
    save_object(obj.id, [general_class, specific_class])


def create_package(obj: MvPackage, target: HttpUrl) -> None:
    domain_model = get_object(id_=target)
    elements = []
    sub_packages = []

    for element_id in obj.elements:
        element = get_object(id_=element_id)
        if isinstance(element, EClass):
            elements.append(element)
        elif isinstance(element, EPackage):
            sub_packages.append(element)

    new_package = EPackage(name=obj.name)
    if elements:
        new_package.eClassifiers.extend(elements)
    if sub_packages:
        new_package.eSubpackages.extend(sub_packages)

    # Store the new package
    domain_model.eSubpackages.append(new_package)
    save_object(obj.id, new_package)

def create_enumeration(obj: MvEnumeration, target: HttpUrl) -> None:
    literals = []

    for lit in obj.literals:
        enum_literal = create_enumeration_literal(lit, target)
        literals.append(enum_literal)

    new_enumeration = EEnum(name=obj.name)

    if literals:
        new_enumeration.eLiterals.extend(literals)

    # Add the new enumeration to the domain model
    domain_model = get_object(id_=target)
    domain_model.eClassifiers.append(new_enumeration)
    save_object(obj.id, new_enumeration)

def create_enumeration_literal(obj: MvEnumerationLiteral, target: HttpUrl) -> EEnumLiteral:
    new_literal = EEnumLiteral(name=obj.name)

    if obj.owner is not None:
        enum = get_object(id_=obj.owner)
        enum.eLiterals.append(new_literal)

    save_object(obj.id, new_literal)
    return new_literal

def create_grant(obj: MvGrant, target: HttpUrl) -> None:
    save_grant(obj.id, obj)

# Map
type_handlers = {
    "DomainModel": create_domain_model,
    "Class": create_class,
    "Property": create_property,
    "BinaryAssociation": create_bin_association,
    "Generalization": create_generalization,
    "Package": create_package,
    "Enumeration": create_enumeration,
    "EnumerationLiteral": create_enumeration_literal,
    "Grant": create_grant,
    }

def generate_id(length=6):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def create(activity: Activity):
    """Creates an object dynamically."""
    obj = activity.object
    obj_type = obj.type
    target = activity.target

    #if obj_type != "DomainModel":
    #    if check_permission(activity) is False:
    #        raise PermissionError("Permission denied.")

    if obj_type in type_handlers:
        result = type_handlers[obj_type](obj, target)
        # Create a grant for the object if it is not a grant
        if obj_type != "Grant":
            create_grant(obj=MvGrant(type="Grant",
                                    id="http://localhost:8000/grants/" + generate_id(),
                                    modelElement=obj.id,
                                    user=activity.actor,
                                    role="admin"
                                    ),
                        target=target)
        return result

    raise ValueError(f"Unknown object type: {obj_type}")
