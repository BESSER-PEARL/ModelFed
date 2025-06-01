from pyecore.ecore import (
    EString, EInteger, EDate,
    EBoolean, EFloat, EClass,
    EPackage, EEnum, EEnumLiteral
)

def map_type(type_str):
    """Parses a string dataType and returns a PrimitiveDataType object"""
    mapping = {
        "int": EInteger,
        "str": EString,
        "date": EDate,
        "datetime": EDate,
        "time": EDate,
        "boolean": EBoolean,
        "float": EFloat,
        "timedelta": EDate,
    }
    return mapping.get(type_str, None)

def parse_multiplicity(multiplicity_str: str) -> list:
    """Parses a string representation of multiplicity and returns a list."""

    if multiplicity_str == "*":
        return [0, -1]

    parts = multiplicity_str.split("..")

    if len(parts) == 1:
        return [int(parts[0]), int(parts[0])]
    else:
        min_val = int(parts[0])
        max_val = (-1) if parts[1] == "*" else int(parts[1])

    return [min_val, max_val]

# Find the class that contains the property
def find_containing_class(package, target_prop):
    for cls in package.eClassifiers:
        if isinstance(cls, EClass) and target_prop in cls.eStructuralFeatures:
            return cls
    for subpackage in package.eSubpackages:
        result = find_containing_class(subpackage, target_prop)
        if result:
            return result
    return None

def remove_supertype(package, eclass_to_remove):
    """Searches in the package and all its subpackages, removing `eclass_to_remove` from `eSuperTypes`."""

    # 1. Remove the reference to the supertype in all classes within the package
    for eclass in package.eClassifiers:
        if isinstance(eclass, EClass) and eclass_to_remove in eclass.eSuperTypes:
            eclass.eSuperTypes.remove(eclass_to_remove)

    # 2. Recursively process subpackages
    for subpackage in package.eSubpackages:
        remove_supertype(subpackage, eclass_to_remove)

def remove_reference(package, reference):
    """Recursively searches through the EPackage and its subpackages to find and remove the EReference."""

    # Iterate through all classifiers in the current package
    for eclass in package.eClassifiers:
        if isinstance(eclass, EClass):
            # If the class has the EReference, remove it
            if reference in eclass.eReferences:
                eclass.eStructuralFeatures.remove(reference)

    # Recursively search in subpackages
    for subpkg in package.eSubpackages:
        remove_reference(subpkg, reference)

def remove_literal(package, literal_to_remove):
    """
    Recursively searches through the package and its subpackages for an EEnum that contains
    the given EEnumLiteral and removes it if found.
    """
    # Check if the package has classifiers (EEnums)
    for classifier in package.eClassifiers:
        if isinstance(classifier, EEnum):
            # If we find an EEnum, check its literals
            if literal_to_remove in classifier.eLiterals:
                classifier.eLiterals.remove(literal_to_remove)
                return True

    # If not found in the current package, check the subpackages
    for subpackage in package.eSubpackages:
        if remove_literal(subpackage, literal_to_remove):
            return True

    return False

def remove_subpackage(base_package, subpackage):
    """
    Recursively searches for the given subpackage inside the base package and removes it if found.
    """
    if subpackage in base_package.eSubpackages:
        base_package.eSubpackages.remove(subpackage)
        return True

    # Recursively search in deeper subpackages
    for subpackage in base_package.eSubpackages:
        if remove_subpackage(subpackage, subpackage):
            return True 

    return False
