from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class Firmware(Base):
    __tablename__ = "firmwares"
    id = Column(Integer, primary_key=True, index=True)
    version = Column(String, index=True)
    url = Column(String)
    compatible_hardware = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    modified_at = Column(DateTime, default=datetime.utcnow)
    #batch_id = Column(Integer, ForeignKey("batches.id"))
    #batch = relationship("Batch", back_populates="firmwares")