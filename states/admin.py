from aiogram.dispatcher.filters.state import State, StatesGroup

class Reklama(StatesGroup):
    reklama = State()
    photo_reklama_photo = State()
    photo_reklama_text = State()
    photo_config = State()
    config = State()