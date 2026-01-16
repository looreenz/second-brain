from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="Second Brain Backend")

@app.get("/health")
async def healthcheck():
    return {
        "status": "ok",
        "environment": os.getenv("APP_ENV", "undefined")
    }
