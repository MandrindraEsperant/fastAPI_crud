# controllers/utilisateurs_controller.py
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import models.userSchemas as schemas, models.user as models

def createUser(utilisateur: schemas.UtilisateurCreate, db: Session):
    nouveau = models.Utilisateur(nom=utilisateur.nom, email=utilisateur.email)
    try:
        db.add(nouveau)
        db.commit()
        db.refresh(nouveau)
        return nouveau
    except IntegrityError:
        db.rollback()  # Toujours rollback après une erreur de commit
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cet email est déjà utilisé. Veuillez en choisir un autre."
        )

def allUsers(db: Session):
   return db.query(models.Utilisateur).all()
    

def oneUser(id: int, db: Session):
    utilisateur = db.query(models.Utilisateur).filter(models.Utilisateur.id == id).first()
    if utilisateur is None:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    return utilisateur

def deleteUser(id: int, db: Session):
    utilisateur = db.query(models.Utilisateur).filter(models.Utilisateur.id == id).first()
    if utilisateur is None:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    else:
        db.delete(utilisateur)
        db.commit()
        return {"message": "Utilisateur supprimé avec succès"}
