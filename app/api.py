from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import (record_router,
                         collection_router,
                         graph_router,
                         model_router)

API = FastAPI(
    title="Prototype Iota - Starter",
    version="0.0.1",
    docs_url="/",
)
API.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@API.post("/info", tags=["General Operations"])
async def info():
    return {"info": "API Information"}


for router in (record_router, collection_router, graph_router, model_router):
    API.include_router(router.Router)

