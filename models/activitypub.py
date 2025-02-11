from pydantic import BaseModel, HttpUrl, Field
from typing import Optional, Union, List

class Object(BaseModel):
    context: List[HttpUrl] = Field(
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
    content: Optional[str] = None
    context: Optional[HttpUrl] = None

    class Config:
        fields = {
            'context': '@context'
        }

class Activity(Object):
    actor: HttpUrl
    #object: Union[Object, dict]
    object: Object
    target: Optional[HttpUrl]
