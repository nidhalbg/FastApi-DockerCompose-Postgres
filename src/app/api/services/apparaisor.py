from fastapi import APIRouter, HTTPException, Request
from ..repositories import apparaisor
from ..controllers.apparaisor import get_appraiser_and_batch, validate_and_install_firmware

router = APIRouter()


# get all Appraisors
@router.get("/")
async def get_all():
    return await apparaisor.get_all()


# get one appraisor
@router.get("/{appraiser_id}")
async def get_appraiser_profile(appraiser_id: int):
    appraiser = await apparaisor.get_one(appraiser_id)
    if appraiser is None:
        raise HTTPException(status_code=404, detail="Appraiser not found")
    return {"profile": appraiser}


@router.put("/{appraiser_id}/install-firmware")
async def install_firmware(appraiser_id: int, request: Request):
    appraiser, appraiser_batch = await get_appraiser_and_batch(appraiser_id)
    request_body = await request.json()
    firmware_version = request_body.get("firmware_version")

    return await validate_and_install_firmware(appraiser_batch, firmware_version, appraiser_id)
