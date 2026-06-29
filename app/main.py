from fastapi import FastAPI
from app.core.database.database import Base, engine
from app.routers.link import link_router

app = FastAPI()

app.include_router(link_router)

Base.metadata.create_all(bind=engine)