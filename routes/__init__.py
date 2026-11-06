"""HTTP-маршруты и обработчики запросов."""
from fastapi import APIRouter
from .release import router as release_router

router = APIRouter()
router.include_router(release_router)
