from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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


@API.post("/info")
async def info():
    return {"info": "API Information"}


@API.post("/create")
async def create():
    return {"create": "insert new record"}


@API.post("/read")
async def read():
    return {"read": "read record by id"}


@API.post("/update")
async def update():
    return {"update": "updates an existing record"}


@API.post("/delete")
async def delete():
    return {"delete": "delete record by id"}


@API.post("/find")
async def find():
    return {"find": "find records by query"}


@API.post("/reseed")
async def reseed():
    return {"reseed": "reseeds the database"}


@API.post("/retrain")
async def retrain():
    return {"retrain": "retrains the model"}


@API.post("/predict")
async def predict():
    return {"predict": "calculates a prediction based on input"}


@API.post("/heatmap")
async def heatmap():
    return {"heatmap": "feature correlation graph"}


@API.post("/crosstabs")
async def crosstabs():
    return {"crosstabs": "feature comparison graph"}
