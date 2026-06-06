import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from app.bot.handlers.start import router as start_router

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

print("Bot launched successfully!")


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
