# models.py
from sqlalchemy import Column, Integer, String
from configs.database import Base

class Utilisateur(Base):
    __tablename__ = "utilisateurs"  # Nom de la table en base

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, index=True)
    email = Column(String, unique=True, index=True)
