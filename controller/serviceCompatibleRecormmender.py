import joblib
import pandas as pd

async def serviceCompatibleRecormmender(weather_data):
    print("<===== service Compatible Recormmender =====>")
    # Load model
    load_mode = joblib.load('ai_models/LogisticRegression.pickle')
    
    df = pd.DataFrame({'temp': [weather_data.temp], 'windspeed': [weather_data.windspeed], 'humidity': [weather_data.humidity],'rain_sum': [weather_data.rain_sum], 'latitude': [weather_data.latitude], 'longitude': [weather_data.longitude], 'work_type': [weather_data.work_type]})
    print(df)

    sample = df.iloc[:,:].values 

    # Make prediction
    prediction = load_mode.predict(sample)
    print(prediction)
    
    # Convert the prediction to a standard Python integer
    prediction_value = int(prediction[0])
    
    return {"prediction": prediction_value}
