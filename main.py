from fastapi import FastAPI, status
from fastapi.responses import HTMLResponse, FileResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse, status_code=status.HTTP_200_OK)
async def index():
    path = "templates/index.html"
    media_type = "text/html"
    return FileResponse(path=path, media_type=media_type)
