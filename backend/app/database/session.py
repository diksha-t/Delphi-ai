from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    
    connect_args = {
        "connect_timeout": 5
    }
)

SessionLocal = sessionmaker(
    bind = engine,
    autoflush = False,
    autocommit = False,
)