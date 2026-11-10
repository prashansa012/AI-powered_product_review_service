from app.schemas.product_schema import ProductResponse
from app.models.porduct_model import ProductModel
from sqlalchemy.orm import Session

def product_to_response(db: Session, product: ProductModel) -> ProductResponse:
    return ProductResponse(
        product_id=product.product_id,
        name=product.name,
        category=product.category,
        status = product.status
        
    )