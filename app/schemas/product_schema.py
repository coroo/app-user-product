from typing import Optional
from pydantic import BaseModel


class ProductBase(BaseModel):
    product_code: str
    description: Optional[str] = None
    price: Optional[int] = None


class ProductId(BaseModel):
    id: int


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    owner_id: str

    class Config:
        orm_mode = True
