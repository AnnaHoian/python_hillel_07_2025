"""
db.py

Creates a connection to PostgreSQL by SQLAlchemy.
Contains:
- engine: connection parameters
- SessionLocal: session factory
- Base: base class for ORM models
- get_session(): returns a new session to work with the database
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql+psycopg2://postgres:password3710!!@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def get_session():
    return SessionLocal()
