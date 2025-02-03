from models import Activity
from storage import save_model, get_model, get_domain_models
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, PrimitiveDataType, StringType,
    BinaryAssociation, Multiplicity, Generalization, Method,
    Parameter, IntegerType, Package, Enumeration, EnumerationLiteral
)

def create_domain_model(object: dict) -> None:
    """Creates a DomainModel from a dictionary object."""
    new_model = DomainModel(name=object["name"])
    new_model.id = object["id"]
    new_model.attributed_to = object["attributedTo"]
    new_model.users = object.get("users", [])
    save_model(id=new_model.id, domain_model=new_model)

def create_class(object: dict) -> None:
    """Creates a Class with attributes if provided."""
    is_abstract = object.get("isAbstract", False)
    is_read_only = object.get("isReadOnly", False)
    new_class = Class(name=object["name"],
                      is_abstract=is_abstract,
                      is_read_only=is_read_only)
    new_class.id = object["id"]

    # Add attributes if present
    '''if "attributes" in object and object["attributes"]:
        new_class.attributes = {
            Property(name=attr["name"], type=PrimitiveDataType(attr["elementType"]), id=attr["id"])
            for attr in object["attributes"]
        }'''
    
    # Add the new class to the domain model
    domain_model = get_model(id=object["context"])
    domain_model.types = domain_model.types | {new_class}
    return new_class

def create_property(object: dict) -> None:
    """Creates a Property with a StringType by default."""
    new_property = Property(name=object["name"], type=StringType)
    new_property.id = object["id"]
    for model in get_domain_models().values():
        for class_obj in model.types:
            if class_obj.id == object["owner"]:
                class_obj.attributes = class_obj.attributes | {new_property}
                break

def create_bin_association(object: dict) -> None:
    """Creates a Binary Association"""
    domain_model = get_model(id=object["context"])
    end1 = object["ends"][0]
    end2 = object["ends"][1]
    composition1 = end1.get("isComposite", False)
    composition2 = end2.get("isComposite", False)
    navigability1 = end1.get("isNavigable", False)
    navigability2 = end2.get("isNavigable", False)

    class1 = next(
        (class_obj for class_obj in domain_model.get_classes() if class_obj.id == end1["elementType"]),
        None
    )

    class2 = next(
        (class_obj for class_obj in domain_model.get_classes() if class_obj.id == end2["elementType"]),
        None
    )

    new_end1 = Property(name=end1["name"],
                    type=class1,
                    is_composite=composition1,
                    is_navigable=navigability1,
                    multiplicity=Multiplicity(end1["multiplicity"]["minMultiplicity"],
                                                end1["multiplicity"]["maxMultiplicity"]))
    new_end1.id = end1["id"]

    new_end2 = Property(name=end2["name"],
                    type=class2,
                    is_composite=composition2,
                    is_navigable=navigability2,
                    multiplicity=Multiplicity(end2["multiplicity"]["minMultiplicity"],
                                                end2["multiplicity"]["maxMultiplicity"]))
    new_end2.id = end2["id"]

    new_association = BinaryAssociation(name=object["name"],
                                        ends={new_end1, new_end2})
    new_association.id = object["id"]

    # Add the new association to the domain model
    domain_model.associations = domain_model.associations | {new_association}

def create_generalization(object: dict) -> None:
    """Creates a Generalization"""
    domain_model = get_model(id=object["context"])

    general_class = next(
        (class_obj for class_obj in domain_model.get_classes() if class_obj.id == object["general"]),
        None
    )

    specific_class = next(
        (class_obj for class_obj in domain_model.get_classes() if class_obj.id == object["specific"]),
        None
    )

    new_generalization = Generalization(general=general_class,
                                        specific=specific_class)
    new_generalization.id = object["id"]

    # Add the new generalization to the domain model
    domain_model.generalizations = domain_model.generalizations | {new_generalization}

def create_method(object: dict) -> None:
    """Creates a Method"""
    domain_model = get_model(id=object["context"])
    owner_class = next(
        (class_obj for class_obj in domain_model.get_classes() if class_obj.id == object["owner"]),
        None
    )

    visibility = object.get("visibility", "public")
    is_abstract = object.get("isAbstract", False)
    navigability1 = object.get("isNavigable", False)
    navigability2 = object.get("isNavigable", False)
    new_method = Method(name=object["name"],
                        visibility=visibility,
                        is_abstract=is_abstract,
                        type=StringType,
                        owner=owner_class)
    new_method.id = object["id"]

    # Add the new method to the class
    owner_class.methods = owner_class.methods | {new_method}

def create_parameter(object: dict) -> None:
    domain_model = get_model(id=object["context"])
    owner_method = None

    for class_object in domain_model.get_classes():
        for method in class_object.methods:
            if method.id == object["owner"]:
                owner_method = method
                break
        if owner_method:
            break

    new_parameter = Parameter(name=object["name"],
                              type=IntegerType,
                              default_value=object["defaultValue"])
    new_parameter.id = object["id"]

    # Add the new method to the class
    owner_method.parameters = owner_method.parameters | {new_parameter}

def create_package(object: dict) -> None:
    domain_model = get_model(id=object["context"])
    class_ids_set = set(object.get("classes", []))
    classes = set()

    # Iterate over domain classes and check for matching id
    for class_obj in domain_model.get_classes():
        if class_obj.id in class_ids_set:
            classes.add(class_obj)

    new_package = Package(name=object["name"], classes=classes)
    new_package.id = object["id"]
    
    # Add the new method to the class
    domain_model.packages = domain_model.packages | {new_package}

def create_enumeration(object: dict) -> None:
    literals = set()
    for lit in object.get("literals", []):
        enum_literal = EnumerationLiteral(name=lit["name"])
        enum_literal.id = lit["id"]
        literals.add(enum_literal)
    new_enumeration = Enumeration(name=object["name"], literals=literals)
    new_enumeration.id = object["id"]

    # Add the new enumeration to the domain model
    domain_model = get_model(id=object["context"])
    domain_model.types = domain_model.types | {new_enumeration}

# Mapeo de tipos a funciones
type_handlers = {
    "DomainModel": create_domain_model,
    "Class": create_class,
    "Property": create_property,
    "BinaryAssociation": create_bin_association,
    "Generalization": create_generalization,
    "Method": create_method,
    "Parameter": create_parameter,
    "Enumeration": create_enumeration,
    "Package": create_package,
}

def create(object: dict):
    """Creates an object (DomainModel, Class, or Property) dynamically."""
    obj_type = object.get("type")

    if obj_type in type_handlers:
        return type_handlers[obj_type](object)

    raise ValueError(f"Unknown object type: {obj_type}")
