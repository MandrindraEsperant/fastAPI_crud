# schemas.py
from pydantic import BaseModel

# Schéma pour la création (input)
class UtilisateurCreate(BaseModel):
    nom: str
    email: str

# Schéma pour la réponse (output)
class UtilisateurResponse(BaseModel):
    id: int
    nom: str
    email: str

    class Config:
        orm_mode = True  # Indique qu'on va utiliser des objets SQLAlchemy
