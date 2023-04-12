import unittest

from src import DiscordClient

test_item = {"foo": "bar", "types": {"satus": 1, "code": 2.3}}


class TestReadWrite(unittest.IsolatedAsyncioTestCase):
    async def setUp(self) -> None:
        client = await DiscordClient.login(token="...")
        self.db = await client.load_database("test_database")
        self.test_table = self.db.table("test_table")

    async def test_create_item(self) -> None:
        item = await self.test_table.create_item(test_item)
        self.item_id = item["_id"]

    async def test_get_item(self) -> None:
        item = self.test_table.get_item(self.item_id)
        del item["_id"]
        self.assertEqual(item, test_item)

    async def test_find_items(self) -> None:
        items = self.test_table.find_items({"types": {"status": 1}})
        self.assertEqual(len(items), 1)
        del items[0]["_id"]
        self.assertEqual(items[0], test_item)

    async def test_create_table(self) -> None:
        table = await self.db.create_table("test_table_2")
        self.assertIsNotNone(table)
