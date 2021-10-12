from fastapi import Depends, APIRouter, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from app.schemas import product_schema, general_schema
from app.usecases.product_service import ProductService as usecase
from app.middlewares import deps, di

router = APIRouter()
local_prefix = "/products/"


class ProductController():

    @router.post("/users/{user_id}"+local_prefix,
                 response_model=product_schema.Product,
                 include_in_schema=True)
    def create_product_for_user(
                user_id: str,
                product: product_schema.ProductCreate,
                db: Session = Depends(deps.get_db)
            ):
        return usecase.create(db=db, product=product, user_id=user_id)

    @router.put(local_prefix+"{product_id}",
                response_model=product_schema.Product,
                include_in_schema=True)
    def update_product(
                product_id: int,
                product: product_schema.ProductCreate,
                db: Session = Depends(deps.get_db)
            ):
        db_product = usecase.read(db, product_id=product_id)
        if db_product is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
        return usecase.update(db=db, product=product, product_id=product_id)

    @router.get(local_prefix,
                response_model=List[product_schema.Product],
                include_in_schema=True)
    def read_products(
                commons: dict = Depends(di.common_parameters),
                db: Session = Depends(deps.get_db)
            ):
        products = usecase.reads(
                db,
                skip=commons['skip'],
                limit=commons['limit']
            )
        return products

    @router.get(local_prefix+"{product_id}",
                response_model=product_schema.Product,
                include_in_schema=True)
    def read_product(product_id: int, db: Session = Depends(deps.get_db)):
        db_product = usecase.read(db, product_id=product_id)
        if db_product is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
        return db_product

    @router.delete(local_prefix,
                   response_model=general_schema.Delete,
                   include_in_schema=True)
    def delete_product(
                product: product_schema.ProductId,
                db: Session = Depends(deps.get_db)
            ):
        db_product = usecase.read(db, product_id=product.id)
        if db_product is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
        usecase.delete(db=db, product_id=product.id)
        return {"id": product.id}
