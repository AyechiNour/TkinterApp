from sqlalchemy import Column, Integer, String
import sys
sys.path.append('C:\\Users\\Dell Pc\\Documents\\projects\\projetTkinter')
from src.Models.base import Base

class User(Base):
    __tablename__ = 'userTable'
    idUser = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    password = Column(String)
    name = Column(String)