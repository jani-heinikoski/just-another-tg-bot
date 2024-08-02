# Mock service of the Elden Ring API for testing purposes

from typing import Optional, Awaitable

from lib.common.typing import EldenAPIServiceProtocol, EldenItem


class MockEldenAPIService(EldenAPIServiceProtocol):

    async def fetch_item(self, item_id: str) -> Awaitable[Optional[EldenItem]]:
        if (item_id):
            return EldenItem(
                "17f69de1218l0i2olc1m799deyzbgj",
                "Boc The Seamster",
                "https://eldenring.fanapis.com/images/npcs/17f69de1218l0i2olc1m799deyzbgj.png",
                "Hm? Oh, yes I remember. Some clod turned me into a tree.",
                "Limgrave",
                "Garments Adjuster"
            )
        return None
