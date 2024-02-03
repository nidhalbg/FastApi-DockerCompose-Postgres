from fastapi import APIRouter
from ..repositories import firmware

router = APIRouter()

# get all firmwares
@router.get("/")
async def get_all():
    return await firmware.get_all()