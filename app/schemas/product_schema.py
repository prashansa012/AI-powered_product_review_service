from typing import Annotated
from pydantic import BaseModel, Field, ConfigDict

class Product(BaseModel):
    name: str
    category:str

class ProductResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    product_id:int
    name:str
    category:str
    status:str
