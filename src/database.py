from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base


engine = create_engine('postgresql://postgres:postgres@localhost/visualisation_db')
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)


def get_session():
    with Session() as session:
        yield session
