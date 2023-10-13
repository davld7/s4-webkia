from fastapi import APIRouter, status
from fastapi.responses import HTMLResponse, FileResponse

prefix = "/vehicles"
tags = ["Vehicles"]

router = APIRouter(prefix=prefix, tags=tags)


@router.get("/", response_class=HTMLResponse, status_code=status.HTTP_200_OK)
async def vehicles() -> FileResponse:
    path = "templates/vehicles.html"
    media_type = "text/html"
    return FileResponse(path=path, media_type=media_type)
