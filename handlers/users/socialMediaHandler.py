from aiogram.dispatcher.filters import Command, Text
# from keyboards.default.socialMediaKeyboard import socialMedia 
from keyboards.inline.socialMedia import socialMedia_menu
from keyboards.inline.callback_Data import socialMedia_callback
from filters.private_chat import IsPrivate

from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from loader import dp



@dp.message_handler(IsPrivate(), text="🌐 Social media")
async def socialMedia(message: Message):
    await message.answer("Kerakli tugmani tanlang", reply_markup=socialMedia_menu)

# @dp.callback_query_handler(text = "cancel")
# async def canlec(call:CallbackQuery):
#     await call.message.edit_reply_markup(reply_markup=socialMedia_menu)
#     await call.answer()


# @dp.callback_query_handler(socialMedia_callback.filter(item_name = "instagram_account"))
# async def showInstagram(call:CallbackQuery):
#     await call.message.answer("Instagram account", reply_markup=instagramKeyboard)
#     await call.message.delete()

    
# @dp.message_handler(text="Instagram")
# async def def_insta(message: Message):
#     await message.answer("https://www.instagram.com/doston_shernazarov_/")
    
# @dp.message_handler(text="Facebook")
# async def def_insta(message: Message):
#     await message.answer("https://www.facebook.com/doston.shernazarov.50/")
    
# @dp.message_handler(text="Twitter")
# async def def_insta(message: Message):
#     await message.answer("Kechirasizu lekin Twitter sahifanmi ulasha olmayman. 😁 ")
    
# @dp.message_handler(text="Gmail")
# async def def_insta(message: Message):
#     await message.answer("dostonshernazarov2001@gmail.com")


# @dp.message_handler(text="Boshiga")
# async def def_portfolio(message: Message):
#     await message.answer(msg, reply_markup=menu)



