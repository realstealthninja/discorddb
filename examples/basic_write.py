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

    # Create a document item
    await table.create_item({"foo": "bar", "type": 123})


if __name__ == "__main__":
    asyncio.run(main())
