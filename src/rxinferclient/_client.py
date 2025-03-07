from ._base_client import SyncClient
from .resources import Learn, Plan


class RxInfer(SyncClient):
    learn: Learn
    plan: Plan

    # client options
    api_key: str

    def __init__(self, api_key: str):
        self.api_key = api_key

        self.learn = Learn(self)
        self.plan = Plan(self)
