from fastapi import APIRouter


Router = APIRouter(
    prefix='/graph',
    tags=["Graph Operations"],
)


@Router.post("/heatmap")
async def heatmap():
    return {"heatmap": "feature correlation graph"}


@Router.post("/crosstabs")
async def crosstabs():
    return {"crosstabs": "feature comparison graph"}
