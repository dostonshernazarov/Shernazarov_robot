from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

post_callback = CallbackData("create_post", "action")

reklama_types_callback = CallbackData("create_post", "action")

config_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="🆗 Chop etish", callback_data=post_callback.new(action="post")),
        InlineKeyboardButton(text="❌ Rad etish", callback_data=post_callback.new(action="cancel"))
    ]]
)

reklama_types= InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="Photo and text", callback_data=reklama_types_callback.new(action="photo")),
        InlineKeyboardButton(text="Text", callback_data=reklama_types_callback.new(action="text"))
    ]]
)