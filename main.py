import asyncio

from aiogram import Dispatcher, Bot

from tgbot.data.config import get_admins, BOT_TOKEN
from tgbot.database.models import Base
from tgbot.database.queries import engine
from tgbot.handlers import register_all_routers


async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    dp = Dispatcher()
    bot = Bot(token=BOT_TOKEN)
    register_all_routers(dp)
    print("~~~~~ Bot was started ~~~~~")
    print("***** ENTER ADMIN ID *****") if len(get_admins()) == 0 else print(f"***** ADMINS: {len(get_admins())} *****")
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
