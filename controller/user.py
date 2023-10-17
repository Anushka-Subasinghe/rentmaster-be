import bcrypt
from typing import List, Dict

from fastapi import HTTPException, status
from models.user import User, LoginData
from schemas.serialize import serializeDict, serializeList
from config.db import db
from bson import ObjectId


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
            "salt": salt
        }
        inserted_result = db.users.insert_one(dict(user))
        res = db.users.find_one({"_id": inserted_result.inserted_id})
        return {
            "name": res["username"],
            "email": res["email"],
            "user_type": res["user_type"],
            "job_types": res["job_types"] if res["user_type"] == "worker" else None,
            "id": str(res['_id'])
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="User with this email already exists. Please use a different email.")


def getAll():
    print("<===== Get All User =====>")
    return serializeList(db.users.find())


def getOne(id):
    print("<===== getLastOne =====>")
    res = serializeDict(db.users.find_one({"_id": ObjectId(id)}))
    print(res)
    return res


def update(user: User):
    db.users.find_one_and_update({"email": user.email}, {
        "$set": dict(user)
    })
    inserted_doc = db.users.find_one({"email": user.email})
    return serializeDict(inserted_doc)


def delete(user: User):
    result = db.users.delete_one({"email": user.email})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"status_code": 200, "detail": "User Deleted"}


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


def login(loginData: LoginData):
    res = verify_user(loginData)
    if res:
        return {
            "name": res["username"],
            "email": res["email"],
            "user_type": res["user_type"],
            "job_types": res["job_types"] if res["user_type"] == "worker" else None,
            "id": str(res['_id'])
        }
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="Login failed. Invalid username or password.")
