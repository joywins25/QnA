from sqlalchemy import Boolean, Column, Integer, String

""" 
from Ex004_FastCampus_FastAPI\database.py
Base = declarative_base()
"""

# from .database import Base  # 기존 코드 주석 처리
from database import Base  # 수정된 코드


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, index=True)
    password = Column(String(255))
    is_active = Column(Boolean, default=True)