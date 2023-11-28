import logging
from datetime import datetime


from src.models import CSVFile
from src.database import Session

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def populate_db():
    session = Session()
    if is_database_empty(session):
        with open("data/your_data.csv", "r") as csv_file:
            csv_string = csv_file.read()
            csv_name = csv_file.read()
        session.add(CSVFile(name=csv_name, content=csv_string, description={
            "created_at": datetime.utcnow().strftime("%Y-%m-%d"),
            "file_format": "csv"
        }))
        session.commit()
        logger.info("Database populated successfully")
    else:
        logger.info("Database contains data, no population is needed")
    session.close()


def is_database_empty(session: Session):
    return session.query(CSVFile).count() == 0
