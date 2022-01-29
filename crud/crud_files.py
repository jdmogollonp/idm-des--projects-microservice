from typing import Any, Dict, Optional, Union
from core.security import get_password_hash, verify_password
from crud.base import CRUDBase
from models.projects import File
from schemas.files import FileCreate,FileUpdate,FileUpdateUrl
from fastapi_sqlalchemy import DBSessionMiddleware, db


class CRUDfile(CRUDBase[File, FileCreate,FileUpdate]):
    def get_by_id(self,  id: str):
        return db.session.query(File).filter(File.id == id).first()

    def create(self,  obj_in: File):
        db_obj = File(name = obj_in.name,url =obj_in.url,project_id = obj_in.project_id)
        db.session.add(db_obj)
        db.session.commit()
        db.session.refresh(db_obj)
        return db_obj

    def delete(self,  id: int) -> Optional[File]:
        File = self.get_by_id( id=id)
        db.session.delete(File)
        db.session.commit()
        if not File:
            return None
        return File
    
    def update_url(self, obj_in: File):
        db_obj = File(type = obj_in.type,url =obj_in.url,project_id = obj_in.project_id)
        db.session.add(db_obj)
        db.session.commit()
        db.session.refresh(db_obj)
        return db_obj

    def search_file(self, keyword = str):
        public_files = db.session.query(File).filter(File.id == id).all()
        if not public_files:
            return None
        return public_files


files = CRUDfile(File)

