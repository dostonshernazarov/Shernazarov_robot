from aiogram import Dispatcher
from loader import dp

from .admins import AdminFilter
from .group_chat import IsGroup
from .private_chat import IsPrivate


if __name__ == "filters":
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(IsGroup)
    dp.filters_factory.bind(IsPrivate)

    # @dp.message_handler(AdminFilter())
    # async def admin_chat(message: types.Message):
    #     await message.reply("You are an admin!")