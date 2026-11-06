from fastapi import APIRouter

router = APIRouter(prefix="/releases", tags=["releases"])


@router.get("/")
async def list_releases():
    return {"releases": []}
