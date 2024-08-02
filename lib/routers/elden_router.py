# Router which handles commands related to querying Elden Ring API
from aiogram import Router, html
from aiogram.types import Message, BotCommand
from aiogram.filters import Command, CommandObject

from typing import Optional

from lib.common.typing import EldenAPIServiceProtocol, EldenItem

_router: Router = Router(name="onboarding_router")

# Commands
_items_command = BotCommand(
    command="items", description="Lists all Elden Ring items"
)
_item_command = BotCommand(
    command="item_id", description="Fetches an Elden Ring item which matches the given id (example usage: /item_id 17f69e47912l0i1z0lip3kamll88h)"
)


@_router.message(Command(_items_command))
async def items_handler(message: Message, elden_api_service: EldenAPIServiceProtocol) -> None:
    """
    Handles /items command
    """
    await message.answer("This command has not yet been implemented...")


@_router.message(Command(_item_command))
async def item_handler(message: Message, command: CommandObject, elden_api_service: EldenAPIServiceProtocol) -> None:
    """
    Handles item_id command
    """
    try:
        item_id: str = command.args
        item: Optional[EldenItem] = await elden_api_service.fetch_item(item_id)
        if item:
            await message.answer_photo(photo=item.image, caption=str(item))
        else:
            await message.answer(f'Could not find an item with id: {item_id}')
    except Exception as e:
        print(e)
        await message.answer("Something unexpected went wrong...")


def get_router() -> Router:
    """
    Returns the Router object which can be included to the dispatcher
    """
    return _router
