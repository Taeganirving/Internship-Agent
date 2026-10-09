
from contextlib import asynccontextmanager

from fastapi import FastAPI

from .database import initialize_database


@asynccontextmanager
async def lifespan(app: FastAPI):
    initialize_database()
    yield


app = FastAPI(
    title="Internship AI Agent",
    description="AI-powered internship discovery and application management",
    version="0.2.0",
    lifespan=lifespan
)


@app.get("/")
def home():
    return {
        "message": "Internship AI Agent is running!",
        "version": "0.2.0"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "database": "initialized"
    }
