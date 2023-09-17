from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
import sys
sys.path.append('C:\\Users\\Dell Pc\\Documents\\projects\\projetTkinter')
from src.Models.base import Base

class Objective(Base):
    __tablename__ = 'objectiveTable'
    idObjective = Column(Integer, primary_key=True, index=True)
    
    # Foreign key relationship with productionType Table
    idType = Column(Integer, ForeignKey("prodTypeTable.idType"))
    type = relationship("ProdType")
    
    objective = Column(Float)

    # Foreign key relationship with user Table
    idUser = Column(Integer, ForeignKey("userTable.idUser"))
    user = relationship("User")

    # Foreign key relationship with date Table
    idDate = Column(Integer, ForeignKey("dateTable.idDate"))
    date = relationship("Date")