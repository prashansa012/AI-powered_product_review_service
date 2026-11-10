from app.database.db_manager import Base
from sqlalchemy import String, Text, DateTime, Integer, Enum
from sqlalchemy.orm import Mapped, mapped_column

class ProductModel(Base):
    __tablename__ = "products"
    product_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    name: Mapped[str]= mapped_column(
        String(20), nullable=False
    )
    category: Mapped[str] = mapped_column(
        String(25), nullable=False
    )
    status: Mapped[str]= mapped_column(
        String(10),nullable=False, default='new'
    )
