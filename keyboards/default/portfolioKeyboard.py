from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


portfolio = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="GitHub"),
            KeyboardButton(text="LinkedIn"),
            KeyboardButton(text="Kaggle"),
            KeyboardButton(text="Replit"),
        ],
        [
            KeyboardButton(text="Boshiga")
        ],

    ], resize_keyboard=True
)