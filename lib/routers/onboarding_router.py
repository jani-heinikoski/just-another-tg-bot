# Router which handles user onboarding
from aiogram import Router, html
from aiogram.types import Message, BotCommand
from aiogram.filters import CommandStart, Command

_router: Router = Router(name="onboarding_router")

# Commands
_help_command = BotCommand(command="help", description="Desc")


@_router.message(CommandStart())
async def start_handler(message: Message) -> None:
    """
    Handles /start command
    """
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


@_router.message(Command(_help_command, ignore_case=True))
async def help_handler(message: Message) -> None:
    """
    Handles /help command
    """
    await message.answer(f"These are the commands this bot understands:")


def get_router() -> Router:
    """
    Returns the Router object which can be included to the dispatcher
    """
    return _router
