from fastapi import Depends, Response
from pydantic import Field
from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from app.utils import AppModel
from typing import Any
from ..service import Service, get_service
from . import router


class GetPostResponse(AppModel):
    id: Any = Field(alias="_id")
    type: str
    price: int
    address: str
    area: int
    rooms_count: int
    description: str
    user_id: Any


@router.get("/{shanyraq_id:str}", response_model=GetPostResponse)
def get_my_post(
    shanyraq_id = str,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> dict[str, str]:
    shanyrak = svc.repository.get_post_by_id(shanyraq_id)
    if shanyrak is None:
        return Response(status_code=404)
    return GetPostResponse(**shanyrak)
