from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path
app = FastAPI(title="Ramya Sree Portfolio", description="This is my portfolio website built using FastAPI.", version="1.0.0")
BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
HTML_DIR = BASE_DIR / "templates"
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
@app.get("/")
def home():
    return FileResponse(HTML_DIR / "index.html") 