from pydantic import BaseModel


class FolderCreate(BaseModel):
    project_id: int

class FolderDelete(BaseModel):
    project_id: int