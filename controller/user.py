import base64
import bcrypt
from typing import List, Dict

from fastapi import HTTPException, UploadFile, status
from models.user import UpdateUser, User, LoginData, JobType
from schemas.serialize import serializeDict, serializeList
from config.db import db
from bson import ObjectId

def getWorkersByJobType(jobType: JobType):
    print(jobType)
    workers = db.users.find({"job_types": {"$in": [jobType]}})
    hasworkers = []
    for worker in workers:
    # Access and work with the matching documents
        print(worker)
        worker['_id'] = str(worker['_id'])
        hasworkers.append(worker)
    return hasworkers    

def register(user: User):
    salt = bcrypt.gensalt()
    password = bcrypt.hashpw(user.password.encode('utf-8'), salt)
    userExists = db.users.find_one({"email": user.email})
    if userExists is None:
        user = {
            "username": user.name,
            "email": user.email,
            "user_type": user.user_type,
            "job_types": user.job_types if user.user_type == "worker" else None,
            "hashed_password": password,
            "salt": salt,
            "phone": ''
        }
        inserted_result = db.users.insert_one(dict(user))
        res = db.users.find_one({"_id": inserted_result.inserted_id})
        return {
            "name": res["username"],
            "email": res["email"],
            "phone": res['phone'] if res["phone"] else None,
            "user_type": res["user_type"],
            "job_types": res["job_types"] if res["user_type"] == "worker" else None,
            "id": str(res['_id']),
            "profile_picture": res['profile_picture'] if res["profile_picture"] else None,
            "rating": 5 if res["user_type"] == "worker" else None
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="User with this email already exists. Please use a different email.")


def getAllWorkers():
    print("<===== Get All Workers =====>")
    return serializeList(db.users.find({"user_type": "worker"}))


def verify_user(loginData: LoginData):
    user = db.users.find_one({"email": loginData.email})
    if user:
        hashed_password = user["hashed_password"]
        salt = user["salt"]
        if bcrypt.hashpw(loginData.password.encode('utf-8'), salt) == hashed_password:
            return user  # Password is correct
        else:
            return None  # Password is incorrect
    else:
        return None  # User not found
    
def checkEmail(email: str):    
    user = db.users.find_one({"email": email})
    if user:
        return True
    else:
        return False

def login(loginData: LoginData):
    res = verify_user(loginData)
    if res:
        return {
            "name": res["username"],
            "email": res["email"],
            "phone": res['phone'] if res["phone"] else None,
            "user_type": res["user_type"],
            "job_types": res["job_types"] if res["user_type"] == "worker" else None,
            "id": str(res['_id']),
            "profile_picture": res["profile_picture"] if "profile_picture" in res else None,
            "rating": res['rating'] if res["rating"] else None
        }
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="Login failed. Invalid username or password.")
    

def updateProfilePicture(picture: UploadFile, id: str):
    user_doc = db.users.find_one({"_id": ObjectId(id)})
    if not user_doc:
        raise HTTPException(status_code=404, detail="User not found")

    # Read the image file and encode it as a base64 string
    image_data = base64.b64encode(picture.file.read()).decode('utf-8')

    # Update the user's profile_picture field with the base64-encoded image
    db.users.update_one({"_id": ObjectId(id)}, {"$set": {"profile_picture": image_data}})

    res = db.users.find_one({"_id": ObjectId(id)})
    return {
            "name": res["username"],
            "email": res["email"],
            "phone": res['phone'] if res["phone"] else None,
            "user_type": res["user_type"],
            "job_types": res["job_types"] if res["user_type"] == "worker" else None,
            "id": str(res['_id']),
            "profile_picture": res['profile_picture'] if res["profile_picture"] else None,
            "rating": res['rating'] if res["rating"] else None
        }

def updateUserProfile(user: UpdateUser):
    db.users.find_one_and_update({"_id": ObjectId(user.id)}, {
        "$set": dict(user)
    })

    condition = {
    "customer_id": user.id
    } if user.user_type == 'customer' else {
        "worker_id": user.id
    }

    # Define the fields to update
    update_fields = {
        "$set": {
            "customer_name": user.username,
            "email": user.email,
        } if user.user_type == 'customer' else {
            "worker_name": user.username,
        }
    }

    # Perform the update operation
    res = db.advertisements.update_many(condition, update_fields)

    # Print the number of documents updated
    print(f"Number of documents updated: {res.modified_count}")

    res = db.users.find_one({"_id": ObjectId(user.id)})
    return {
            "name": res["username"],
            "email": res["email"],
            "phone": res['phone'] if res["phone"] else None,
            "user_type": res["user_type"],
            "job_types": res["job_types"] if res["user_type"] == "worker" else None,
            "id": str(res['_id']),
            "profile_picture": res['profile_picture'] if res["profile_picture"] else None,
            "rating": res['rating'] if res["rating"] else None
        }

