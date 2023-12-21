from logging.config import dictConfig

from aiogram import types, Dispatcher, Bot
from fastapi import FastAPI

from app.bot import dp, bot
from app.config import settings
from app.log_config import log_config
from app.loggers import run_log as logger

dictConfig(log_config)


app = FastAPI(
    title="Income tax calculator",
    description="Calculate income tax for United Kingdom.",
    version="0.0.1",
    docs_url="/api/docs",
)


@app.on_event("startup")
async def on_startup():
    logger.info("On startup things.")

    # Below import is required because handlers for commands has to be loaded.
    # Otherwise, sending commands will result in nothing.
    import app.handlers  # noqa: F401


@app.post('/set_webhook')
async def set_webhook():
    logger.info(f"app_base_url={settings.app_base_url}.")  # TODO Remove
    logger.info(f"telegram_webhook_url={settings.telegram_webhook_url()}.")  # TODO Remove

    webhook_info = await bot.get_webhook_info()
    logger.info(f"webhook_info: {webhook_info}.")

    webhook_url = settings.telegram_webhook_url()
    if webhook_info.url != webhook_url:
        assert (
                await bot.set_webhook(url=webhook_url) is True
        ), "Result of `set_webhook` has to be `True`."
        webhook_info = await bot.get_webhook_info()
        logger.info(f"webhook_info updated: {webhook_info}.")
        return {'new': webhook_url}

    return {'existing': webhook_info.url}


@app.post(settings.telegram_webhook_path(), include_in_schema=False)
async def bot_webhook(update: dict):
    logger.info(f"Update object: {update}.")
    telegram_update = types.Update(**update)
    Dispatcher.set_current(dp)
    Bot.set_current(bot)
    await dp.process_update(telegram_update)


@app.on_event("shutdown")
async def on_shutdown():
    logger.info("On shutdown things.")
    session = await bot.get_session()
    await session.close()
