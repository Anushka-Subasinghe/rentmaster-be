import joblib
import numpy as np
import pandas as pd
from typing import List, Dict
from models.location import Location
from datetime import datetime
from helper.loadReasons import getResons
from helper.loadLocations import getLocations

# Load the trained model
model = joblib.load("controller/DecisionTreeClassifierModel.pickle")

week_day_mapping = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}
day_mapping = {"Morning": 0, "Afternoon": 1, "Evening": 2, "Night": 3}

def locationPreditor(location: Location):
    
    date = "3/5/2023" # location.date
    day_of_week = "Sunday"
    time_of_day = "Morning"
    s_reason = "Medicine"
    reason_to_number = getResons()
    
    numeric_date = pd.to_datetime(date, format='%m/%d/%Y')
    numeric_date = (numeric_date - pd.Timestamp('1970-01-01')).days

    day_of_week = week_day_mapping[day_of_week]
    time_of_day = day_mapping[time_of_day]

    if s_reason in reason_to_number:
        s_reason = reason_to_number[s_reason]
    else:
        s_reason = len(reason_to_number)

    df = pd.DataFrame({'Date': [numeric_date], 'Day of the Week': [day_of_week], 'Time of the Day': [time_of_day], 'Reason': [s_reason]})

    sample = df.iloc[:,:].values 
    
    location_arr = getLocations()

    predict_res = model.predict(sample)
    print('predic', predict_res)
    print("Predict Location : ", location_arr[predict_res[0]])
        
def locationsPredictor(result: List[Location]):
    
    
    data = []
    for res in result:
        data.append(
            {
                "exam": res.exam,
                "test": res.test,
                "quize": res.quize,
                "grade": res.grade,
                "name": res.name,
                "result": res.result,
                "student_id": res.student_id
            }
        )

    df = pd.DataFrame(data, columns=["exam", "test", "quize", "grade", "name", "result", "student_id"])
    print(df)

    sample = df.iloc[:,:3].values 
    print(sample)
    predict_res = model.predict(sample)

    df["result"] = predict_res
    print('result', df)

    return df.to_dict(orient='records')
