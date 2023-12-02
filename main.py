from fastapi import FastAPI, HTTPException, status
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from backend.routers import about, company, vehicles, contact, admin
from backend.database.client import client
from pymongo.errors import PyMongoError

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
    path = "index.html"
    media_type = "text/html"
    return FileResponse(path=path, media_type=media_type)


@app.get("/favicon.ico", tags=tags, response_class=FileResponse, status_code=status.HTTP_200_OK, include_in_schema=False)
async def favicon() -> FileResponse:
    path = "favicon.ico"
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


@app.get("/contact.js", tags=tags, response_class=FileResponse, status_code=status.HTTP_200_OK, include_in_schema=False)
async def script() -> FileResponse:
    path = "static/js/contact.js"
    media_type = "text/javascript"
    return FileResponse(path=path, media_type=media_type)


@app.get("/ping", response_class=JSONResponse, status_code=status.HTTP_200_OK)
async def send_ping():
    try:
        client.admin.command('ping')
        message = "Pinged your deployment. You successfully connected to MongoDB!"
        return JSONResponse(content={"message": message})
    except PyMongoError as exception:
        detail = str(exception)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=detail)
