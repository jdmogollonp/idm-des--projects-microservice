from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Boolean,Enum,ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


Base = declarative_base()


class Project(Base):
    __tablename__ = "project"
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    name = Column(String, nullable=False,unique=True)
    description = Column(String, nullable=True)
    creation_date = Column(DateTime, server_default=func.now())
    modification_date = Column(DateTime, onupdate=func.now())
    isActive = Column(Boolean, default=True)
    isPublic = Column(Boolean, default=False)
    version_id = Column(Integer, nullable=False)
    tags= Column(ARRAY(String),nullable=True)
    __mapper_args__ = {
        "version_id_col": version_id
    }


class File(Base):
    __tablename__ = "files"
    id = Column(Integer, primary_key=True)    
    creation_date = Column(DateTime, server_default=func.now())
    modification_date = Column(DateTime, onupdate=func.now())
    url = Column(String,nullable=False)
    type = Column(String,nullable=False)
    version_id = Column(Integer, nullable=False)        
    project_id = Column(Integer, ForeignKey("project.id"))
    project = relationship("Project")
    __mapper_args__ = {
        "version_id_col": version_id
    }

