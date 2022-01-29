from pydantic import BaseModel


class FileCreate(BaseModel):
    name: str
    url:  str
    project_id: int


class FileDelete(BaseModel):
    id: int


class FileUpdate(BaseModel):
    filename: str
    name: str

class FileUpdateUrl(BaseModel):
    project_id: int
    url: str
    type: str

