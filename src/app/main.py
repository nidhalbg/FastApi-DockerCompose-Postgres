from fastapi import FastAPI


from app.api.services import apparaisor, batch, content, firmware
from app.db import engine, metadata, database

metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(apparaisor.router, prefix="/apparaisors", tags=["apparaisors"])
app.include_router(batch.router, prefix="/batchs", tags=["batchs"])
app.include_router(content.router, prefix="/contents", tags=["contents"])
app.include_router(firmware.router, prefix="/firmwares", tags=["firmwares"])
