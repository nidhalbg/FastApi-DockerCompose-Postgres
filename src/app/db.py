import os

from sqlalchemy import (Column, DateTime, Integer, MetaData, String,
                        Table, Boolean, ForeignKey, create_engine)
from sqlalchemy.sql import func

from databases import Database

DATABASE_URL = os.getenv("DATABASE_URL")

def drop_all_tables():
    metadata.drop_all(bind=engine)

# SQLAlchemy
engine = create_engine(DATABASE_URL)
metadata = MetaData()
drop_all_tables()


batches = Table(
    "batches",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(255)),
    Column("firmware", String(50)),
    Column("compatible_hardware", String(255)),
    Column("created_at", DateTime, default=func.now()),
    Column("modified_at", DateTime, default=func.now()),
    Column("firmware_id", Integer, ForeignKey("firmwares.id"))
)

contents = Table(
    "contents",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(255)),
    Column("url", String(255)),
    Column("mandatory", Boolean),
    Column("min_version", String(255)),
    Column("max_version", String(255)),
    Column("created_at", DateTime, default=func.now()),
    Column("modified_at", DateTime, default=func.now())
)

firmwares = Table(
    "firmwares",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("version", String(255)),
    Column("url", String(255)),
    Column("compatible_hardware", String(255)),
    Column("created_at", DateTime, default=func.now()),
    Column("modified_at", DateTime, default=func.now())
)

appraisor_content = Table(
    "appraisor_content",
    metadata,
    Column("appraisor_id", Integer, ForeignKey("appraisors.id"), primary_key=True),
    Column("content_id", Integer, ForeignKey("contents.id"), primary_key=True),
)


appraisors = Table(
    "appraisors",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("nickname", String(255)),
    Column("mac", String(17)),
    Column("last_connection", DateTime, default=func.now()),
    Column("installed_firmware", String(255)),
    Column("hardware", String(50)),
    Column("created_at", DateTime, default=func.now()),
    Column("modified_at", DateTime, default=func.now()),
    Column("batch_id", Integer, ForeignKey("batches.id"))
)


# databases query builder
database = Database(DATABASE_URL)


# Création des tables dans la base de données
metadata.create_all(engine)

#
# #Insertion de données de test dans les tables
# with engine.connect() as connection:
#     # Insertion dans la table "batches"
#     connection.execute(batches.insert(), [
#         {"name": "Batch1", "firmware": "1.0.0", "compatible_hardware": "Hardware 1, Hardware 2", "firmware_id": 1},
#         {"name": "Batch2", "firmware": "1.1.0", "compatible_hardware": "Hardware 2", "firmware_id": 2},
#     ])
#
#     # Insertion dans la table "firmwares"
#     connection.execute(firmwares.insert(), [
#         {"version": "1.0.0", "url": "https://example.com/firmware1", "compatible_hardware": "Hardware 1, Hardware 2"},
#         {"version": "1.1.0", "url": "https://example.com/firmware2", "compatible_hardware": "Hardware 2"},
#     ])
#
#     # Insertion dans la table "contents"
#     connection.execute(contents.insert(), [
#         {"name": "Content1", "url": "https://example.com/content1", "mandatory": True, "min_version": "1.0.0", "max_version": "2.0.0"},
#         {"name": "Content2", "url": "https://example.com/content2", "mandatory": False, "min_version": "1.1.0", "max_version": "2.0.0"},
#     ])
#
#     # Insertion dans la table "appraisors"
#     connection.execute(appraisors.insert(), [
#         {"nickname": "Drone1", "mac": "00:11:22:33:44:55", "installed_firmware": "1.0.0", "hardware": "Hardware 1", "batch_id": 1},
#         {"nickname": "Drone2", "mac": "11:22:33:44:55:66", "installed_firmware": "1.1.0", "hardware": "Hardware 2", "batch_id": 2},
#     ])
#
#     # Insertion dans la table "appraisor_content"
#     connection.execute(appraisor_content.insert(), [
#         {"appraisor_id": 1, "content_id": 1},
#         {"appraisor_id": 2, "content_id": 2},
#     ])