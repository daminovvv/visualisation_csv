from sqlalchemy import Column, Integer, String, Text, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CSVFile(Base):
    __tablename__ = 'csv_files'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    content = Column(Text)  # Используйте Text для хранения содержимого CSV файла
    description = Column(JSON)  # Используйте JSON для хранения расширенных метаданных в формате JSON
