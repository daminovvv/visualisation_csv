from fastapi import Request, Depends, APIRouter, UploadFile
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse, StreamingResponse

from src.api.crud import create_csv_file, get_all_files_id, retrieve_csv_content
from src.api.utils import plot_html_from_csv_string, png_bytes_from_csv_string, csv_file_processing, translate_columns
from src.database import get_session, Session

router = APIRouter()
templates = Jinja2Templates(directory="src/templates")

UPLOAD_FOLDER = "uploads"


@router.get("/", response_class=HTMLResponse)
def home_page(request: Request, session: Session = Depends(get_session)):
    """Provides links to find plot by id"""
    file_ids = get_all_files_id(session)
    show_file_ids = file_ids if len(file_ids) < 100 else file_ids[:100]
    return templates.TemplateResponse("home.html", {"request": request, "show_file_ids": show_file_ids})


@router.get("/uploadfile/", response_class=HTMLResponse)
async def upload_form_page(request: Request):
    """Form for uploading csv file"""
    return templates.TemplateResponse("upload_form.html", {"request": request})


@router.post("/uploadfile/", response_class=HTMLResponse)
def upload_file_page(request: Request, file: UploadFile, session: Session = Depends(get_session)):
    """Saves file to db and returns plot"""
    csv_dict = csv_file_processing(file)
    file_id = create_csv_file(session=session, csv_dict=csv_dict)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "file_id": file_id[0],
            "plot_html": plot_html_from_csv_string(csv_dict),
            "created_at": "just now"
        }
    )


@router.get("/files/{file_id}/", response_class=HTMLResponse)
def retrieve_test_results(file_id: int, request: Request, session: Session = Depends(get_session)):
    """Provides plots by file_id"""
    csv_dict = retrieve_csv_content(session=session, file_id=file_id)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "file_id": file_id,
            "plot_html": plot_html_from_csv_string(csv_dict),
            "created_at": csv_dict["description"]["created_at"]
        }
    )


@router.get("/download_csv/{file_id}", response_class=StreamingResponse)
def download_csv(file_id: str, session: Session = Depends(get_session)):
    """Sends plot data in CSV format to user"""
    csv_dict = retrieve_csv_content(session=session, file_id=file_id)
    csv_bytes = translate_columns(csv_dict)["content"].encode("utf-8")
    response = StreamingResponse(iter([csv_bytes]), media_type="text/csv")
    response.headers["Content-Disposition"] = f"attachment; filename={file_id}.csv"
    return response


@router.get("/download_png/{file_id}", response_class=StreamingResponse)
def download_png(file_id: str, session: Session = Depends(get_session)):
    """Sends plot figure in png format to user"""
    csv_dict = retrieve_csv_content(session=session, file_id=file_id)
    png_bytes = png_bytes_from_csv_string(csv_dict)
    response = StreamingResponse(iter([png_bytes]), media_type="image/png")
    response.headers["Content-Disposition"] = f"attachment; filename={file_id}.png"
    return response
