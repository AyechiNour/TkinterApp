from sqlalchemy import Column, Integer, String
import sys
sys.path.append('C:\\Users\\Dell Pc\\Documents\\projects\\projetTkinter')
from src.Models.base import Base

class ProdType(Base):
    __tablename__ = 'prodTypeTable'
    idType = Column(Integer, primary_key=True, index=True)
    type = Column(String(255), unique=True, index=True)