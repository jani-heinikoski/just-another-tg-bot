# Service which provides access to the Elden Ring API

from typing import Any, Optional, Awaitable

from lib.common.typing import EldenAPIServiceProtocol, EldenItem


class EldenAPIService(EldenAPIServiceProtocol):

    async def fetch_item(self, item_id: str) -> Awaitable[Optional[EldenItem]]:
        raise NotImplementedError
