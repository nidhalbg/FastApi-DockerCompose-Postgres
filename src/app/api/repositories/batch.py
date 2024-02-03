from app.db import batches, database


async def get_all():
    query = batches.select()
    return await database.fetch_all(query=query)


async def get_one(id):
    query = batches.select().where(id == batches.c.id)
    return await database.fetch_one(query=query)
