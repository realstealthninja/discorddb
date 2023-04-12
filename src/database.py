import json
import time
import uuid
from typing import Any, Self

from .types import Item
from .utils import Formatter

# fmt: off
__all__ = [
    'Table',
    'Database',
]
# fmt: on


class Table:
    """Represents a table
    (categorized by the discord channel categories)
    """

    def __init__(self, *, category_id: int, channel_ids: list[int]) -> None:
        self._items: dict[str, Item] = {}
        self._id: int = category_id  # Discord channel category id
        self._channels: list[int] = channel_ids  # List of discord channel ids

    async def _fetch_all_messages(self) -> list[str]:
        # TODO: Get all messages from every channel within the
        # table category
        return []

    async def create_item(self, data: dict, **kwargs: Any) -> None:
        if "_id" in data:
            raise TypeError("Data must not contain reserved `_id` keyword")

        data["_id"] = f"{time.time()}-{str(uuid.uuid4())[:8]}"
        item = Formatter.format(data)

        # TODO: Write data into channels
        # TODO: Dynamically split items across channels

        return data

    def get_item(self, id: int) -> Item | None:
        return self._items.get(id)

    def find_items(self, search: dict) -> list[Item]:
        search_items = search.items()

        def match(item):
            for key, value in search_items:
                if key not in item or item[key] != value:  # TODO: Use missing sentinel
                    return False
            return True

        return list(filter(match, self._items.values()))
    
    @property
    def name(self) -> str:
        return self.name
    
    def item_count(self) -> int:
        """Returns the total item count for this database."""
        return len(self._items)
    
    def total_size(self) -> float:
        """Returns the total size of the database and all its items.
        :return: Size in mb.
        """
        characters = 0
        for item in self._items.values():
            characters += len(str(item))
        # In unicode one character represents one byte
        kilobytes = characters / 1000
        megabytes = kilobytes / 1000
        return megabytes

    def average_item_size(self) -> float:
        """Returns the average item size for all items
        in this database.
        :return: Average item size in mb."""
        return self.total_size() / self.item_count()

class Database:
    """Represents a Database, which stores data using discords
    CDN from their servers and channels.
    """

    def __init__(self, tables: dict[str, Table]) -> None:
        self.tables = tables
        self._id: int = ...  # Discord server id

    @classmethod
    async def create(cls, name: str) -> Self:
        """Creates a database (discord server)."""
        # TODO: Create a discord server

    @classmethod
    async def load(cls, name: str) -> Self | None:
        """Load pre-existing database."""
        # TODO: Check if database exists
        if ... is None:
            return None

        # TODO: Get tables via text channel categories
        tables: list[Table] = ...

        for table in tables:
            raw_items = await table._fetch_all_messages()
            items: list[Item] = [Formatter.unformat(json.loads(raw_item)) for raw_item in raw_items]

            # Sort via `_id`
            all_items: dict[str, Item] = {}
            for item in items:
                # TODO: Group multiple items with the same _id
                # Done when items are so large they go over multiple messages
                all_items[item["_id"]] = item
            table._items = all_items

        self = cls(tables)
        return self

    async def create_table(self, name: str, *, channels: int = 5) -> Table:
        # TODO: Create category with X number of channels in it
        table = Table()
        self.tables[name] = table
        return table

    def table(self, name: str) -> Table | None:
        return self.tables.get(name)

    def item_count(self) -> int:
        """Returns the total item count for this database."""
        items = 0
        for table in self.tables.values():
            items += len(table._items)
        return items

    def total_size(self) -> float:
        """Returns the total size of the database and all its items.
        :return: Size in mb.
        """
        characters = 0
        for table in self.tables.values():
            for item in table._items.values():
                characters += len(str(item))
        # In unicode one character represents one byte
        kilobytes = characters / 1000
        megabytes = kilobytes / 1000
        return megabytes

    def average_item_size(self) -> float:
        """Returns the average item size for all items
        in this database.
        :return: Average item size in mb."""
        return self.total_size() / self.item_count()
