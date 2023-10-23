from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_Data import portfoli_callback


portfoliomenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="GitHub", url="https://github.com/dostonshernazarov"),
        InlineKeyboardButton(text="LinkedIn", url="https://www.linkedin.com/feed/?trk=404_page"),],
        [InlineKeyboardButton(text="Kaggle", url="https://www.kaggle.com/shernazarovdoston"),
        InlineKeyboardButton(text="Repit", url="https://replit.com/@DostonShernazar"),],
        [InlineKeyboardButton(text="↪ Ulashish", switch_inline_query="Zo'r bot ekan!")],
        
    ]
)