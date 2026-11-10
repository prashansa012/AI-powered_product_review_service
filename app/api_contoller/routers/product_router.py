from fastapi import APIRouter, status, Depends
from app.schemas.product_schema import ProductResponse, Product
# from app.models.porduct_model import ProductModel
from sqlalchemy.orm import Session
from app.database.db_manager import get_db
from app.services.product_service import post_product, get_products, get_product_by_id


product_router = APIRouter()

@product_router.post("/products", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product_endpoint(product_data: Product,
    db: Session = Depends(get_db)):
    return post_product(product_data,db)

@product_router.get("/products", response_model=list[ProductResponse], status_code=status.HTTP_200_OK)
def show_product_endpoint( db:Session = Depends(get_db)):
    return get_products(db)

@product_router.get(
    "/products/{product_id}",
    response_model=ProductResponse,
    status_code=status.HTTP_200_OK,
)
def get_product_by_id_endpoint(
    product_id: int,
    db: Session = Depends(get_db),
):
    return get_product_by_id(db, product_id)