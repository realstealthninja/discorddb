from typing import  TYPE_CHECKING

if TYPE_CHECKING:
    from .client import DiscordClient

class pool:
    
    def __init__(self, tokens: list[str]) -> None:
        self.tokens: list[str] = tokens
        self.cursors: list["DiscordClient"] = [DiscordClient.login(token) for token in tokens]
    
    @classmethod
    async def sort(cls):
        #TODO: implement more sorting methods
        self = cls()
        self.cursors.sort(lambda x: x.latency)
    
    
