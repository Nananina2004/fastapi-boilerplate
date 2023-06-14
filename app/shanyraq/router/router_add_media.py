from fastapi import Depends, Response, UploadFile
from pydantic import Field
from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from app.utils import AppModel
from typing import Any
from ..service import Service, get_service
from . import router

@router.post("/{shanyraq_id:str}/media")
def upload_file(
    shanyraq_id: str,
    file: UploadFile,
    svc: Service = Depends(get_service),
):
    url = svc.s3_service.upload_file(shanyraq_id, file.file, file.filename)
    return {"msg": url}
