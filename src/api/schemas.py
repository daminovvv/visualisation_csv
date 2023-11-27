from typing import Any

from pydantic import BaseModel


class CSVFileSchema(BaseModel):
    class Config:
        from_attributes = True

    id: int
    name: str
    content: Any
    description: Any
