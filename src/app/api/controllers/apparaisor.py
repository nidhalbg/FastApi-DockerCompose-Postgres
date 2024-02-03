from fastapi import HTTPException
from ..repositories import apparaisor, batch


async def get_appraiser_and_batch(appraiser_id: int):
    appraiser = await apparaisor.get_one(appraiser_id)

    if appraiser is None:
        raise HTTPException(status_code=404, detail="Appraiser not found")

    appraiser_batch = await batch.get_one(appraiser.batch_id)

    return appraiser, appraiser_batch


async def validate_and_install_firmware(appraiser_batch, firmware_version, appraiser_id):
    if firmware_version is None:
        return {"error": "firmware_version is missing in the request body"}

    await validate_firmware(appraiser_batch, firmware_version)

    await apparaisor.update_installed_firmware(appraiser_id, firmware_version)

    return {"message": "Firmware installed successfully"}


async def validate_firmware(appraiser_batch, firmware_version):
    if firmware_version not in appraiser_batch.firmware:
        raise HTTPException(
            status_code=400, detail="Firmware not compatible with Appraiser hardware")