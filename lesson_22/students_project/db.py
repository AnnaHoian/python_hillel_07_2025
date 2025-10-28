"""
db.py

This module sets up the database connection and session for the
students_project using SQLAlchemy.

Components:
1. Engine: connects to the PostgreSQL database.
2. Base.metadata.create_all(engine): ensures all tables from models are created.
3. SessionLocal: factory for creating new database sessions.
4. session: a single session instance for executing queries.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

engine = create_engine("postgresql+psycopg2://postgres:password3710!!@localhost:5432/postgres")

Base.metadata.create_all(engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()