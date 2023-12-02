from fastapi import APIRouter, status
from fastapi.responses import HTMLResponse, FileResponse

prefix = "/about"
tags = ["About"]

router = APIRouter(prefix=prefix, tags=tags)


@router.get("/", response_class=HTMLResponse, status_code=status.HTTP_200_OK)
async def about() -> FileResponse:
    path = "templates/about.html"
    media_type = "text/html"
    return FileResponse(path=path, media_type=media_type)
