from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


contact = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text="Contact yuborish", request_contact=True)]
    ], resize_keyboard=True
)