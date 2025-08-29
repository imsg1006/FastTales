from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 

from core.config import settings 
from db.base import Base

engine = create_engine(
    settings.DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

 

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from models.story import Story, StoryNode

def create_tables():
    Base.metadata.create_all(bind=engine)