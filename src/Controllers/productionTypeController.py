import sys
sys.path.append('C:\\Users\\Dell Pc\\Documents\\projects\\projetTkinter')
from src.Models.mainModel import SessionLocal
from src.Models.productionType import ProdType

class productionTypeController:

    @staticmethod
    def getAllTypes():
        with SessionLocal() as session:
            types = session.query(ProdType).all()
            prodTypes =[]
            for type in types:
                prodTypes.append(type.type)
        return prodTypes
    
    @staticmethod
    def getIdType(type):
        with SessionLocal() as session:
            prodType  = session.query(ProdType).filter_by(type=type).first()
        return prodType.idType
    
    @staticmethod
    def getType(idType):
        with SessionLocal() as session:
            prodType  = session.query(ProdType).filter_by(idType=idType).first()
        return prodType.type

    @staticmethod
    def getIdType(type):
        with SessionLocal() as session:
            prodType  = session.query(ProdType).filter_by(type = type).first()
        return prodType.idType