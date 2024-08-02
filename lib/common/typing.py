from typing import Protocol, Optional, Awaitable
from abc import abstractmethod


class EldenItem:
    def __init__(self, id: str, name: str, image: str, quote: str, location: str, role: str) -> None:
        self.id = id
        self.name = name
        self.image = image
        self.quote = quote
        self.location = location
        self.role = role

    def __str__(self) -> str:
        return f'id: {self.id}\nname: {self.name}\n'


class EldenAPIServiceProtocol(Protocol):

    @abstractmethod
    async def fetch_item(self, item_id: str) -> Awaitable[Optional[EldenItem]]:
        raise NotImplementedError
