from fastapi import APIRouter
from controller.booking import create, getOne, getAll, update, delete
from models.booking import Booking

booking = APIRouter()

@booking.post('/booking')
async def create_booking(booking: Booking):
    return create(booking)

@booking.get('/booking/{booking_id}')
async def get_booking_by_id(booking_id: str):
    return getOne(booking_id)

@booking.delete('/booking/{booking_id}')
async def delete_booking(booking_id: str):
    return delete(booking_id)

@booking.put('/booking/{booking_id}')
async def update_booking(booking_id: str, updated_booking: Booking):
    return update(booking_id, updated_booking)
    
@booking.get('/bookings')
async def get_all_bookings():
    return getAll()
