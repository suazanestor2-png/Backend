from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import aprendiz_router

app = FastAPI(title="API Aprendices")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(aprendiz_router.router)