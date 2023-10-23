from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from filters import IsPrivate

from loader import dp
from data.config import ADMINS


@dp.message_handler(IsPrivate(),CommandHelp(), user_id=ADMINS[0])
async def bot_helpAdmin(message: types.Message):
    text = "/new_post - Kanalga yangi post joylash\n/set_photo - Guruh rasmini o'zgartirish\n"
    text += "/set_description - Guruh descriptionini o'zgartirish\n/allusers - botdan nechta foydalanuvchi foydalanishi haqida ma'lumot\n"    
    text += "/reklama - Har bir foydalanuvchiga bot orqali reklama yuborish"
    await message.answer(text)



            
            # types.BotCommand("set_photo", "Guruh rasmini o'zgartirish"),
            # types.BotCommand("set_title", "Guruh nomini o'zgartirish"),
            # types.BotCommand("set_description", "Guruh descriptionini o'zgartirish"),