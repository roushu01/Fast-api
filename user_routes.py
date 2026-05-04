from fastapi import APIRouter
from database import user_collection
from models import User

from bson import ObjectId

router = APIRouter()

@router.post("/user")
def create_user(user: User):
    try:
        data=user.model_dump()
        result = user_collection.insert_one(data)
        print("Inserted ID:", result.inserted_id)  
        return {"message": "User created"}
    except Exception as e:
        print("ERROR:", e)
        return {"error": str(e)}


@router.get("/user")
def get_users():
    users = user_collection.find()
    results=[]
    for user in users:
        results.append({
            "id":str(user["_id"]),
            "name":user["name"],
            "email":user["email"]
        })
    return results


@router.get("/user/{id}")
def get_user(id: str):
    user = user_collection.find_one({"_id": ObjectId(id)})
    return user

# Update
@router.put("/user/{id}")
def update_user(id: str, data: dict):
    user_collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": data}
    )
    return {"message": "User updated"}

# Delete
@router.delete("/user/{id}")
def delete_user(id: str):
    user_collection.delete_one({"_id": ObjectId(id)})
    return {"message": "User deleted"}