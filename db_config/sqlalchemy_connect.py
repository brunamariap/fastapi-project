from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from domain.data.sqlalchemy_models import Base

DB_URL = "postgresql://postgres:BMp7890@localhost:5432/fastapi"

engine = create_engine(DB_URL)

Base.metadata.create_all(engine)
SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)
