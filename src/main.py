import uvicorn
from fastapi import FastAPI, Request, Depends
from api import router as charts_router

app = FastAPI()
app.include_router(charts_router)


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
