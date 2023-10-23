from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import ADMINS
from filters import IsPrivate
from keyboards.default import menuKeyboard

from loader import dp, bot, db

@dp.message_handler(IsPrivate(), CommandStart(), user_id=ADMINS[0])
async def adminStart(message: types.Message):
    await message.answer(f"Xush kelibsiz admin!", reply_markup=menuKeyboard.menu)