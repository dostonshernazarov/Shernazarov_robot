from aiogram.dispatcher.filters.builtin import CommandHelp
from aiogram.types import Message
from filters.group_chat import IsGroup

from loader import dp

@dp.message_handler(IsGroup(), CommandHelp())
async def helpGroup(message: Message):
    await message.answer(f"Salom, {message.from_user.full_name} sizga qanday yordam bera olaman?")