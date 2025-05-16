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
ProductPassport = Class(name="ProductPassport")
Hazard = Class(name="Hazard")
RecycledMaterial = Class(name="RecycledMaterial")
ChemicalProp = Class(name="ChemicalProp")
LifecycleStage = Class(name="LifecycleStage")
Design = Class(name="Design")
Manufacture = Class(name="Manufacture")
Use = Class(name="Use")
Collect = Class(name="Collect")
Recycle = Class(name="Recycle")
Reparation = Class(name="Reparation")
Distribution = Class(name="Distribution")

# ProductPassport class attributes and methods
ProductPassport_name: Property = Property(name="name", type=StringType)
ProductPassport_code: Property = Property(name="code", type=StringType)
ProductPassport_UID: Property = Property(name="UID", type=StringType)
ProductPassport.attributes={ProductPassport_UID, ProductPassport_code, ProductPassport_name}

# Hazard class attributes and methods
Hazard_very_high: Property = Property(name="very_high", type=BooleanType)
Hazard_exed_limit: Property = Property(name="exed_limit", type=BooleanType)
Hazard.attributes={Hazard_exed_limit, Hazard_very_high}

# RecycledMaterial class attributes and methods
RecycledMaterial_preconsumer: Property = Property(name="preconsumer", type=StringType)
RecycledMaterial_postconsumer: Property = Property(name="postconsumer", type=StringType)
RecycledMaterial_renewable: Property = Property(name="renewable", type=StringType)
RecycledMaterial.attributes={RecycledMaterial_renewable, RecycledMaterial_preconsumer, RecycledMaterial_postconsumer}

# ChemicalProp class attributes and methods
ChemicalProp_threshold: Property = Property(name="threshold", type=FloatType)
ChemicalProp_disclosure: Property = Property(name="disclosure", type=StringType)
ChemicalProp_composition: Property = Property(name="composition", type=StringType)
ChemicalProp.attributes={ChemicalProp_composition, ChemicalProp_threshold, ChemicalProp_disclosure}

# LifecycleStage class attributes and methods
LifecycleStage_name: Property = Property(name="name", type=StringType)
LifecycleStage_start: Property = Property(name="start", type=DateType)
LifecycleStage_end: Property = Property(name="end", type=DateType)
LifecycleStage.attributes={LifecycleStage_start, LifecycleStage_end, LifecycleStage_name}

# Design class attributes and methods

# Manufacture class attributes and methods

# Use class attributes and methods

# Collect class attributes and methods

# Recycle class attributes and methods

# Reparation class attributes and methods
Reparation_description: Property = Property(name="description", type=StringType)
Reparation_date_set: Property = Property(name="date_set", type=DateType)
Reparation.attributes={Reparation_description, Reparation_date_set}

# Distribution class attributes and methods

# Relationships
HazardToProductPassport: BinaryAssociation = BinaryAssociation(
    name="HazardToProductPassport",
    ends={
        Property(name="hazard", type=Hazard, multiplicity=Multiplicity(1, 1)),
        Property(name="product_passport", type=ProductPassport, multiplicity=Multiplicity(0, 9999))
    }
)
RecycledMaterialToProductPassport: BinaryAssociation = BinaryAssociation(
    name="RecycledMaterialToProductPassport",
    ends={
        Property(name="recycled_material", type=RecycledMaterial, multiplicity=Multiplicity(1, 1)),
        Property(name="product_passport", type=ProductPassport, multiplicity=Multiplicity(0, 9999))
    }
)
ChemicalPropToProductPassport: BinaryAssociation = BinaryAssociation(
    name="ChemicalPropToProductPassport",
    ends={
        Property(name="chemical_prop", type=ChemicalProp, multiplicity=Multiplicity(1, 1)),
        Property(name="product_passport", type=ProductPassport, multiplicity=Multiplicity(0, 9999))
    }
)
LifecycleStageToProductPassport: BinaryAssociation = BinaryAssociation(
    name="LifecycleStageToProductPassport",
    ends={
        Property(name="lifecycle_stage", type=LifecycleStage, multiplicity=Multiplicity(0, 9999)),
        Property(name="product_passport", type=ProductPassport, multiplicity=Multiplicity(1, 1))
    }
)
UseToReparation: BinaryAssociation = BinaryAssociation(
    name="UseToReparation",
    ends={
        Property(name="use", type=Use, multiplicity=Multiplicity(1, 1)),
        Property(name="reparation", type=Reparation, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_Design_LifecycleStage = Generalization(general=LifecycleStage, specific=Design)
gen_Manufacture_LifecycleStage = Generalization(general=LifecycleStage, specific=Manufacture)
gen_Distribution_LifecycleStage = Generalization(general=LifecycleStage, specific=Distribution)
gen_Use_LifecycleStage = Generalization(general=LifecycleStage, specific=Use)
gen_Recycle_LifecycleStage = Generalization(general=LifecycleStage, specific=Recycle)
gen_Collect_LifecycleStage = Generalization(general=LifecycleStage, specific=Collect)

# Domain Model
domain_model = DomainModel(
    name="Digital_Product_Passport",
    types={ProductPassport, Hazard, RecycledMaterial, ChemicalProp, LifecycleStage, Design, Manufacture, Use, Collect, Recycle, Reparation, Distribution},
    associations={HazardToProductPassport, RecycledMaterialToProductPassport, ChemicalPropToProductPassport, LifecycleStageToProductPassport, UseToReparation},
    generalizations={gen_Design_LifecycleStage, gen_Manufacture_LifecycleStage, gen_Distribution_LifecycleStage, gen_Use_LifecycleStage, gen_Recycle_LifecycleStage, gen_Collect_LifecycleStage}
)
