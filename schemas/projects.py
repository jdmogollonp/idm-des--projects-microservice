from pydantic import BaseModel,constr
from pydantic.networks import EmailStr
import email_validator
from typing import List

from typing import Optional


class Projects(BaseModel):
    username: str
    name: str
    description: str
    tags: List[constr(max_length=255)]
    isPublic: bool
    class Config:
        orm_mode = True

class Profiles(BaseModel):
    user_id: int
    id_project: int
    user_type: str
    permissions: str

    class Config:
        orm_mode = True

# Properties to receive via API on creation
class ProjectCreate(BaseModel):
    email: EmailStr
    password: str

class ProjectDelete(BaseModel):
    id: int

class ProjectSearch(BaseModel):
    keyword: str

class ProjectListProject(BaseModel):
    username: str

# Properties to receive via API on update
class ProjectUpdate(BaseModel):
    id: int
    username: str
    name: str
    description: str
    tags: List[constr(max_length=255)]
    isPublic: bool




