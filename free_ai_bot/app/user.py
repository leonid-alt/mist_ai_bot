from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

from app.database.requests import set_user
# from middlewares import BaseMiddleware
from app.generators import generate
user = Router()

# user.message.middleware(BaseMiddleware())

@user.message(CommandStart())
async def cmd_start(message: Message):
    await set_user(message.from_user.id)
    await message.answer('Добро пожаловать в бот с ИИ!')

@user.message()
async def ai(message: Message):
    res = await generate(message.text)
    print(res.choices[0].message.content)
    await message.answer(res.choices[0].message.content)
