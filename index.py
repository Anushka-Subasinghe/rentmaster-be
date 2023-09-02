from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.user import user
from routes.worker import worker
from routes.advertisement import advertisement
from routes.job import job
from routes.booking import booking

app = FastAPI()

previous_val = "None"


# Set up CORS
origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(worker)
app.include_router(user)
app.include_router(advertisement)
app.include_router(job)
app.include_router(booking)
print("<============== Server started ==============>")

