# Driver code for the bot
# https://docs.aiogram.dev/en/dev-3.x/
import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

import lib.routers as routers
import lib.services as services
import lib.utils as utils

API_KEY_FP = "./api_key.txt"


def create_bot() -> Bot:
    """
    Creates the Bot object with default configurations
    """
    BOT_KEY: str = utils.api_token_repository.get_telegram_access_token(
        API_KEY_FP)
    return Bot(token=BOT_KEY, default=DefaultBotProperties(
        parse_mode=ParseMode.HTML))


def create_dispatcher() -> Dispatcher:
    """
    Creates the dispatcher object injecting all dependencies as named args
    """
    # Setup the required services for the dispatcher and the routers
    elden_api_service = services.mock_elden_api_service.MockEldenAPIService()

    # Create the dispatcher and inject all the required services
    return Dispatcher(
        elden_api_service=elden_api_service
    )


def include_routers(dispatcher: Dispatcher) -> None:
    """
    Includes routers required by the bot to the dispatcher object
    """
    dispatcher.include_router(routers.onboarding_router.get_router())
    dispatcher.include_router(routers.elden_router.get_router())


async def main() -> None:
    bot = create_bot()
    dispatcher = create_dispatcher()
    include_routers(dispatcher)
    await dispatcher.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
