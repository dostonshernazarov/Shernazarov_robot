from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery, Message

from data.config import ADMINS, CHANNELS
from keyboards.inline.new_post import config_keyboard, post_callback
from loader import dp, bot
from states.new_post import NewPost
from filters.private_chat import IsPrivate

# admin = False
@dp.message_handler(IsPrivate(),Command("new_post"))
async def createPost(message: types.Message):
    await message.answer("Chop etish uchun post yuboring!")
    await NewPost.NewMessage.set()

@dp.message_handler(state=NewPost.NewMessage)
async def getMessage(message: Message, state: FSMContext):
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    await message.answer("Postni tekshirish uchun yuboraymi?", reply_markup=config_keyboard)
    await NewPost.next()

@dp.callback_query_handler(post_callback.filter(action="post"), state=NewPost.Config)
async def configPost(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        text = data.get("text")
        mention = data.get("mention")
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Post adminga yuborildi")
    await bot.send_message(ADMINS[0], f"Foydalanuvchi {mention} quyidagi postni chop etmoqchi:")
    await bot.send_message(ADMINS[0], text, parse_mode="HTML", reply_markup=config_keyboard)

@dp.callback_query_handler(post_callback.filter(action="cancel"), state=NewPost.Config)
async def cancelPost(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Post rad etildi!")

@dp.message_handler(state=NewPost.NewMessage)
async def post_unknown(message: Message):
    await message.answer("'Chop etish' yoki 'Rad etish' tugmasini bosing!")

@dp.callback_query_handler(post_callback.filter(action="post"), user_id=ADMINS[0])
async def post(call: CallbackQuery):
    await call.answer("Chop etishga ruxsat berdingiz!", show_alert=True)
    target_channel = CHANNELS[0]
    message = await call.message.edit_reply_markup()
    await message.send_copy(target_channel)

@dp.callback_query_handler(post_callback.filter(action="cancel"), user_id=ADMINS[0])
async def cancel(call: CallbackQuery):
    await call.answer("Rad etishga ruxsat berdingiz!", show_alert=True)
    await call.message.edit_reply_markup()
