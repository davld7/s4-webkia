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


@router.get("/kia-rio.png", tags=tags, response_class=FileResponse, status_code=status.HTTP_200_OK, include_in_schema=False)
async def kia_rio() -> FileResponse:
    path = "static/images/kia-rio.png"
    media_type = "image/png"
    return FileResponse(path=path, media_type=media_type)


@router.get("/kia-sonet.png", tags=tags, response_class=FileResponse, status_code=status.HTTP_200_OK, include_in_schema=False)
async def kia_picanto() -> FileResponse:
    path = "static/images/kia-sonet.png"
    media_type = "image/png"
    return FileResponse(path=path, media_type=media_type)


@router.get("/kia-sportage.png", tags=tags, response_class=FileResponse, status_code=status.HTTP_200_OK, include_in_schema=False)
async def kia_sportage() -> FileResponse:
    path = "static/images/kia-sportage.png"
    media_type = "image/png"
    return FileResponse(path=path, media_type=media_type)


@router.get("/kia-picanto.png", tags=tags, response_class=FileResponse, status_code=status.HTTP_200_OK, include_in_schema=False)
async def kia_picanto() -> FileResponse:
    path = "static/images/kia-picanto.png"
    media_type = "image/png"
    return FileResponse(path=path, media_type=media_type)


@router.get("/kia-seltos.png", tags=tags, response_class=FileResponse, status_code=status.HTTP_200_OK, include_in_schema=False)
async def kia_seltos() -> FileResponse:
    path = "static/images/kia-seltos.png"
    media_type = "image/png"
    return FileResponse(path=path, media_type=media_type)


@router.get("/kia-carens.png", tags=tags, response_class=FileResponse, status_code=status.HTTP_200_OK, include_in_schema=False)
async def kia_carens() -> FileResponse:
    path = "static/images/kia-carens.png"
    media_type = "image/png"
    return FileResponse(path=path, media_type=media_type)


@router.get("/kia-sorento.png", tags=tags, response_class=FileResponse, status_code=status.HTTP_200_OK, include_in_schema=False)
async def kia_sorento() -> FileResponse:
    path = "static/images/kia-sorento.png"
    media_type = "image/png"
    return FileResponse(path=path, media_type=media_type)


@router.get("/kia-k2700.png", tags=tags, response_class=FileResponse, status_code=status.HTTP_200_OK, include_in_schema=False)
async def kia_k2700() -> FileResponse:
    path = "static/images/kia-k2700.png"
    media_type = "image/png"
    return FileResponse(path=path, media_type=media_type)


@router.get("/kia-k3000.png", tags=tags, response_class=FileResponse, status_code=status.HTTP_200_OK, include_in_schema=False)
async def kia_k3000() -> FileResponse:
    path = "static/images/kia-k3000.png"
    media_type = "image/png"
    return FileResponse(path=path, media_type=media_type)
