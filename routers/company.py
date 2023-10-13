from fastapi import APIRouter, status
from fastapi.responses import HTMLResponse, FileResponse

prefix = "/company"
tags = ["Company"]

router = APIRouter(prefix=prefix, tags=tags)


@router.get("/", response_class=HTMLResponse, status_code=status.HTTP_200_OK)
async def company() -> FileResponse:
    path = "templates/company.html"
    media_type = "text/html"
    return FileResponse(path=path, media_type=media_type)
