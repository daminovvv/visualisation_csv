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


def create_csv_file_query(csv_dict):
    query = insert(CSVFile).values(**csv_dict).returning(CSVFile.id)
    return query
