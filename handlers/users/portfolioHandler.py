from aiogram.dispatcher.filters import Command, Text
from keyboards.default.portfolioKeyboard import portfolio
from keyboards.inline.portfoliokeyboard import portfoliomenu, portfoli_callback
from filters.private_chat import IsPrivate

from aiogram.types import Message, ReplyKeyboardRemove
from loader import dp

msg = "Kerakli tugmani tanlang!"

@dp.message_handler(IsPrivate(), text="💼 Portfolio")
async def def_portfolio(message: Message):
    await message.answer(msg, reply_markup=portfoliomenu)

# @dp.message_handler(text="GitHub")
# async def def_github(message: Message):
#     await message.answer("https://github.com/dostonshernazarov")
    
# @dp.message_handler(text="LinkedIn")
# async def def_linkidin(message: Message):
#     await message.answer("https://www.linkedin.com/feed/?trk=404_page")
    
# @dp.message_handler(text="Kaggle")
# async def def_kaggle(message: Message):
#     await message.answer("https://www.kaggle.com/shernazarovdoston")
    
# @dp.message_handler(text="Replit")
# async def def_replit(message: Message):
#     await message.answer("https://replit.com/@DostonShernazar")

# @dp.message_handler(text="Boshiga")
# async def def_portfolio(message: Message):
#     await message.answer(msg, reply_markup=menu)




