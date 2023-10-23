from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from data.config import ADMINS
from filters import IsPrivate
from states.admin import Reklama
from keyboards.inline.new_post import config_keyboard, post_callback, reklama_types, reklama_types_callback

import time

from loader import dp, bot, db


@dp.message_handler(IsPrivate(),Command("allusers"), user_id=ADMINS[0])
async def countUsers(message: types.Message):
    count = db.count_users()[0]
    await message.answer(f"Botdagi foydalanuvchilar soni {count} ta.")

@dp.message_handler(IsPrivate(), text="/reklama", user_id=ADMINS[0])
async def getReklama(message: types.Message):
    await message.answer("Reklama yuboring")
    await Reklama.reklama.set()


@dp.message_handler(content_types=types.ContentType.PHOTO, state=Reklama.reklama)
async def reklama(message:types.Message ,state:FSMContext):
    global PHOTO_ID
    PHOTO_ID = message.photo[-1].file_id
    await message.answer("Rasm osti matnini kiriting!")
    await Reklama.photo_reklama_text.set()

@dp.message_handler(state=Reklama.photo_reklama_text)
async def checkReklama(message: types.Message):
    global MESSAGE
    MESSAGE = str(message.text)
    await message.answer_photo(PHOTO_ID, caption=MESSAGE)
    await message.answer("Reklamani foydalanuvchilarga yuborasizmi?", reply_markup=config_keyboard)
    await Reklama.photo_config.set()


@dp.message_handler(content_types=types.ContentType.TEXT, state=Reklama.reklama)
async def reklama_text(message:types.Message ,state:FSMContext):
    global MESSAGE_TEXT
    MESSAGE_TEXT = str(message.text)
    await message.answer(MESSAGE_TEXT)
    await message.answer("reklamani foydalanuvchilarga yuboraymi?", reply_markup=config_keyboard)
    await Reklama.config.set()


@dp.callback_query_handler(post_callback.filter(action="post"), state=Reklama.config)
async def configReklama(call: types.CallbackQuery, state: FSMContext):
    

    users = db.select_all_users()
    for user in users:
        user_id = user[0]
        await bot.send_message(chat_id=user_id, text=MESSAGE_TEXT)
        time.sleep(1)
    
    count = db.count_users()[0]
    await bot.send_message(chat_id=ADMINS[0], text=f"Reklama {count} ta foydalanuvchiga yuborildi")
    await state.finish()

@dp.callback_query_handler(post_callback.filter(action="cancel"), state=Reklama.config)
async def configPost(call: types.CallbackQuery, state: FSMContext):
    
    await bot.send_message(chat_id=ADMINS[0], text = "Reklama bekor qilindi!")
    await state.finish()


@dp.callback_query_handler(post_callback.filter(action="post"), state=Reklama.photo_config)
async def configReklama(call: types.CallbackQuery, state: FSMContext):
    

    users = db.select_all_users()
    for user in users:
        user_id = user[0]
        await bot.send_photo(chat_id=user_id, photo=PHOTO_ID, caption=MESSAGE)
        time.sleep(1)
    
    count = db.count_users()[0]
    await bot.send_message(chat_id=ADMINS[0], text=f"Reklama {count} ta foydalanuvchiga yuborildi")
    await state.finish()

@dp.callback_query_handler(post_callback.filter(action="cancel"), state=Reklama.photo_config)
async def configPost(call: types.CallbackQuery, state: FSMContext):
    
    await bot.send_message(chat_id=ADMINS[0], text = "Reklama bekor qilindi!")
    await state.finish()




    
