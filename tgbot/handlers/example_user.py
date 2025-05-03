from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

example_user_router = Router()


@example_user_router.message(CommandStart())
async def user_start(message: Message):
    await message.reply("Вітаю, звичайний користувач!")
