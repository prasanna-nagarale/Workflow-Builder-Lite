from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
load_dotenv()

from app.database import Base, engine
from app.routes import workflows, runs, status


app = FastAPI(title="Workflow Builder Lite", version="1.0.0")

# Create database tables
Base.metadata.create_all(bind=engine)

# Mount static files and templates
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# Include API routes
app.include_router(workflows.router, prefix="/api/workflows", tags=["workflows"])
app.include_router(runs.router, prefix="/api/runs", tags=["runs"])
app.include_router(status.router, prefix="/api", tags=["status"])

# Frontend routes
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/builder")
def builder(request: Request):
    return templates.TemplateResponse("builder.html", {"request": request})

@app.get("/run")
def run_page(request: Request):
    return templates.TemplateResponse("run.html", {"request": request})

@app.get("/history")
def history_page(request: Request):
    return templates.TemplateResponse("history.html", {"request": request})

@app.get("/status")
def status_page(request: Request):
    return templates.TemplateResponse("status.html", {"request": request})