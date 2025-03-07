import time

from ._client import RxInfer


class APIResource:
    _client: RxInfer

    def __init__(self, client: RxInfer) -> None:
        self._client = client
        self._get = client.get
        self._post = client.post
        self._put = client.put
        self._delete = client.delete

    def _sleep(self, seconds: float) -> None:
        time.sleep(seconds)
