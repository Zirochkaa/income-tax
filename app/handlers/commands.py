from aiogram import types

from app.bot import dp
from app.loggers import handlers_commands_log as logger
from app.texts import start_text


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    logger.error(f"/start:\n{message}\n---")
    await message.answer(text=start_text)
