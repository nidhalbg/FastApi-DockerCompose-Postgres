from app.db import firmwares, database


async def get_all():
    query = firmwares.select()
    return await database.fetch_all(query=query)


async def get_one(id):
    query = firmwares.select().where(id == firmwares.c.id)
    return await database.fetch_one(query=query)
