from fastapi import Depends, Response
from pydantic import Field
from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from app.utils import AppModel
from typing import Any
from ..service import Service, get_service
from . import router

class CreatePostRequest(AppModel):
    type: str
    price: int
    address: str
    area: int
    rooms_count: int
    description: str
    

class CreatePostResponse(AppModel):
     id: Any = Field(alias="_id")


@router.post("/", response_model = CreatePostResponse)
def create_tweet(
    input: CreatePostRequest,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> dict[str, str]:
    user_id = jwt_data.user_id
    sh_id = svc.repository.create_post(user_id, input.dict())
    return CreatePostResponse(id=sh_id)
