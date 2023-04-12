import unittest

from src import DiscordClient


test_item = {"foo": "bar", "types": {"satus": 1, "code": 2.3}}


class TestReadWrite(unittest.IsolatedAsyncioTestCase):
    async def setUp(self) -> None:
        self.client = await DiscordClient.login(token="...")

    async def test_create_database(self) -> None:
        db = await self.client.create_database("test_database")
        self.assertIsNotNone(db)

    async def test_load_database(self) -> None:
        db = await self.client.load_database("test_database")
        self.assertIsNotNone(db)

    async def test_load_non_existant_database(self) -> None:
        db = await self.client.load_database("...")
        self.assertIsNone(db)
