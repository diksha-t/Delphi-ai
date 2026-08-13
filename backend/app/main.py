from fastapi import FastAPI
from app.database.session import engine

app = FastAPI(
    title = "Delphi API",
    description = "Backend for Delphi multi-agent society simulation.",
    version = "0.1.0"
)

@app.get("/")
def root():
    return {
        "project": "Delphi",
        "status": "running",
    }
    
@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.get("/health/database")
def database_health():
    try:
        with engine.connect():
            return {
                "database": "connected"
            }

    except Exception as e:
        return {
            "database": "disconnected",
            "error": str(e),
        }
