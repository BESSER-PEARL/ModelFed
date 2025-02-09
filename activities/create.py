from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, BinaryAssociation,
    Multiplicity, Generalization, Method, Parameter,
    Package, Enumeration, EnumerationLiteral
)
from utils import check_permission
from models import Grant
from pydantic import HttpUrl
from storage import save_object, get_object
from models import Activity
from utils import map_type, parse_multiplicity

def create_domain_model(obj: dict, target: HttpUrl, actor: HttpUrl) -> None:
    """Creates a DomainModel from a dictionary object."""
    new_model = DomainModel(name=obj["name"])
    new_model.id = obj["id"]
    
    save_object(new_model)
    create_grant(obj={"model_element": new_model.id, "user": str(actor), "role": "admin"}, 
                 target=target,
                 actor=actor)

def create_class(obj: dict, target: HttpUrl, actor: HttpUrl) -> None:
    """Creates a Class with attributes if provided."""
    is_abstract = obj.get("isAbstract", False)
    is_read_only = obj.get("isReadOnly", False)
    new_class = Class(name=obj["name"],
                      is_abstract=is_abstract,
                      is_read_only=is_read_only)
    new_class.id = obj["id"]

    if "attributes" in obj:
        attrs = set()
        for attr in obj["attributes"]:
            attr_obj = create_property(obj=attr, target=target, actor=actor)
            attrs.add(attr_obj)
        new_class.attributes = attrs

    if "methods" in obj:
        methods = set()
        for method in obj["methods"]:
            method_obj = create_method(obj=method, target=target, actor=actor)
            methods.add(method_obj)
        new_class.methods = methods

    # Add the new class to the domain model
    domain_model = get_object(id_=str(target))
    domain_model.types = domain_model.types | {new_class}
    save_object(new_class)

def create_property(obj: dict, target: HttpUrl, actor: HttpUrl) -> Property:
    """Creates a Property object."""
    is_composite = obj.get("isComposite", False)
    is_navigable = obj.get("isNavigable", True)
    type_ = get_object(id_=obj["elementType"], raise_error=False)
    if type_ is None:
        type_ = map_type(obj["elementType"])
    if "multiplicity" in obj:
        mult = parse_multiplicity(obj["multiplicity"])
    else:
        mult = Multiplicity(1,1)

    new_property = Property(name=obj["name"],
                            type=type_,
                            is_composite=is_composite,
                            is_navigable=is_navigable,
                            multiplicity=mult)
    new_property.id = obj["id"]

    # Add the property to the owner
    if "owner" in obj:
        owner = get_object(obj["owner"], raise_error=False)
        if owner is not None:
            if type(owner).__name__ == "Class":
                owner.attributes = owner.attributes | {new_property}
            elif type(owner).__name__ == "Association" or "BinaryAssociation":
                owner.ends = owner.ends | {new_property}

    save_object(new_property)
    return new_property

def create_bin_association(obj: dict, target: HttpUrl, actor: HttpUrl) -> None:
    """Creates a Binary Association"""
    domain_model = get_object(id_=str(target))
    end1 = obj["ends"][0]
    end2 = obj["ends"][1]

    end1_obj = create_property(obj=end1, target=target, actor=actor)
    end2_obj = create_property(obj=end2, target=target, actor=actor)

    new_association = BinaryAssociation(name=obj["name"],
                                        ends={end1_obj, end2_obj})
    new_association.id = obj["id"]

    # Add the new association to the domain model
    domain_model.associations = domain_model.associations | {new_association}
    save_object(new_association)

def create_generalization(obj: dict, target: HttpUrl, actor: HttpUrl) -> None:
    """Creates a Generalization"""
    domain_model = get_object(id_=str(target))

    general_class = next(
        (class_obj for class_obj in domain_model.get_classes() if class_obj.id == obj["general"]),
        None
    )

    specific_class = next(
        (class_obj for class_obj in domain_model.get_classes() if class_obj.id == obj["specific"]),
        None
    )

    new_generalization = Generalization(general=general_class,
                                        specific=specific_class)
    new_generalization.id = obj["id"]

    # Add the new generalization to the domain model
    domain_model.generalizations = domain_model.generalizations | {new_generalization}
    save_object(new_generalization)

