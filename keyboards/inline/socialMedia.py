from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_Data import socialMedia_callback


socialMedia = {
    "Instagram":"instagram_account",
    "Facebook":"facebook_account",
    "Telegram":"telegram_account",
    "Gmail":"gmail_account"
}

socialMedia_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/doston_shernazarov_/"),
        InlineKeyboardButton(text="Facebook", url="https://www.facebook.com/doston.shernazarov.50"),],
        [InlineKeyboardButton(text="Telegram", url="https://t.me/dostonshernazarov_blog"),
        InlineKeyboardButton(text="Gmail", url="dostonshernazarov2001@gmail.com"),],
        [InlineKeyboardButton(text="↪ Ulashish", switch_inline_query="Zo'r bot ekan!")],
        
    ]
)


# for key, value in socialMedia.items():
#     socialMedia_menu.insert(InlineKeyboardButton(text=key, callback_data=socialMedia_callback.new(item_name = value)))


# instagramKeyboard = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="Instagram", callback_data=socialMedia_callback.new(item_name ="instagram_account"), url="https://www.instagram.com/doston_shernazarov_/")]
# ])


# facebookKeyboard = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="Aytmeman :)", callback_data=socialMedia_callback.new(item_name ="facebook_account"))]

# ])

# telegramKeyboard = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="Telegram ", callback_data=socialMedia_callback.new(item_name ="telegram_account"), url="https://t.me/shernazarov_doston")]

# ])

# gmailKeyboard = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="Gmail ", callback_data=socialMedia_callback.new(item_name ="gmail_account"), url="dostonshernazarov2001@gmail.com")]

# ])
# socialMedia_menu.insert(instagramKeyboard)
# socialMedia_menu.insert(facebookKeyboard)
# socialMedia_menu.insert(telegramKeyboard)
# socialMedia_menu.insert(gmailKeyboard)


