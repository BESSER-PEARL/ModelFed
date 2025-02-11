from typing import Optional, Union, List, Any, Literal
from datetime import datetime
from pydantic import BaseModel, HttpUrl, Field

class Object(BaseModel):
    context: Union[HttpUrl, List[HttpUrl]] = Field(
        default=[
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        alias="@context"
    )
    name: Optional[str] = None
    type: str
    id: HttpUrl
    to: Optional[List[HttpUrl]] = None

    class Config:
        fields = {
            'context': '@context'
        }

class MvDomainModel(Object):
    types: Optional[List[Union[Object, HttpUrl]]]
    packages: Optional[List[Union[Object, HttpUrl]]] = None
    associations: Optional[List[Union[Object, HttpUrl]]] = None
    generalizations: Optional[List[Union[Object, HttpUrl]]] = None

class MvModelElement(Object):
    visibility: Optional[str] = None

class MvType(MvModelElement):
    pass

class MvDataType(MvType):
    pass

class MvPrimitiveDataType(MvDataType):
    pass

class MvTypedElement(MvModelElement):
    elementType: Union[
        MvType,
        HttpUrl,
        Literal[
            'str', 
            'int', 
            'float', 
            'boolean', 
            'date', 
            'time', 
            'datetime', 
            'timedelta'
        ]
    ] = None

class MvEnumerationLiteral(MvModelElement):
    value: Optional[str] = None
    owner: Optional[HttpUrl] = None

class MvEnumeration(MvDataType):
    literals: Optional[List[Union[MvEnumerationLiteral, HttpUrl]]] = None

class MvParameter(MvTypedElement):
    defaultValue: Optional[Any] = None
    owner: Optional[HttpUrl] = None

class MvMethod(MvTypedElement):
    parameters: Optional[List[Union[MvParameter, HttpUrl]]] = None
    code: Optional[str] = None
    owner: Optional[HttpUrl] = None
    isAbstract: Optional[bool] = None

class MvProperty(MvTypedElement):
    owner: Optional[HttpUrl] = None
    multiplicity: Optional[str] = None
    isComposite: Optional[bool] = None
    isNavigable: Optional[bool] = None
    isId: Optional[bool] = None

class MvClass(MvType):
    attributes: Optional[List[Union[MvProperty, HttpUrl]]] = None
    methods: Optional[List[Union[MvMethod, HttpUrl]]] = None
    isAbstract: Optional[bool] = None

class MvPackage(MvModelElement):
    classes: Optional[List[Union[MvClass, HttpUrl]]] = None

class MvAssociation(MvModelElement):
    ends: Optional[List[Union[MvProperty, HttpUrl]]] = None

class MvBinaryAssociation(MvAssociation):
    pass

class MvGeneralization(MvModelElement):
    general: Optional[Union[MvClass, HttpUrl]] = None
    specific: Optional[Union[MvClass, HttpUrl]] = None
    isDisjoint: Optional[bool] = None
    isComplete: Optional[bool] = None

class MvGrant(Object):
    modelElement: HttpUrl
    user: HttpUrl
    role: Literal[
            'writer', 
            'admin', 
            'read', 
            'maintainer'
        ]

# Mapping of type to Pydantic classes
object_type_map = {
    "Class": MvClass,
    "PrimitiveDataType": MvPrimitiveDataType,
    "EnumerationLiteral": MvEnumerationLiteral,
    "Enumeration": MvEnumeration,
    "Parameter": MvParameter,
    "Method": MvMethod,
    "Property": MvProperty,
    "Package": MvPackage,
    "Association": MvAssociation,
    "BinaryAssociation": MvBinaryAssociation,
    "Generalization": MvGeneralization,
    "Grant": MvGrant,
}

class Activity(Object):
    actor: HttpUrl
    object: Union[Object, HttpUrl]
    target: Optional[HttpUrl] = None
    timestamp: datetime

    def __init__(self, **data):
        obj_data = data.get("object")

        if isinstance(obj_data, str) and obj_data.startswith("http"):
            data["object"] = HttpUrl(obj_data)
        elif isinstance(obj_data, dict):  
            obj_type = obj_data.get("type")
            if obj_type in object_type_map:
                data["object"] = object_type_map[obj_type](**obj_data)
            else:
                data["object"] = Object(**obj_data)

        super().__init__(**data)
