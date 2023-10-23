from aiogram.dispatcher.filters import Command, Text
from keyboards.default.menuKeyboard import menu
from keyboards.default.contactKeyboard import contact
from keyboards.default.cancel import cancel
from states.dataState import PersonalData
from aiogram.dispatcher import FSMContext
from filters.private_chat import IsPrivate
from states.fikrState import FikrData

from data.config import ADMINS
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from loader import dp, bot

# global fikr
# global number

@dp.message_handler(IsPrivate(), text="📝 Fikr-mulohaza. A'loqa")
async def boglanishHandler(message: Message):
    await message.answer("Fikr yoki shikoyatingizni yozing", reply_markup=cancel)
    await FikrData.fikr.set()

@dp.message_handler(state=FikrData.fikr)
async def fikr_func(message: Message):
    
    global fikr
    fikr = str(message.text)
    await message.answer("Telefon raqamingizni yuboring! (91-321-44-55)", reply_markup=cancel)
    await FikrData.fikrNum.set()

@dp.message_handler(text="❌ Bekor qilish")
async def cancel_boglanish(call:CallbackQuery, state:FSMContext):
    await call.answer("Buyruq bekor qilindi!")
    await state.finish()
    
@dp.message_handler(state=FikrData.fikrNum)
async def fikrNum_func(message: Message, state: FSMContext):
    global number
    number = str(message.text)
    await message.answer("Rahmat. Fikringiz adminga yetkazildi!")
    await state.finish()
    try:
        await bot.send_message(ADMINS[0], f"<b>Fikr-mulohaza</b>\nText:{fikr}\n\nTel: {number}\nFullname: {message.from_user.full_name}\nUsername: @{message.from_user.username}")
    except:
        await bot.send_message(ADMINS[0], f"<b>Fikr-mulohaza</b>\nText:{fikr}\n\nTel: {number}\nFullname: {message.from_user.full_name}")
    

    # await PersonalData.fullname.set()

# @dp.message_handler(state=FikrData.fikrAdmin)
# async def fikr_func(message: Message, call: FSMContext):
#     await bot.send_message(746586147, f"fikr:{fikr}\n.tel. raqam:{number}")
#     await call.finish()


# @dp.message_handler(state=PersonalData.fullname)
# async def getName(message: Message, state: FSMContext):
#     fullname = message.text
#     await state.update_data(
#         {"name":fullname}
#     )
#     await message.answer("Telifon raqamingizni kiriting!")
#     await PersonalData.phoneNum.set()

# @dp.message_handler(state=PersonalData.phoneNum)
# async def getNumber(message: Message, state: FSMContext):
#     number = message.text
#     await state.update_data(
#         {"number":number}
#         )
    
#     data = await state.get_data()
#     userName = data.get("name")
#     userNumber = data.get("number")
#     # with open("users.txt", "a") as file:
#     #     file.write(f"name:{userName}, number:{userNumber}\n")

#     await message.answer(f"{userName} Sizga tez orada {userNumber} ga a'loqaga chiqishadi!")
    
#     await state.finish()
