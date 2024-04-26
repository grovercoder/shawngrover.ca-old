from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from src.email import SiteEmail

router = APIRouter()
templates = Jinja2Templates(directory="public")

@router.get("/", response_class=HTMLResponse)
def get_home(request: Request):
    # Switched from static file to using index.html as a template
    # This will handle if we need to pass generated content into the page
    # - such as a CSRF token or similar.
    context = {
        "request": request,
    }
    return templates.TemplateResponse("index.html", context)
 