import niquests


class BaseClient:
    def __init__(self, api_key: str):
        self.api_key = api_key


class SyncClient(BaseClient):

    def get(self, url: str, **kwargs):
        return niquests.get(url, kwargs)

    def post(self, url: str, **kwargs):
        return niquests.post(url, **kwargs)

    def put(self, url: str, **kwargs):
        return niquests.put(url, **kwargs)

    def delete(self, url: str, **kwargs):
        return niquests.delete(url, **kwargs)
