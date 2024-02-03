from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

Base = declarative_base()


class Appraisor(Base):
    __tablename__ = "appraisors"
    id = Column(Integer, primary_key=True, index=True)
    nickname = Column(String, index=True)
    mac = Column(String, unique=True, index=True)
    last_connection = Column(DateTime)
    installed_firmware = Column(String)
    hardware = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    modified_at = Column(DateTime, default=datetime.utcnow)
    batch_id = Column(Integer, ForeignKey("batches.id"))
    batch = relationship("Batch", back_populates="appraisors")
    contents = relationship("Content", secondary="appraisor_content")



