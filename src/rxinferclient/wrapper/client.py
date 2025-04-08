
from typing import Optional

import warnings

from rxinferclient.api_client import ApiClient
from rxinferclient.api.authentication_api import AuthenticationApi
from rxinferclient.api.server_api import ServerApi
from rxinferclient.api.models_api import ModelsApi

class RxInferClient:
    """High-level client for the RxInfer API.
    
    This class provides a more user-friendly interface to the RxInfer API,
    wrapping the auto-generated client code.
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize the RxInfer client.
        
        Parameters:
            api_key: Optional API key for authentication. If not provided,
                    the client will attempt to generate a temporary API key.

        """
        self._api_client = ApiClient()
        
        if api_key is None:
            _tmp_auth = AuthenticationApi(self._api_client)    
            try:
                response = _tmp_auth.token_generate()
                api_key = response.token
            finally:
                if api_key is None or not isinstance(api_key, str):
                    warnings.warn("Failed to generate API key for the client. Provide an API key manually.", UserWarning)
        
        self._api_client.configuration.access_token = api_key
        
        self.server = ServerApi(self._api_client)
        self.authentication = AuthenticationApi(self._api_client)
        self.models = ModelsApi(self._api_client)
    