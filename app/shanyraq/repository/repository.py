from typing import Any

from bson.objectid import ObjectId
from pymongo.database import Database
from pymongo.results import DeleteResult, UpdateResult

class ShanyraqRepository:
    def __init__(self, database: Database):
        self.database = database

    def create_post(self, user_id, input: dict[str, Any]):
        payload = {
            "type": input["type"],
            "price": input["price"],
            "address": input["address"],
            "area": input["area"],
            "rooms_count": input["rooms_count"],
            "description": input['description'],
            "user_id": ObjectId(user_id)
            
        }
        insert_result = self.database["shanyraqs"].insert_one(payload)
        return insert_result.inserted_id
    
    def get_post_by_id(self, post_id: str) -> dict | None:
        post = self.database["shanyraqs"].find_one(
            {
                "_id": ObjectId(post_id),
            }
        )
        return post
    
    def update_post(self,  post_id: str, user_id: str, input: dict[str, Any]) -> UpdateResult:
        self.database["shanyraqs"].update_one(
            filter={"_id": ObjectId(post_id),  "user_id": ObjectId(user_id)},
            update={
                "$set": input,
            },
        )

    def delete_shanyrak(self, shanyraq_id: str, user_id: str) -> DeleteResult:
        return self.database["shanyraqs"].delete_one(
            {"_id": ObjectId(shanyraq_id), "user_id": ObjectId(user_id)}
        )


