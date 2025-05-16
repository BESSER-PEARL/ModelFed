# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint
)

# Enumerations
# Classes
Pet = Class(name="Pet")
Person = Class(name="Person")

# Pet class attributes and methods

# Person class attributes and methods
Person_name: Property = Property(name="name", type=StringType)
Person_age: Property = Property(name="age", type=IntegerType)
Person.attributes={Person_name, Person_age}

# Relationships
relationship: BinaryAssociation = BinaryAssociation(
    name="relationship",
    ends={
        Property(name="person", type=Person, multiplicity=Multiplicity(1, 1)),
        Property(name="pets", type=Pet, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="MyModel",
    types={Pet, Person},
    associations={relationship},
    generalizations={}
)
