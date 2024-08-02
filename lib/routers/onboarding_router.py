# Router which handles user onboarding
from aiogram import Router, html
from aiogram.types import Message, BotCommand
from aiogram.filters import CommandStart, Command

from typing import List

from .elden_router import get_commands as get_elden_router_commands

_router: Router = Router(name="onboarding_router")

# Commands
_help_command = BotCommand(
    command="help", description="Lists all commands the bot understands.")


def get_commands() -> List[BotCommand]:
    """
    Returns a list of all commands this router is capable of handling. Used by onboarding (this) router to provide help.
    """
    return [_help_command]


@_router.message(CommandStart())
async def start_handler(message: Message) -> None:
    """
    Handles /start command
    """
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}! See /{_help_command.command} for a listing of commands you can use!")


def add_commands_to_answer(to: List[str], heading: str, commands: List[BotCommand]) -> None:
    """
    Helper function for constructing the answer message to /help command 
    """
    to.append(f"\n{html.bold(heading)}")
    for c in commands:
        to.append(f"\n/{c.command} - {c.description}")
    to.append('\n')


@_router.message(Command(_help_command, ignore_case=True))
async def help_handler(message: Message) -> None:
    """
    Handles /help command
    """
    answer = [html.underline(
        html.bold("These are the commands this bot understands:\n"))]
    # Onboarding (this) router
    add_commands_to_answer(
        answer, "Onboarding:", get_commands())
    # Elden router
    add_commands_to_answer(
        answer, "Elden Ring related commands:", get_elden_router_commands())
    await message.answer("".join(answer))


def get_router() -> Router:
    """
    Returns the Router object which can be included to the dispatcher
    """
    return _router
