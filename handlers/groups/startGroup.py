from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import Message
from filters.group_chat import IsGroup

from loader import dp

@dp.message_handler(IsGroup(), CommandStart())
async def startGroup(message: Message):
    await message.answer(f"Qani boshladik bo'lmasa!")