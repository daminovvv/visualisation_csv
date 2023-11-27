import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from api import router as charts_router

app = FastAPI()
app.include_router(charts_router)
UPLOAD_FOLDER = "uploads"
app.mount("/uploads", StaticFiles(directory=UPLOAD_FOLDER), name="uploads")

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
