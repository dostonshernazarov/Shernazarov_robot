from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from filters import IsPrivate

from loader import dp
from data.config import ADMINS


@dp.message_handler(IsPrivate(),CommandHelp())
async def bot_help(message: types.Message):
    text = ("Ushbu bot <a href='https://t.me/dostonshernazarov_blog'>Doston Shernazarov</a> kanalining yordamchi robot boti! ")
    
    await message.answer(text)

