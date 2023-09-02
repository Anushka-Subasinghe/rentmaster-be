# Import necessary libraries
import numpy as np
import pandas as pd

def getResons():
    data = pd.read_csv("datasets/Dataset_Locations.csv")
    
    data = data[~(data['Date'] == 0)]
    data = data[~(data['Day of the Week'] == 0)]
    data = data[~(data['Time of the Day'] == 0)]
    data = data[~(data['Location'] == 0)]
    data = data[~(data['Reason'] == 0)]
    
    # remove null values
    null_rows = data.isnull().any(axis=1)  # Check if any value in each row is null
    data = data[~(null_rows)]
    data.shape
    
    # Remove duplicate rows
    data = data.drop_duplicates(subset=['Date', 'Day of the Week', 'Time of the Day', 'Location', 'Reason'])

    reasons = data['Reason'].value_counts()
    reason_to_number = {}

    for index, label in enumerate(reasons.index):
        reason_to_number[label] = index
    
    return reason_to_number
