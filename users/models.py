from typing import List
from pydantic import BaseModel

class OfertasHistory(BaseModel):
    history: List[str]

class User(BaseModel):
    userid: str
    name: str
