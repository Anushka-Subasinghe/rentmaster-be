from fastapi import APIRouter
from controller.customerRecommendation import recommend_customers
from controller.serviceProviderRecommend import recommend_providers
from controller.serviceCompatibleRecormmender import serviceCompatibleRecormmender
from models.weather import Weather

recommend = APIRouter()

@recommend.get('/recommend/customers/{advertisment_job}')
async def recommend_cust(advertisment_job: str):
    return await recommend_customers(advertisment_job)

@recommend.get('/recommend/providers/')
async def recommend_service_providers():
    return await recommend_providers()

@recommend.post('/recommend/weathre')
async def recommend_work_compatible(weather: Weather):
    return await serviceCompatibleRecormmender(weather)
