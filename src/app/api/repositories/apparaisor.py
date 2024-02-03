from app.db import appraisors, database


async def get_all():
    query = appraisors.select()
    return await database.fetch_all(query=query)


async def get_one(appraiser_id):
    query = appraisors.select().where(appraiser_id == appraisors.c.id)
    return await database.fetch_one(query=query)


async def update_installed_firmware(appraiser_id, installed_firmware):
    query = (
        appraisors
        .update()
        .where(appraiser_id == appraisors.c.id)
        .values(installed_firmware=installed_firmware)
        .returning(appraisors.c.id)
    )
    return await database.execute(query=query)


async def get_all_appraisors_by_batch_id(batch_id):
    query = appraisors.select().where(batch_id == appraisors.c.batch_id)
    return await database.fetch_all(query=query)
