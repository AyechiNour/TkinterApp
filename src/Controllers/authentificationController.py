import sys
import re
sys.path.append('C:\\Users\\Dell Pc\\Documents\\projects\\projetTkinter')
from src.Models.mainModel import SessionLocal
from src.Models.user import User
import bcrypt

class AuthentificationController:

    @staticmethod
    def signIn(email, password):
        with SessionLocal() as session:
            if (AuthentificationController.is_empty_string(email)):
                raise ValueError("Veuillez remplir tous les champs du formulaire.")

            if (AuthentificationController.is_empty_string(password)):
                raise ValueError("Veuillez remplir tous les champs du formulaire.")
    
            existing_user = session.query(User).filter_by(email=email).first()

            if existing_user:
                print(bcrypt.checkpw(password.encode('utf-8'), existing_user.password.encode('utf-8')))
                if bcrypt.checkpw(password.encode('utf-8'), existing_user.password.encode('utf-8')):
                    return existing_user
                else:
                    raise ValueError("Email ou Mot de passe incorrect.")
            else:
                raise ValueError("Email ou Mot de passe incorrect.")
    
    @staticmethod
    def signUp(name, email, password, confpassword):
        with SessionLocal() as session:
            if (AuthentificationController.is_empty_string(name)):
                raise ValueError("Veuillez remplir tous les champs du formulaire.")
            
            if (AuthentificationController.is_empty_string(email)):
                raise ValueError("Veuillez remplir tous les champs du formulaire.")

            if (AuthentificationController.is_empty_string(password)):
                raise ValueError("Veuillez remplir tous les champs du formulaire.")

            if (AuthentificationController.is_empty_string(confpassword)):
                raise ValueError("Veuillez remplir tous les champs du formulaire.")

            if not(AuthentificationController.verifEmail(email)):
                raise ValueError("L'adresse e-mail n'est pas valide.")
            
            if not(AuthentificationController.verifPassword(password)):
                raise ValueError("Le mot de passe n'est pas valide")

            existing_user  = session.query(User).filter_by(email=email).first()

            if existing_user:
                raise ValueError("Un utilisateur avec cet e-mail existe déjà.")

            if password != confpassword:
                raise ValueError("Les deux mots de passe ne sont pas conformes")

            password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
            new_user = User(email=email, password=password_hash, name=name)
            try:
                session.add(new_user)
                session.commit()
            except Exception as e:
                session.rollback() 
                raise ValueError("Une erreur s'est produite lors de l'ajout de l'utilisateur à la base de données.")
            
            userNew= session.query(User).filter_by(email=email).first()
        return userNew
        
    @staticmethod
    def verifEmail(email):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$"
        return re.match(pattern, email) is not None
    
    @staticmethod
    def verifPassword(password):
        # Vérifier si la longueur du mot de passe est d'au moins 8 caractères
        if len(password) < 8:
            return False
        
        # Vérifier si le mot de passe contient au moins une lettre majuscule
        if not any(char.isupper() for char in password):
            return False
        
        # Vérifier si le mot de passe contient au moins une lettre minuscule
        if not any(char.islower() for char in password):
            return False
        
        # Vérifier si le mot de passe contient au moins un chiffre
        if not any(char.isdigit() for char in password):
            return False
        
        # Si toutes les conditions sont satisfaites, le mot de passe est valide
        return True
    
    @staticmethod
    def is_empty_string(s):
        return len(s.strip()) == 0