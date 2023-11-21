from manager.load_config import CONFIG

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from contextlib import asynccontextmanager

from pymongo import MongoClient

import colorama
from colorama import Fore

from ofertas import router as ofertas_router
from users import router as users_router


colorama.init(autoreset=True)

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.mongoConnection = MongoClient(CONFIG["MONGO_HOST"], CONFIG["MONGO_PORT"])

    yield

    app.state.mongoConnection.close()

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ofertas_router, prefix="/ofertas")
app.include_router(users_router, prefix="/users")
