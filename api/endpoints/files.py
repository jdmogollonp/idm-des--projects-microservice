from typing import Any, List
from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder

from sqlalchemy.orm import Session
from core.config import Settings
from core.security import generate_confirmation_token, confirm_token
from utils import send_new_account_email, send_ses

import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db
from fastapi.security import HTTPBearer

from models.projects import File as ModelFile
from schemas.files import FileUpdate as SchemaUpdate
from schemas.files import FileCreate as SchemaCreate
from schemas.files import FileDelete as SchemaFileDelete
from schemas.files import FileUpdateUrl as SchemaUpdateUrl

import crud, models, schemas
import logging
from api import deps

settings= Settings()
security = HTTPBearer()
router = APIRouter()


@router.post("/upload_file/", status_code=201)
def upload_file(file_in: SchemaCreate, db: Session = Depends(deps.get_db) ):
    db_file = crud.files.create( obj_in=file_in)
    return db_file

@router.post("/delete_file/")
def delete_project(file_in: SchemaFileDelete, db: Session = Depends(deps.get_db) ):
    file = crud.files.get_by_id( id=file_in.id ) 
    if not file:
        raise HTTPException(
            status_code=400,
            detail="File not found",
        )
    else:
        response = crud.files.delete( id=file.id)
        if response:
            logging.info("File deleted")
            return 200

@router.post("/update_urls/", status_code=201)
def update_project_url(file_in:SchemaUpdateUrl, db: Session = Depends(deps.get_db)):
    project = crud.project.get_by_id( id=file_in.project_id)
    if not project:
        raise HTTPException(
            status_code=400,
            detail="project does not exists",
        )
    else:
        project_update = crud.files.update_url( obj_in=file_in)
        logging.info("Urls updated")
        return project_update







