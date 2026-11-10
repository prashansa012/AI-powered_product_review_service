
from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.database.db_manager import engine, Base
from app.api_contoller.routers.product_router import product_router

@asynccontextmanager
async def lifespan(app: FastAPI):

    Base.metadata.create_all(bind=engine)
    print("PostgreSQL database connected successfully!")

    yield

    engine.dispose()
    print("Database connection closed!")


app = FastAPI(lifespan=lifespan)
app.include_router(product_router)
