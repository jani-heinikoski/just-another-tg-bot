import unittest

from lib.services.elden_api_service import EldenAPIService
from lib.common.typing import EldenItem, EldenAPIServiceProtocol


class TestEldenAPIService(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        self.elden_service: EldenAPIServiceProtocol = EldenAPIService()
        self.valid_item = EldenItem(
            "17f69de1218l0i2olc1m799deyzbgj",
            "Boc The Seamster",
            "https://eldenring.fanapis.com/images/npcs/17f69de1218l0i2olc1m799deyzbgj.png",
            "Hm? Oh, yes I remember. Some clod turned me into a tree.",
            "Limgrave",
            "Garments Adjuster"
        )

    async def test_fetch_item_not_none(self):
        self.assertIsNotNone(await self.elden_service.fetch_item(self.valid_item.id),
                             f'Did not find item with id: {self.valid_item.id}')

    async def test_fetch_item_is_instance_of_elden_item(self):
        item: EldenItem = await self.elden_service.fetch_item(self.valid_item.id)
        self.assertIsInstance(
            item, EldenItem, f'Returned item is not instance of {EldenItem.__name__}')

    async def test_fetch_item_returns_none(self):
        self.assertIsNone(await self.elden_service.fetch_item("this is a non-valid item identifier"),
                          "Invalid item_id argument did not result in None")


if __name__ == '__main__':
    unittest.main()
