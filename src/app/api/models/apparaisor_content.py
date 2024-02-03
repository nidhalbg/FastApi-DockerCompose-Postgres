from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class AppraisorContent(Base):
    __tablename__ = "appraisor_content"
    appraisor_id = Column(Integer, ForeignKey("appraisors.id"), primary_key=True)
    content_id = Column(Integer, ForeignKey("contents.id"), primary_key=True)
