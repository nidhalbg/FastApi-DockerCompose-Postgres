from app.db import contents, database


async def get_all():
    query = contents.select()
    return await database.fetch_all(query=query)


async def get_one(id):
    query = contents.select().where(id == contents.c.id)
    return await database.fetch_one(query=query)
