class Codec:
    def __init__(self):
        self.encodeMap = {}
        self.decodeMap = {}
        self.base = "https://wecom-url.com/"

    def encode(self, longUrl: str) -> str:
        if longUrl not in self.encodeMap:
            shortUrl = self.base + str(len(encodeMap) + 1)
            self.encodeMap[longUrl] = shortUrl
            self.decodeMap[shortUrl] = longUrl
        return self.encodeMap[longUrl]

    def decode(self, shortUrl:str) -> str:
        return self.decodeMap[shortUrl]