from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from controller.booking import getAll

# When a service provider searches for a job, you can use the KNN model to recommend customers
async def recommend_customers(advertisment_job):
    # Get bookings
    bookings = getAll()
    
    # Convert MongoDB documents to a list of dictionaries
    dataList = [doc for doc in bookings]
    
    # Convert data to a DataFrame
    data = pd.DataFrame(dataList)
    
    # Example for creating TF-IDF vectors for job titles
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_job_titles = tfidf_vectorizer.fit_transform(data['job'])
    
    # Create a KNN model 
    knn_model = NearestNeighbors(n_neighbors=6, metric='cosine')
    knn_model.fit(tfidf_job_titles)

    query_vector = tfidf_vectorizer.transform([advertisment_job])
    _, indices = knn_model.kneighbors(query_vector)
    
    recommended_customers = {}
    
    for idx in indices[0]:
        key = str(idx)  # Convert index to string
        recommended_customers[key] = {
            "worker": {
                "name": data["worker"][key]["name"] if key in data["worker"] else "",
                "mobile": data["worker"][key]["mobile"] if key in data["worker"] else ""
            },
            "customer": {
                "name": data["customer"][key]["name"] if key in data["customer"] else "",
                "mobile": data["customer"][key]["mobile"] if key in data["customer"] else ""
            },
            "start_date": data["start_date"].get(key, ""),
            "end_date": data["end_date"].get(key, ""),
            "start_time": data["start_time"].get(key, ""),
            "end_time": data["end_time"].get(key, ""),
            "district": data["district"].get(key, ""),
            "city": data["city"].get(key, ""),
            "address": data["address"].get(key, ""),
            "location": data["location"].get(key, ""),
            "description": data["description"].get(key, ""),
            "job": data["job"].get(key, ""),
            "_id": key
        }

    return recommended_customers
