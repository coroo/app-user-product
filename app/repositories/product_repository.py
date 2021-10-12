from sqlalchemy.orm import Session

from app.interfaces.api_interfaces import RepositoryInterface
from app.models import product_model
from app.schemas import product_schema


class ProductRepository(RepositoryInterface):

    def reads(db: Session, skip: int = 0, limit: int = 100):
        return db.query(
            product_model.Product
        ).offset(skip).limit(limit).all()

    def read(db: Session, product_id: int):
        return db.query(
            product_model.Product
        ).filter(product_model.Product.id == product_id).first()

    def create(
            db: Session,
            product: product_schema.ProductCreate,
            user_id: str):
        db_product = product_model.Product(**product.dict(), owner_id=user_id)
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return db_product

    def update(db: Session, product: product_schema.ProductCreate, product_id: int):
        db.query(
            product_model.Product
        ).filter(
            product_model.Product.id == product_id
        ).update({
            product_model.Product.title: product.title,
            product_model.Product.description: product.description,
        })

        db.commit()
        return db.query(
            product_model.Product
        ).filter(product_model.Product.id == product_id).first()

    def delete(db: Session, product_id: int):
        # use this one for hard delete:
        db.query(
            product_model.Product
        ).filter(product_model.Product.id == product_id).delete()
        db.commit()
        return True
