from .client import DiscordClient


class Pool:
    def __init__(self, tokens: list[str]) -> None:
        self.tokens = tokens
        self.cursors: list[DiscordClient] = [
            DiscordClient.login(token) for token in tokens
        ]

    async def sort(self):
        # TODO: implement more sorting methods
        self.cursors.sort(key=lambda x: x.latency)
