from pydantic import BaseModel, HttpUrl
from typing import Optional, Union, List

class Object(BaseModel):
    name: Optional[str] = None
    type: str
    id: HttpUrl
    attributedTo: Optional[HttpUrl] = None
    content: Optional[str] = None
    context: Optional[HttpUrl] = None

class Activity(BaseModel):
    context: str = "https://www.w3.org/ns/activitystreams"
    type: str
    id: HttpUrl
    to: Optional[List[HttpUrl]] = None
    actor: HttpUrl
    object: Union[Object, dict] 

    class Config:
        fields = {
            'context': '@context'
        }