def create_method(obj: dict, target: HttpUrl, actor: HttpUrl) -> Method:
    """Creates a Method"""
    visibility = obj.get("visibility", "public")
    is_abstract = obj.get("isAbstract", False)
    type_ = get_object(id_=obj["elementType"], raise_error=False)
    if type_ is None:
        type_ = map_type(obj["elementType"])

    new_method = Method(name=obj["name"],
                        visibility=visibility,
                        is_abstract=is_abstract,
                        type=type_)
    new_method.id = obj["id"]

    if "parameters" in obj:
        params = set()
        for param in obj["parameters"]:
            param_obj = create_parameter(obj=param, target=target, actor=actor)
            params.add(param_obj)
        new_method.parameters = params

    # Add the method to the owner class
    if "owner" in obj:
        owner = get_object(obj["owner"], raise_error=False)
        if owner is not None:
            if type(owner).__name__ == "Class":
                owner.methods = owner.methods | {new_method}

    save_object(new_method)
    return new_method

def create_parameter(obj: dict, target: HttpUrl, actor: HttpUrl) -> Parameter:
    """Creates a parameter"""
    default_value = obj.get("defaultValue", None)
    type_ = map_type(obj["elementType"])
    if type_ is None:
        type_ = get_object(id_=obj["elementType"])

    new_parameter = Parameter(name=obj["name"],
                              type=type_,
                              default_value=default_value)
    new_parameter.id = obj["id"]

    # Add the parameter to the owner method
    if "owner" in obj:
        owner = get_object(id_=obj["owner"], raise_error=False)
        if owner is not None:
            if type(owner).__name__ == "Method":
                owner.parameters = owner.parameters | {new_parameter}

    save_object(new_parameter)
    return new_parameter

def create_package(obj: dict, target: HttpUrl, actor: HttpUrl) -> None:
    domain_model = get_object(id_=str(target))
    class_ids_set = set(obj.get("classes", []))
    classes = set()

    # Iterate over domain classes and check for matching id
    for class_obj in domain_model.get_classes():
        if class_obj.id in class_ids_set:
            classes.add(class_obj)

    new_package = Package(name=obj["name"], classes=classes)
    new_package.id = obj["id"]

    # Add the new method to the class
    domain_model.packages = domain_model.packages | {new_package}
    save_object(new_package)

def create_enumeration(obj: dict, target: HttpUrl, actor: HttpUrl) -> None:
    literals = set()
    for lit in obj.get("literals", []):
        enum_literal = EnumerationLiteral(name=lit["name"])
        enum_literal.id = lit["id"]
        literals.add(enum_literal)
    new_enumeration = Enumeration(name=obj["name"], literals=literals)
    new_enumeration.id = obj["id"]

    # Add the new enumeration to the domain model
    domain_model = get_object(id_=str(target))
    domain_model.types = domain_model.types | {new_enumeration}
    save_object(new_enumeration)

def create_enumeration_literal(obj: dict, target: HttpUrl, actor: HttpUrl) -> None:
    domain_model = get_object(id_=str(target))
    new_literal = EnumerationLiteral(name=obj["name"])
    new_literal.id = obj["id"]

    if "owner" in obj:
        enum = get_object(id_=obj["owner"])
        enum.literals = enum.literals | {new_literal}
    
    save_object(new_literal)

def create_grant(obj: dict, target: HttpUrl, actor: HttpUrl) -> None:
    model_element = get_object(id_=obj["model_element"])
    grant = Grant(user=obj["user"], role=obj["role"])
    model_element.grants.add(grant)

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

def create(activity: Activity):
    """Creates an object dynamically."""
    obj = activity.object
    obj_type = obj.get("type")
    target = activity.target
    actor = activity.actor

    if obj_type != "DomainModel":
        if check_permission(activity) is False:
            raise PermissionError("Permission denied.")

    if obj_type in type_handlers:
        return type_handlers[obj_type](obj, target, actor)

    raise ValueError(f"Unknown object type: {obj_type}")
