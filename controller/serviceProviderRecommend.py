import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
from controller.worker import getAll

async def recommend_providers():
    
    workers = getAll()
    
    # Convert MongoDB documents to a list of dictionaries
    dataList = [doc for doc in workers]
    
    # Convert data to a DataFrame
    data = pd.DataFrame(dataList)
    
    # Drop non-numeric columns and scale the numeric features
    scaler = StandardScaler()
    data['rating'] = scaler.fit_transform(data[['rating']])
    X = data[['rating']]
    
    # Create KNN model
    k = 3  # Number of neighbors to consider
    knn_model = NearestNeighbors(n_neighbors=k, metric='euclidean')

    # Fit the model to the scaled data
    knn_model.fit(X)

    # Sample customer's rating (replace with actual customer's rating)
    customer_rating = 4.2

    # Scale the customer's rating
    scaled_customer_rating = scaler.transform([[customer_rating]])

    # Find the k nearest neighbors
    distances, indices = knn_model.kneighbors(scaled_customer_rating)

    # Get recommended providers by returning their details
    recommended_providers = data.iloc[indices[0]]
    
    # Convert recommended_providers to a list of dictionaries
    recommended_providers_list = recommended_providers.to_dict(orient="records")
    print(recommended_providers_list)
    return recommended_providers_list
