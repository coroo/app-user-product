from sqlalchemy.orm import Session

from app.interfaces.api_interfaces import ServiceInterface
from app.repositories.product_repository import ProductRepository as repository
from app.schemas import product_schema as schema

from app.utils.attribute import rsetattr, rgetattr


class ProductService(ServiceInterface):

    def reads(db: Session, skip: int = 0, limit: int = 100):
        return repository.reads(db, skip=skip, limit=limit)

    def read(db: Session, product_id: int):
        product = repository.read(db, product_id=product_id)
        if product is not None:
            rsetattr(product, 'authors', {"name": "Kuncoro Wicaksono"})
            rgetattr(product, 'authors.name', "Kuncoro Wicaksono")
        return product

    def create(db: Session,
               product: schema.ProductCreate,
               user_id: int):
        return repository.create(
            db=db,
            product=product,
            user_id=user_id)

    def update(db: Session, product: schema.ProductCreate, product_id: int):
        return repository.update(db=db, product=product, product_id=product_id)

    def delete(db: Session, product_id: str):
        return repository.delete(db=db, product_id=product_id)
