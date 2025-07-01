from fastapi import FastAPI
from configs.database import  engine, Base

from routes import userRoute # ⬅️ importer les routes

Base.metadata.create_all(bind=engine)# Création automatique des tables

app = FastAPI()

# ⬇️ ajouter le routeur
app.include_router(userRoute.router)


