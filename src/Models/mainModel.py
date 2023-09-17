from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
sys.path.append('C:\\Users\\Dell Pc\\Documents\\projects\\projetTkinter')
from src.Models.user import User
from src.Models.productionType import ProdType
from src.Models.objective import Objective
from src.Models.date import Date
from src.Models.base import Base

# Paramètres de connexion
server_name = 'DESKTOP-OM8GRSH\SQLEXPRESS'
database_name = 'ObjectiveBD'
connection_string = f'mssql+pyodbc://{server_name}/{database_name}?driver=ODBC+Driver+17+for+SQL+Server'

# Création du moteur SQLAlchemy
engine = create_engine(connection_string, echo=True)

# Création de la classe de session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crée toutes les tables définies dans vos modèles
Base.metadata.create_all(bind=engine)

productionTypes = ["Matériel de Réseau et de Télécommunication","Électronique Grand Public","Solutions Énergétiques","Équipements pour l'IoT (Internet des Objets)","Solutions pour les Opérateurs de Services","Solutions de Communication d'Entreprise"]

session = SessionLocal() 

for type in productionTypes:
    typeSearch = session.query(ProdType).filter_by(type=type).first()
    if typeSearch:
        print(typeSearch.type," existe")
    else:
        new_type = ProdType(type=type)
        session.add(new_type)
        session.commit()
        print(type," est ajouté avec succès")