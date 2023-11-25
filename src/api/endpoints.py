from fastapi import FastAPI, Request, Depends, APIRouter
from fastapi.templating import Jinja2Templates

from charts import get_plot_html

router = APIRouter()
templates = Jinja2Templates(directory="src/templates")


@router.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "plot_html": get_plot_html()})
