from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.user import user
from routes.advertisement import advertisement

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

app.include_router(user)
app.include_router(advertisement)
print("<============== Server started ==============>")
