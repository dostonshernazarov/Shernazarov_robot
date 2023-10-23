import sqlite3

from data.config import ADMINS

from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menuKeyboard import menu
from filters import IsPrivate
from data.config import CHANNELS
from keyboards.inline.subscription import check_button
from utils.misc import subscription

from loader import dp, bot, db


# @dp.message_handler(IsPrivate(),CommandStart())
# async def bot_start(message: Message):
#     channel_format = str()
#     for channel in CHANNELS:
#         chat = await bot.get_chat(channel)
#         invite_link = await chat.export_invite_link()
#         channel_format += f"👉🏻 <a href = '{invite_link}'>{chat.title}</a>\n"

#     await message.answer(f"Botdan foydalanish uchun quyidagi kanallarga obuna bo'ing:\n"
#                          f"{channel_format}", reply_markup=check_button, disable_web_page_preview=True)
    
# @dp.callback_query_handler(text="check_sub")
# async def checker(call: CallbackQuery):
#     await call.answer()
#     result = str()
#     for channel in CHANNELS:
#         status = await subscription.check(user_id=call.from_user.id, channel=channel)

#         channel = await bot.get_chat(channel)
#         if status:
#             result += f"✅ <b>{channel.title}</b> kanalga obuna bo'lgansiz!\n\n"
            
#         else:
#             invite_link = await channel.export_invite_link()
#             result += (f"❌ <b>{channel.title}</b> kanaliga obuna bo'lmagansiz. "
#                        f"<a href='{invite_link}'> obuna bo'lish</a>\n\n")
            
#     await call.message.answer(result, reply_markup=menu,disable_web_page_preview=True)

@dp.message_handler(IsPrivate(),CommandStart())
async def bot_start(message: Message):
    name = message.from_user.full_name

    #foydalanuvchini bazaga qo'shish
    try:
        db.add_user(id=message.from_user.id, name=name)
    except sqlite3.IntegrityError as err:
        pass

    await message.answer(f"Assalomu alaykum {message.from_user.full_name}.\n<a href='https://t.me/doston_shernazarov'>Doston shernazarov</a> kanalining robot botiga xush kelibsiz!", reply_markup=menu, disable_web_page_preview=True)

    # adminga habar berish
    count = db.count_users()[0]
    msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} f\ta foydalanuvchi bor."
    await bot.send_message(chat_id=ADMINS[0], text=msg)
