from fastapi import APIRouter
from controller.user import create, getOne, getAll, update, delete
from models.user import User

user = APIRouter()

@user.post('/user')
async def create_user(user: User):
    res = create(user)
    print("res : ", res)
    return res

@user.get('/user/{user_id}')
async def get_user_by_id(user_id: str):
    user = getOne(user_id)
    if user:
        return user
    return {"message": "User not found"}

@user.delete('/worker/{user_id}')
async def delete_worker(user_id: str):
    return delete(user_id)

@user.get('/users')
async def get_all_users():
    users = getAll()
    return users

@user.put('/user/{user_id}')
async def update_user_by_id(user_id: str, updated_user: User):
    updated_user = update(user_id, updated_user)
    if updated_user:
        return updated_user
    return {"message": "User not found"}
