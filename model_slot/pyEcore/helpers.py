from pyecore.ecore import (
    EString, EInteger, EDate,
    EBoolean, EFloat
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
