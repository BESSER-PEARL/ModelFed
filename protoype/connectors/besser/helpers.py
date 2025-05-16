from besser.BUML.metamodel.structural import (
    StringType, IntegerType, DateTimeType, TimeType,
    BooleanType, FloatType, TimeDeltaType, DateType,
    Multiplicity
)

def map_type(type_str):
    """Parses a string dataType and returns a PrimitiveDataType object"""
    mapping = {
        "int": IntegerType,
        "str": StringType,
        "date": DateType,
        "datetime": DateTimeType,
        "time": TimeType,
        "boolean": BooleanType,
        "float": FloatType,
        "timedelta": TimeDeltaType
    }
    return mapping.get(type_str, None)

def parse_multiplicity(multiplicity_str: str) -> Multiplicity:
    """Parses a string representation of multiplicity and returns a Multiplicity object."""

    if multiplicity_str == "*":
        return Multiplicity(0, "*")

    parts = multiplicity_str.split("..")

    if len(parts) == 1:
        min_val = max_val = int(parts[0])
    else:
        min_val = int(parts[0])
        max_val = parts[1] if parts[1] == "*" else int(parts[1])

    return Multiplicity(min_val, max_val)
