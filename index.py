from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.user import user
from routes.worker import worker
from routes.advertisement import advertisement
from routes.job import job
from routes.booking import booking
from routes.recommend import recommend
from routes.chatbot import chatbot

app = FastAPI()

previous_val = "None"


# Set up CORS
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1:5173/",
    "http://localhost:5173/",
    "http://127.0.0.1:8000/",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Set this to the appropriate origins
    allow_credentials=True,
    allow_methods=["*"],  # Set this to the allowed HTTP methods
    allow_headers=["*"],  # Set this to the allowed headers
)

app.include_router(chatbot)
app.include_router(recommend)
app.include_router(worker)
app.include_router(user)
app.include_router(advertisement)
app.include_router(job)
app.include_router(booking)
print("<============== Server started ==============>")
