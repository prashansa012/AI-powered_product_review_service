from fastapi import HTTPException, status
from app.models.porduct_model import ProductModel
from app.schemas.product_schema import Product
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError



def create_product( product_data: Product,db: Session):
    try:
        product = ProductModel(
            name=product_data.name,
            category=product_data.category,
        )
        db.add(product)
        db.commit()
        db.refresh(product)
        return product
    except SQLAlchemyError as exc:
        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create product due to a database error.",
        ) from exc

def show_all_products( db: Session):
        
        return db.query(ProductModel).all()

def show_product_by_id(db:Session,product_id:int):
    try:
        product = (
                db.query(ProductModel)
                .filter(ProductModel.product_id == product_id)
                .first()
            )
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Ticket with ID {product_id} not found.",
            )
        return product
    except SQLAlchemyError as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve the product due to a database error.",
        ) from exc

