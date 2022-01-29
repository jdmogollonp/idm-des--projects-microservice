from fastapi import APIRouter
from api.endpoints import  projects
from api.endpoints import  files
from api.endpoints import  folders

api_router = APIRouter()
api_router.include_router(projects.router,prefix="/api/projects", tags=["projects"])
api_router.include_router(files.router,prefix="/api/files", tags=["files"])
api_router.include_router(folders.router,prefix="/api/folders", tags=["folders"])
