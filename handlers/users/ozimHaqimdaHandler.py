from aiogram.dispatcher.filters import Command, Text
# from keyboards.default.portfolioKeyboard import portfolio
from keyboards.default.menuKeyboard import menu
from filters.private_chat import IsPrivate
from data.config import ABOUT_MYSELF

from aiogram.types import Message, ReplyKeyboardRemove
from loader import dp

msg = "Kerakli tugmani tanlang!"

@dp.message_handler(IsPrivate(), text="👨‍💻 O'zim haqimda")
async def ozimHaqimda(message: Message):
    await message.answer(ABOUT_MYSELF, disable_web_page_preview=True)