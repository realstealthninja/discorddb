from typing import TypedDict

# fmt: off
__all__ = [
    'Item',
]
# fmt: on


class Item(TypedDict):
    """Represents an item found in a table."""

    _id: str
