from fastapi import APIRouter
from controller.user import register, getOne, getAll, update, delete, login, checkEmail
from models.user import User, LoginData

user = APIRouter()


@user.post('/user/register')
async def register_user(user: User):
    res = register(user)
    return res


@user.post('/user/login')
async def login_user(user_data: LoginData):
    res = login(user_data)
    return res

@user.get('/user/check-email/{email}')
async def register_user(email: str):
    res = checkEmail(email)
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
