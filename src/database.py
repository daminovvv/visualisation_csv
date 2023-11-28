import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.models import Base


engine = create_engine(os.getenv("POSTGRES_URL"))
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)


def get_session():
    with Session() as session:
        yield session
