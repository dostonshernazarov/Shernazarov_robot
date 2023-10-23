from aiogram.dispatcher.filters.state import State, StatesGroup


class FikrData(StatesGroup):
    fikr = State()
    fikrNum = State()