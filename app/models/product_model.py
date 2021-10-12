from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from config.database import Base
from app.utils.datatype import SqliteNumeric
Numeric = SqliteNumeric


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    product_code = Column(String(100), index=True)
    description = Column(String(100))
    price = Column(Numeric(13, 2), default=0.00)
    owner_id = Column(String(100), ForeignKey("users.id"))

    owner = relationship("User", back_populates="products")
