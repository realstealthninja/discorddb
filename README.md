# DiscordDB
### A document database utilising the discord API in order to store data that can be read, written to, and edited at any time.


## Why DiscordDB
DiscordDB is a cheap alternative to some larger, paid database such as `mongodb` or amazon web services `dynamodb`.

Ultimately, `DiscordDB` is a fun project that probably doesn't scale well, but I've been thinking about this idea for a while so testing discord as a database could be interesting.


## How does DiscordDB work
In `DiscordDB`, a server represents a `database`, with channels storing `items`. In order to mitigate discords ratelimit of 5 messages per second per channel, items are spread out over multiple channels.
Channels are put under categories, which indicate the name of the `table`.
Some items with larger data will be stored over multiple messages due to discords 2000 character limit.

In the future, some larger items could be stored as files due to discord allowing you to store files up to 8mb of size. These shouldn't be used every message due to suspicious activity though.

When loading a `database`, all items are initially fetched and cached from the channels, and sorted via their `_id`'s in order to provide a `O(1)` complexity when getting items with their `_id`. Similiarly, items can also be retrieved with keys and values that these items may have. This is done with a normal `O(n)` filtering algorithm, and does not require any API requests due to all items being initially cached.

By fetching and caching items when loading, `DiscordDB` can provide instant lookup and quick finding times.

I am currently deciding whether or not to use a discord bot along with a standard library such as `discord.py`, or just making raw requests to the discord API. Advantages of using `discord.py` would be the automatic ratelimit handling and ease of access, however it could potentially be slowed due to its websocket connection with discord and sending useless heartbeats. 
We would only be using the discord bot to purely send HTTP requests and receive nothing, and therefore websocket is required.
Advantages of creating our own dedicated HTTP client include better manipulation of the HTTP ourselves, instead of using a wrapper limiting direct access to the API.
Unfortunately, creating our own HTTP client would take longer and potentially be less reliable.


## Reserved keywords in items
`_id` - A unique identifier that each item is automtically assigned. It is split via `-`, with the first half being the `unix` timestamp in order to provided automatic sorting, and the second half being the first 8 characters of a unique uuid4 code.
Looks like `1681238527.9129455-bbb12f5d`


## Limitations
Currently `DiscordDB` supports data types including `boolean`, `real`, `integer`, `string` however does not support `blob` or other more unusual datatypes.

As mentiond earlier, `DiscordDB` initially fetches all data from a database when it is loaded. A downside of this method is a potentially long startup period in which many batch history requests are made. This leads to poor scalibility and the possibility of getting temporarily banned from the discord API.


## Installation
### Via pythons package manager, pip:
> ```sh
> pip install git+https://github.com/caedenph/discorddb
> ```

### Other methods are not currently supported


## Contribution
I am open to pull requests, issues and discussions about `DiscordDB`. Please contact me if you have any questions, but don't hesitate to open an issue.

I myself developed most of the codebase on a plane without internet connection, hence the lack of code interacting with the discord API.