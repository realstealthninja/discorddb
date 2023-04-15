from .client import DiscordClient


class Pool:
    def __init__(self, tokens: list[str]) -> None:
        self.tokens: list[str] = tokens
        self.cursors: list[DiscordClient] = [
            DiscordClient.login(token) for token in tokens
        ]

    async def sort(cls):
        # TODO: implement more sorting methods
        self = cls()
        self.cursors.sort(key=lambda x: x.latency)
