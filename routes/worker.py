from fastapi import APIRouter
from controller.worker import create, getOne, getAll, update, delete
from models.user import Worker

worker = APIRouter()

@worker.post('/worker')
async def create_worker(worker: Worker):
    return create(worker)

@worker.get('/worker/{worker_id}')
async def get_worker_by_id(worker_id: str):
    return getOne(worker_id)

@worker.delete('/worker/{worker_id}')
async def delete_worker(worker_id: str):
    return delete(worker_id)

@worker.put('/worker/{worker_id}')
async def update_worker(worker_id: str, updated_worker: Worker):
    return update(worker_id, updated_worker)
    
@worker.get('/workers')
async def get_all_workers():
    return getAll()
