from fastapi import FastAPI, status
from fastapi.responses import HTMLResponse, FileResponse
from routers import about, company, vehicles, contact, admin

app = FastAPI()
app.title = "KIA"
tags = ["Index"]

app.include_router(about.router)
app.include_router(company.router)
app.include_router(vehicles.router)
app.include_router(contact.router)
app.include_router(admin.router)


@app.get("/", tags=tags, response_class=HTMLResponse, status_code=status.HTTP_200_OK)
async def index() -> FileResponse:
    path = "templates/index.html"
    media_type = "text/html"
    return FileResponse(path=path, media_type=media_type)


@app.get("/favicon.ico", tags=tags, response_class=FileResponse, status_code=status.HTTP_200_OK, include_in_schema=False)
async def favicon() -> FileResponse:
    path = "static/images/favicon.ico"
    media_type = "image/x-icon"
    return FileResponse(path=path, media_type=media_type)


@app.get("/styles.css", tags=tags, response_class=FileResponse, status_code=status.HTTP_200_OK, include_in_schema=False)
async def styles() -> FileResponse:
    path = "static/css/styles.css"
    media_type = "text/css"
    return FileResponse(path=path, media_type=media_type)


@app.get("/script.js", tags=tags, response_class=FileResponse, status_code=status.HTTP_200_OK, include_in_schema=False)
async def script() -> FileResponse:
    path = "static/js/script.js"
    media_type = "text/javascript"
    return FileResponse(path=path, media_type=media_type)


@app.get("/kia-rio.png", tags=tags, response_class=FileResponse, status_code=status.HTTP_200_OK, include_in_schema=False)
async def kia_rio() -> FileResponse:
    path = "static/images/kia-rio.png"
    media_type = "image/png"
    return FileResponse(path=path, media_type=media_type)


@app.get("/kia-sonet.png", tags=tags, response_class=FileResponse, status_code=status.HTTP_200_OK, include_in_schema=False)
async def kia_picanto() -> FileResponse:
    path = "static/images/kia-sonet.png"
    media_type = "image/png"
    return FileResponse(path=path, media_type=media_type)


@app.get("/kia-sportage.png", tags=tags, response_class=FileResponse, status_code=status.HTTP_200_OK, include_in_schema=False)
async def kia_sportage() -> FileResponse:
    path = "static/images/kia-sportage.png"
    media_type = "image/png"
    return FileResponse(path=path, media_type=media_type)
