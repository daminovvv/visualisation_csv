from sqlalchemy import Column, Integer, String, Text, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CSVFile(Base):
    __tablename__ = 'csv_files'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    content = Column(Text)
    description = Column(JSON)
