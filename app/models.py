from sqlalchemy import String, Boolean, Integer, Column, text, TIMESTAMP
from .database import Base


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    roll_no = Column(String, nullable=False)
    phone_number = Column(Integer, nullable=False)
    is_active = Column(Boolean, server_default=text('true'))
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('Now()'))
