from fastapi import APIRouter
from ..repositories import content

router = APIRouter()

# Get all contents
@router.get("/")
async def get_all():
    return await content.get_all()

