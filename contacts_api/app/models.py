from sqlalchemy import Column, Integer, String, Date
from .database import Base

class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), index=True)
    last_name = Column(String(50), index=True)
    email = Column(String(100), unique=True, index=True)
    phone = Column(String(20))
    birthday = Column(Date)
    extra_info = Column(String(250), nullable=True)
