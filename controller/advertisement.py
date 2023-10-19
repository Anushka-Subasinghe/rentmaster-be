import json
from fastapi import HTTPException, status
from typing import List, Dict
from models.advertisement import AcceptAdvertisement, Advertisement, BidAdvertisement, CancelBid, CancelJob, SelectWorker
from schemas.serialize import serializeDict, serializeList
from config.db import db
from bson import ObjectId
from fastapi.encoders import jsonable_encoder
import pandas as pd
import joblib
import os

def predict(input_data):
    try:
        print(input_data)
        
        # Convert the input data into a DataFrame
        input_df = pd.DataFrame([input_data])

        print("Current working directory:", os.getcwd())

        loaded_best_model = joblib.load(os.getcwd() + '/controller/model.pkl')
        
        # Make predictions using the loaded model
        predictions = loaded_best_model.predict(input_df)

        predicted_value = int(predictions[0])

        print('prediction ${predicted_value}')
        
        # Return the predicted value
        return predicted_value == 1
    except Exception as e:
        print('error', e)
        return None

def post_advertisement(advertisement: Advertisement):
    print("<===== Create Advertisement =====>")
    user = db.users.find_one({"email": advertisement.email})
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found."
        )
    
    forecast = advertisement.forecast
    
    weather = {
        "temperature": forecast.temperature,
        "windspeed": forecast.windspeed,
        "humidity": forecast.humidity,
        "work_type": advertisement.work_type
    }

    prediction = predict(weather)

    # Create the job document
    advertisement = {
        "job_type": advertisement.job_type,
        "date": advertisement.date,
        "time": advertisement.time,
        "email": advertisement.email,
        "status": advertisement.status,
        "latitude": advertisement.latitude,
        "longitude": advertisement.longitude,
        "forecast": jsonable_encoder(forecast),
        "customer_name": user["username"],
        "customer_id": str(user["_id"]),
        "prediction": prediction,
        "bid": [],
        "selectedWorkers": []
    }

    # Insert the job into the database
    inserted_result = db.advertisements.insert_one(advertisement)
    inserted_advertisement = db.advertisements.find_one({"_id": inserted_result.inserted_id})

    return serializeDict(inserted_advertisement)
    
def getAll():
    print("<===== Get All Advertisement =====>")
    return serializeList(db.advertisement.find())

def getAdvertisementsByCustomer(email: str):

    # Query the database to find all advertisements with the specified email
    advertisements = db.advertisements.find({"email": email})

    # Convert the MongoDB cursor to a list of dictionaries excluding _id
    advertisements_list = []
    for ad in advertisements:
        ad['_id'] = str(ad['_id'])
        advertisements_list.append(ad)

    if advertisements_list:
        return json.dumps({"advertisements": advertisements_list})
    else:
        return json.dumps({"advertisements": []})
    
def getAdvertisementsByJobType(job_types: list):

    # Query the database to find all advertisements with the specified job types
    advertisements = db.advertisements.find({"job_type": {"$in": job_types}})

    # Convert the MongoDB cursor to a list of dictionaries excluding _id
    advertisements_list = []
    for ad in advertisements:
        ad['_id'] = str(ad['_id'])
        advertisements_list.append(ad)

    if advertisements_list:
        return json.dumps({"advertisements": advertisements_list})
    else:
        return json.dumps({"advertisements": []})   

def accept_advertisement(update: AcceptAdvertisement):
    print("<===== update Advertisement =====>")
    db.advertisements.find_one_and_update(
        {"_id": ObjectId(update.id)},
    {"$set": {"status": "Accepted", "worker_name": update.worker_name, "worker_id": update.worker_id, "price": update.price, "bid": []}})
    
    inserted_doc = db.advertisements.find_one({"_id": ObjectId(update.id)})
    return serializeDict(inserted_doc)

def cancel_job(cancel: CancelJob):
    print("<===== cancel Job =====>")
    db.advertisements.find_one_and_update(
        {"_id": ObjectId(cancel.id)},
    {"$set": {
    "status": "Active",
    "worker_name": "",
    "worker_id": "",
    "price": "",
    "bid": []
  }})
    
    inserted_doc = db.advertisements.find_one({"_id": ObjectId(cancel.id)})
    return serializeDict(inserted_doc)


def bid_advertisement(bid: BidAdvertisement):
    print("<===== bid Advertisement =====>")
    db.advertisements.find_one_and_update(
        {"_id": ObjectId(bid.id)},
    {"$push": {"bid": {"worker_name": bid.worker_name, "worker_id": bid.worker_id, "price": bid.price}}})
    
    inserted_doc = db.advertisements.find_one({"_id": ObjectId(bid.id)})
    return serializeDict(inserted_doc)

def cancel_bid(bid: CancelBid):
    print("<===== Cancel Bid =====>")
    db.advertisements.find_one_and_update(
        {"_id": ObjectId(bid.id)},
    {"$pull": {"bid": {"worker_id": bid.worker_id}}})
    inserted_doc = db.advertisements.find_one({"_id": ObjectId(bid.id)})
    return serializeDict(inserted_doc)

def delete_advertisement(id: str):
    print("<===== delete Advertisement =====>", id)
    result = db.advertisements.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Advertisement not found")
    return {"status_code": 200, "detail": "Advertisement Deleted" }

def select_worker(worker: SelectWorker):
    print("<===== Select Worker =====>")
    filter = {"_id": ObjectId(worker.id)}
    update = {"$push": {"selectedWorkers": jsonable_encoder(worker)}}
    
    result =db.advertisements.find_one_and_update(filter, update)
    
    inserted_doc = db.users.find_one({"_id": ObjectId(worker.worker_id)})
    return serializeDict(inserted_doc)