from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
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

from models.projects import Project as ModelProject
from schemas.projects import Projects as SchemaProject
from schemas.projects import ProjectDelete as SchemaProjectDelete
from schemas.projects import ProjectSearch  as SchemaSearch
from schemas.projects import ProjectUpdate  as SchemaProjectUpdate
from schemas.projects import ProjectListProject  as SchemaListProject


import crud, models, schemas
import logging

router = APIRouter()

from api import deps

settings= Settings()

security = HTTPBearer()
router = APIRouter()

import requests

@router.post("/create_project/", status_code=201)
def create_project(project_in: SchemaProject, db: Session = Depends(deps.get_db) ):
    db_project = crud.project.create( obj_in=project_in)    
    return db_project

@router.post("/update_project/", status_code=201)
def update_project(project_in: SchemaProjectUpdate, db: Session = Depends(deps.get_db) ):
    project = crud.project.get_by_id( id=project_in.id)
    if not project:
        raise HTTPException(
            status_code=400,
            detail="Project not found",
        )
    else:
        logging.info("entro")        
        response = crud.project.update(  obj_in=project_in)
        if response:
            logging.info("Project updated")
            return 200
        else:
            raise HTTPException(
                status_code=400,
                detail="Project name already taken. Select a new name for your project.",
            )

@router.post("/delete_project/")
def delete_project(project_in: SchemaProjectDelete, db: Session = Depends(deps.get_db) ):
    project = crud.project.get_by_id( id=project_in.id)
    if not project:
        raise HTTPException(
            status_code=400,
            detail="Project not found",
        )
    else:
        response = crud.project.delete( id=project_in.id)
        if response:
            logging.info("Project deleted")
            return 200

@router.post("/search_project/")
def search_project(search_in: SchemaSearch):
    project_list =  crud.project.search_project(keyword = search_in.keyword)
    if not project_list:
        raise HTTPException(
            status_code=400,
            detail="There are no public projects",
        )
    return project_list

@router.post("/list_project/")
def search_project(search_in: SchemaListProject):
    project_list =  crud.project.list_project(username = search_in.username)
    if not project_list:
        raise HTTPException(
            status_code=400,
            detail=f"There user: {username} has no projects",
        )
    return project_list

'''
@router.get("/invite_user/", response_model=SchemaUsers)
def invite_user(user: SchemaUsers,  token: str = Depends(security)):
    db_user = Modeluser(name=user.name, surname=user.surname, email=user.email, password=user.password)
    db.session.add(db_user)
    db.session.commit()
    return db_user
'''

