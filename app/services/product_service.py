from app.repositories.product_repo import create_product, show_all_products, show_product_by_id
from app.services.product_mapper import product_to_response
from app.schemas.product_schema import Product
from sqlalchemy.orm import Session

def post_product(product_data:Product,db:Session):
    product= create_product(product_data,db)
    return product_to_response(db, product)

def get_products( db:Session):
    products = show_all_products( db)
    return [
        product_to_response(db, product)
        for product in products
    ]

def get_product_by_id(db:Session,id: int):
    product = show_product_by_id(db, id)
    return product_to_response(db,product)
