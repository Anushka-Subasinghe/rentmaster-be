from fastapi import APIRouter
from controller.job import create, getOne, getAll, update, delete
from models.job import Job

job = APIRouter()

@job.post('/job')
async def create_job(job: Job):
    return create(job)

@job.get('/job/{job_id}')
async def get_job_by_id(job_id: str):
    return getOne(job_id)

@job.delete('/job/{job_id}')
async def delete_job(job_id: str):
    return delete(job_id)

@job.put('/job/{job_id}')
async def update_job(job_id: str, updated_job: Job):
    return update(job_id, updated_job)
    
@job.get('/jobs')
async def get_all_jobs():
    return getAll()
