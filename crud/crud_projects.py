from typing import Any, Dict, Optional, Union
from core.security import get_password_hash, verify_password
from crud.base import CRUDBase
from models.projects import Project
from schemas.projects import Projects,ProjectCreate,ProjectUpdate
from fastapi_sqlalchemy import DBSessionMiddleware, db



class CRUDProject(CRUDBase[Project, ProjectCreate,ProjectUpdate]):
    def get_by_id(self,  id: str):
        return db.session.query(Project).filter(Project.id == id).first()

    def create(self,  obj_in: Project):
        
        db_obj = Project(username = obj_in.username,
        name = obj_in.name,
        description = obj_in.description, 
        tags = obj_in.tags,
        isPublic = obj_in.isPublic)
        db.session.add(db_obj)
        db.session.commit()
        db.session.refresh(db_obj)
        return db_obj

    def update(self,  obj_in: ProjectUpdate):    
        db.session.query(Project).filter(Project.id == obj_in.id).\
        update(dict(obj_in), synchronize_session="fetch")         
        db.session.commit()
        return obj_in
    
    def delete(self,  id: int):
        Project = self.get_by_id( id=id)
        db.session.delete(Project)
        db.session.commit()
        if not Project:
            return None
        return Project
    
    def list_project(self, username = str):
        my_projects = db.session.query(Project).\
        filter(Project.username.contains(username)).all()
        if not my_projects:
            return None
        return my_projects

    def search_project(self, keyword = str):
        public_projects = db.session.query(Project).\
        filter(Project.name.contains(keyword)).all()
        if not public_projects:
            return None
        return public_projects

    def is_active(self, Project: Project) -> bool:
        return Project.isActive 

project = CRUDProject(Project)
