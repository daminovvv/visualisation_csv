import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.api import router as charts_router
from src.startup import populate_db

app = FastAPI()
app.include_router(charts_router)
UPLOAD_FOLDER = "uploads"
app.mount("/uploads", StaticFiles(directory=UPLOAD_FOLDER), name="uploads")
app.add_event_handler("startup", populate_db)


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
