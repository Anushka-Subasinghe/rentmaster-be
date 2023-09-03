from fastapi import APIRouter
from controller.chatbot import chatbot_response, getAll
from models.chatbot import Chatbot

chatbot = APIRouter()

@chatbot.post('/chatbot')
async def chat_bot(chat: Chatbot):
    return chatbot_response(chat)

@chatbot.get('/chatbot')
async def get_all_chats():
    chats = getAll()
    return chats

