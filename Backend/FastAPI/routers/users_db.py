from fastapi import APIRouter, HTTPException, status
from db.models.user import User
from db.esquemas.user import user_schema, users_schema
from db.client import db_client
from bson import ObjectId


router = APIRouter()

@router.get("/", response_model=list[User])
async def get_users():
    return users_schema(db_client.users.find())
 
@router.get("/{id}")
async def get_user(id: str):
    return search_user("_id", ObjectId(id))

def search_user(field: str, value):
    try:
        user = db_client.users.find_one({field: value})
        return User(**user_schema(user))
    except:
        raise HTTPException(status_code=404, detail="User not found")

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
    try:
        if type(search_user("email", user.email)) == User:
            raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="El usuario ya existe"
        )
    except HTTPException as e:
        if e.status_code != 404:  # si no es 404, es que ya existe
            raise e
    
    user_dict = dict(user)
    user_dict.pop("id", None)
    id = db_client.users.insert_one(user_dict).inserted_id
    new_user = user_schema(db_client.users.find_one({"_id": id}))
    return User(**new_user)

@router.put("/")
async def update_user(user: User):
    try:
        user_dict = dict(user)
        user_dict.pop("id", None)
        db_client.users.find_one_and_replace(
            {"_id": ObjectId(user.id)}, user_dict
        )
        return search_user("_id", ObjectId(user.id))
    except:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

@router.delete("/{id}")
async def user(id: str):

    found = db_client.users.find_one_and_delete({"_id": ObjectId(id)})
    if not found:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")