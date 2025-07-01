from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models.userSchemas as userSchemas
from configs.database import SessionLocal, engine, Base,  get_db
from controllers import userController as controller

router = APIRouter(
    prefix="/utilisateurs",  # Toutes les routes commenceront par /utilisateurs
    tags=["utilisateurs"]    # Regroupe ces routes dans la doc Swagger
)

@router.post("/", response_model=userSchemas.UtilisateurResponse)
def creer_utilisateur(utilisateur: userSchemas.UtilisateurCreate, db: Session = Depends(get_db)):
    return controller.createUser(utilisateur, db)

@router.get("/", response_model=list[userSchemas.UtilisateurResponse])
def lire_utilisateurs(db: Session = Depends(get_db)):
    return controller.allUsers(db)

@router.get("/{id}", response_model=userSchemas.UtilisateurResponse)
def lire_utilisateur(id: int, db: Session = Depends(get_db)):
    return controller.oneUser(id, db)

@router.delete("/{id}")
def supprimer_utilisateur(id: int, db: Session = Depends(get_db)):
    return controller.deleteUser(id, db)
    