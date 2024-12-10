import logging
import os

from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from database.models import User, MessagesText, create_tables
from settings.settings import BOT_TOKEN
from dotenv import load_dotenv
from aiogram.utils import executor
import asyncio

load_dotenv()
create_tables()

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot)

target_username = None


@dp.message_handler()
async def set_user(message: types.Message):
    user, created = User.get_or_create(
        telegram_id=message.from_user.id,
        defaults={'user_name': message.from_user.username}
    )

    message_record = MessagesText.create(
        message_text=message.text,
        user=user,
        name=message.from_user.username
    )

    print(f"Сообщение от @{message.from_user.username} сохранено в базе данных.")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
