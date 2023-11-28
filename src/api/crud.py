from src.api.query import get_all_id_query, create_csv_file_query, retrieve_query


def get_all_files_id(session):
    query = get_all_id_query()
    data = session.execute(query)
    return data.all()


def retrieve_csv_content(session, file_id) -> dict:
    query = retrieve_query(file_id=file_id)
    data = session.execute(query)
    csv_row = data.first()
    return csv_row._asdict()


def create_csv_file(session, name, content):
    query = create_csv_file_query(name, content)
    session.execute(query)
    session.commit()
