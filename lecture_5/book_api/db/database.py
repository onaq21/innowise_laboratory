from sqlalchemy import create_engine
from sqlalchemy.orm  import sessionmaker, declarative_base

engine = create_engine("sqlite:///books.db", echo=True)
Base = declarative_base()

SessionLocal = sessionmaker(bind=engine, autoflush=False)

def get_db():
    """Provide a database session for a FastAPI request and close it after use"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(bind=engine)