from fastapi import APIRouter, HTTPException, Request
from ..repositories import apparaisor, batch

router = APIRouter()


@router.get("/")
async def get_all():
    return await batch.get_all()

# update all appraisors firmware by batch
@router.put("/{batch_id}/update-firmware")
async def update_firmware_for_batch(batch_id: int, request: Request):
    appraisors = await apparaisor.get_all_appraisors_by_batch_id(batch_id)
    request_body = await request.json()
    firmware_version = request_body.get("firmware_version")
    for appraisor in appraisors:
        await apparaisor.update_installed_firmware(appraisor.id, firmware_version)

    return {"message": "Firmware update initiated for the batch"}
