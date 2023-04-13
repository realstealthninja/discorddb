from typing import Self

from .database import Database

# fmt: off
__all__ = [
    'DiscordClient'
]
# fmt: on


class DiscordClient:
    """Represents the base discord client that utilises the discord
    api in order to create/load databases and make http requests."""

    def __init__(self) -> None:
        self.databases: dict[str, Database] = {}

    @classmethod
    async def login(cls, *, token: str) -> Self:
        self = cls()
        # TODO: Login as discord bot (?) and pass credentials
        return self

    async def load_database(self, name: str) -> Database | None:
        # TODO: Pass discord bot credentials
        self.databases[name] = (database := await Database.load(name))
        return database

    async def create_database(self, name: str) -> Database:
        # TODO: Pass discord bot credentials
        self.databases[name] = (database := await Database.create(name))
        return database
