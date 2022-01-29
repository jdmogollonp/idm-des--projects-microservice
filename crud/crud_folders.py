from typing import Any, Dict, Optional, Union
from schemas.folders import FolderCreate,FolderDelete
from fastapi_sqlalchemy import DBSessionMiddleware, db


import boto3
from core.config import Settings
import os

settings= Settings()

s3_client = boto3.client('s3',region_name=settings.AWS_REGION,  
       aws_access_key_id="",
       aws_secret_access_key="∫")


class CRUDfolder(object):
    def __init__(self):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD) folders in S3
        **Parameters**
        * `bucket`: A S3 bucket 
        """
        self.bucket = settings.BUCKET_NAME

    def create(self,  obj_in: FolderCreate):                
        project_id = obj_in.project_id
        s3_obj = s3_client.put_object(Bucket=self.bucket, Key=("project_"+str(project_id)+"/"))
        return s3_obj

    def delete(self,  obj_in: FolderCreate):
        project_id = obj_in.project_id
        s3_obj = s3_client.delete_object(Bucket=self.bucket, Key=("project_"+str(project_id)+"/"))
        return s3_obj

folder = CRUDfolder()
