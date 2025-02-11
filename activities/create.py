import random
import string
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, BinaryAssociation,
    Multiplicity, Generalization, Method, Parameter,
    Package, Enumeration, EnumerationLiteral
)
from pydantic import HttpUrl
from models import (
    MvDomainModel, MvClass, MvProperty,
    MvMethod, MvPackage, MvParameter, MvEnumeration,
    MvEnumerationLiteral, MvGeneralization, Activity,
    MvBinaryAssociation, MvGrant
)
from utils import check_permission
from utils import map_type, parse_multiplicity
from storage import save_object, get_object, save_grant


def create_domain_model(obj: MvDomainModel, target: HttpUrl) -> None:
    """Creates a DomainModel from a dictionary object."""
    new_model = DomainModel(name=obj.name)

    save_object(obj.id, new_model)

def create_class(obj: MvClass, target: HttpUrl) -> None:
    """Creates a Class with attributes if provided."""
    params = {"name": obj.name}

    if obj.isAbstract is not None:
        params["is_abstract"] = obj.isAbstract

    new_class = Class(**params)

    if obj.attributes is not None:
        attrs = set()
        for attr in obj.attributes:
            attr_obj = create_property(obj=attr, target=target)
            attrs.add(attr_obj)
        new_class.attributes = attrs

    if obj.methods is not None:
        methods = set()
        for method in obj.methods:
            print(method)
            method_obj = create_method(obj=method, target=target)
            methods.add(method_obj)
        new_class.methods = methods

    # Add the new class to the domain model
    domain_model = get_object(id_=target)
    domain_model.types = domain_model.types | {new_class}
    save_object(obj.id, new_class)

def create_property(obj: MvProperty, target: HttpUrl) -> Property:
    """Creates a Property object of BESSER."""
    params = {"name": obj.name}

    if obj.isComposite is not None:
        params["is_composite"] = obj.isComposite
    if obj.isNavigable is not None:
        params["is_navigable"] = obj.isNavigable

    type_ = get_object(id_=obj.elementType, raise_error=False)
    if type_ is None:
        type_ = map_type(obj.elementType)
    if obj.multiplicity is not None:
        mult = parse_multiplicity(obj.multiplicity)
    else:
        mult = Multiplicity(1,1)

    params["type"] = type_
    params["multiplicity"] = mult

    new_property = Property(**params)
    #new_property.id = obj["id"]

    # Add the property to its owner
    if obj.owner is not None:
        owner = get_object(obj.owner, raise_error=False)
        if owner is not None:
            if type(owner).__name__ == "Class":
                owner.attributes = owner.attributes | {new_property}
            elif type(owner).__name__ in ('Association', 'BinaryAssociation'):
                owner.ends = owner.ends | {new_property}

    save_object(obj.id, new_property)
    return new_property

def create_bin_association(obj: MvBinaryAssociation, target: HttpUrl) -> None:
    """Creates a Binary Association"""
    domain_model = get_object(id_=target)
    end1 = obj.ends[0]
    end2 = obj.ends[1]

    end1_obj = create_property(obj=end1, target=target)
    end2_obj = create_property(obj=end2, target=target)

    new_association = BinaryAssociation(name=obj.name,
                                        ends={end1_obj, end2_obj})

    # Add the new association to its domain model
    domain_model.associations = domain_model.associations | {new_association}
    save_object(obj.id, new_association)

def create_generalization(obj: MvGeneralization, target: HttpUrl) -> None:
    """Creates a Generalization"""
    domain_model = get_object(id_=target)
    general_class = get_object(id_=obj.general)
    specific_class = get_object(id_=obj.specific)

    new_generalization = Generalization(general=general_class,
                                        specific=specific_class)

    # Add the new generalization to its domain model
    domain_model.generalizations = domain_model.generalizations | {new_generalization}
    save_object(obj.id, new_generalization)

