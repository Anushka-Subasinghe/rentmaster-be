from fastapi import APIRouter, UploadFile
from controller.user import getUserById, rateWorker, register, getAllWorkers, login, checkEmail, getWorkersByJobType, updateProfilePicture, updateUserProfile
from models.user import RateWorker, UpdateUser, User, LoginData

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

@user.get('/user/jobType/{jobType}')
async def get_worker_by_jobType(jobType: str):
    res = getWorkersByJobType(jobType)
    return res

@user.get('/user/getUser/{id}')
async def get_user_by_id(id: str):
    res = getUserById(id)
    return res


@user.get('/users')
async def get_all_workers():
    users = getAllWorkers()
    return users

@user.post("/user/profilePicture/{id}")
async def upload_profile_picture(file: UploadFile, id: str):
    return updateProfilePicture(file, id)

@user.patch('/user/updateProfile')
async def update_user_profile(updated_user: UpdateUser):
    updated_user = updateUserProfile(updated_user)
    if updated_user:
        return updated_user
    return {"message": "User not found"}

@user.patch('/user/rate')
async def update_user_profile(rate: RateWorker):
    rated_worker = rateWorker(rate)
    if rated_worker:
        return rated_worker
    return {"message": "User not found"}
