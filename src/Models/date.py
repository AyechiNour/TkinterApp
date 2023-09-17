from sqlalchemy import Column, Integer, Date
import sys
sys.path.append('C:\\Users\\Dell Pc\\Documents\\projects\\projetTkinter')
from src.Models.base import Base

class Date(Base):
    __tablename__ = 'dateTable'
    idDate = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    nbdays = Column(Integer)