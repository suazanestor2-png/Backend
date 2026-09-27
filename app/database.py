import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

if MONGO_URI:
    # Producción (Render): usa la URI completa de Atlas tal cual
    client = MongoClient(MONGO_URI)
    MONGO_DB = os.getenv("MONGO_DB", "aprendiz")
else:
    # Local: arma la URI con host/puerto sueltos
    MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
    MONGO_PORT = os.getenv("MONGO_PORT", "27017")
    MONGO_DB = os.getenv("MONGO_DB", "aprendiz")
    MONGO_USER = os.getenv("MONGO_USER", "")
    MONGO_PASSWORD = os.getenv("MONGO_PASSWORD", "")

    if MONGO_USER and MONGO_PASSWORD:
        uri = f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}?authSource=admin"
    else:
        uri = f"mongodb://{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}"

    client = MongoClient(uri)

database = client[MONGO_DB]


def get_db():
    return database