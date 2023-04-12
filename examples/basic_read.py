import asyncio

from src import DiscordClient


async def setup_table():
    # Login to discord API
    client = await DiscordClient.login(token="...")

    # Load an existing database
    db = await client.load_database("test_database")
    # Alternatively you can use `client.create_database`

    # When creating a database all tables are loaded
    # Load table called `table_1`
    table = db.table("table_1")
    # Alternatively you can use `db.create_table`
    return table


async def main():
    table = await setup_table()

    # Get item via unique `_id`
    # Example of what an _id looks like
    table.get_item("1681238527.9129455-bbb12f5d")

    # Alternatively get items via search criterias
    # You could even create your own id and use that
    table.find_items({"foo": "bar"})


if __name__ == "__main__":
    asyncio.run(main())
