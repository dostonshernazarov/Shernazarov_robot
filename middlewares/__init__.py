from aiogram import Dispatcher

from loader import dp
from .throttling import ThrottlingMiddleware
# from .checkSub import BigBro


if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
    # dp.middleware.setup(BigBro())
