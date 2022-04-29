from typing import Optional

from pydantic import BaseModel, Field

#// https://sqlmodel.tiangolo.com/#create-a-sqlmodel-model
class Hero(BaseModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None