def create_method(obj: MvMethod, target: HttpUrl) -> Method:
    """Creates a Method"""
    params = {"name": obj.name}

    if obj.isAbstract is not None:
        params["is_abstract"] = obj.isAbstract

    type_ = get_object(id_=obj.elementType, raise_error=False)
    if type_ is None:
        type_ = map_type(obj.elementType)
    params["type"] = type_

    new_method = Method(**params)

    if obj.parameters is not None:
        params = set()
        for param in obj.parameters:
            param_obj = create_parameter(obj=param, target=target)
            params.add(param_obj)
        new_method.parameters = params

    # Add the method to its owner class
    if obj.owner is not None:
        owner = get_object(obj.owner)
        if type(owner).__name__ == "Class":
            owner.methods = owner.methods | {new_method}

    save_object(obj.id, new_method)
    return new_method

def create_parameter(obj: MvParameter, target: HttpUrl) -> Parameter:
    """Creates a parameter"""
    default_value = obj.defaultValue
    type_ = map_type(obj.elementType)
    if type_ is None:
        type_ = get_object(id_=obj["elementType"])

    new_parameter = Parameter(name=obj.name,
                              type=type_,
                              default_value=default_value)

    # Add the parameter to the owner method
    if obj.owner is not None:
        owner = get_object(id_=obj.owner)
        if type(owner).__name__ == "Method":
            owner.parameters = owner.parameters | {new_parameter}

    save_object(obj.id, new_parameter)
    return new_parameter

def create_package(obj: MvPackage, target: HttpUrl) -> None:
    domain_model = get_object(id_=target)
    classes = set()

    for class_id in obj.classes:
        cls = get_object(id_=class_id)
        classes.add(cls)

    new_package = Package(name=obj.name, classes=classes)

    # Add the new method to the class
    domain_model.packages = domain_model.packages | {new_package}
    save_object(obj.id, new_package)

def create_enumeration(obj: MvEnumeration, target: HttpUrl) -> None:
    literals = set()
    for lit in obj.literals:
        enum_literal = EnumerationLiteral(name=lit.name)
        literals.add(enum_literal)
    new_enumeration = Enumeration(name=obj.name, literals=literals)

    # Add the new enumeration to the domain model
    domain_model = get_object(id_=target)
    domain_model.types = domain_model.types | {new_enumeration}
    save_object(obj.id, new_enumeration)

def create_enumeration_literal(obj: MvEnumerationLiteral, target: HttpUrl) -> None:
    domain_model = get_object(id_=target)
    new_literal = EnumerationLiteral(name=obj.name)

    if obj.owner is not None:
        enum = get_object(id_=obj.owner)
        enum.literals = enum.literals | {new_literal}

    save_object(obj.id, new_literal)

def create_grant(obj: MvGrant, target: HttpUrl) -> None:
    save_grant(obj.id, obj)

# Map
type_handlers = {
    "DomainModel": create_domain_model,
    "Class": create_class,
    "Property": create_property,
    "BinaryAssociation": create_bin_association,
    "Generalization": create_generalization,
    "Method": create_method,
    "Parameter": create_parameter,
    "Enumeration": create_enumeration,
    "EnumerationLiteral": create_enumeration_literal,
    "Package": create_package,
    "Grant": create_grant,
}

def generate_id(length=6):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def create(activity: Activity):
    """Creates an object dynamically."""
    obj = activity.object
    obj_type = obj.type
    target = activity.target

    if obj_type != "DomainModel":
        if check_permission(activity) is False:
            raise PermissionError("Permission denied.")

    if obj_type in type_handlers:
        result = type_handlers[obj_type](obj, target)
        create_grant(obj=MvGrant(type="Grant",
                                 id="http://localhost:8000/grants/" + generate_id(),
                                 modelElement=obj.id,
                                 user=activity.actor,
                                 role="admin"
                                 ),
                    target=target)
        return result

    raise ValueError(f"Unknown object type: {obj_type}")
