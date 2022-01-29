from typing import Any, List
from fastapi import FastAPI
from fastapi.security import HTTPBearer
from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from models.projects import Project as ModelProject

from schemas.projects import Projects as SchemaProject
from schemas.folders import FolderCreate as SchemaFolderCreate


import crud, models, schemas
import logging


security = HTTPBearer()
router = APIRouter()


@router.post("/create_folder/",status_code=201)
def create_folder(project_in: SchemaFolderCreate):
    project_folder = crud.folder.create(obj_in=project_in)
    if not project_folder:
        raise HTTPException(
            status_code=400,
            detail="Error creating object in Bucket, please check your credentials and bucket name",
        )
    return project_folder



@router.post("/delete_folder/",status_code=200)
def create_folder(project_in: SchemaFolderCreate):
    project_folder = crud.folder.delete(obj_in=project_in)
    if not project_folder:
        raise HTTPException(
            status_code=400,
            detail="Error deleting object in Bucket,please check your credentials and bucket name",
        )
    return project_folder
