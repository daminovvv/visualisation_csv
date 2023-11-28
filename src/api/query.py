from datetime import datetime

from sqlalchemy import Select, select, insert

from src.models import CSVFile


def get_all_id_query() -> Select:
    query = select(
        CSVFile.id,
    )
    return query


def retrieve_query(file_id: int) -> Select:
    query = select(
        CSVFile.id,
        CSVFile.name,
        CSVFile.content,
        CSVFile.description,
    ).where(CSVFile.id == file_id)
    return query


def create_csv_file_query(name, content):
    description = {"created_at": datetime.utcnow().strftime("%Y-%m-%d"),
                   "file_format": "csv"}
    query = insert(CSVFile).values(
        name=name,
        content=content,
        description=description
    )
    return query
