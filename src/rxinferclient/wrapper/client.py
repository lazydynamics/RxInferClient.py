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

    The client functionality is organized into several subfields:
        - server: Access to server-related operations via ServerApi
        - authentication: Authentication and token management via AuthenticationApi
        - models: Model management and operations via ModelsApi

    Examples:
        Initialize the client (will auto-generate API key if not provided):
        >>> client = RxInferClient()

        Initialize with custom server URL:
        >>> client = RxInferClient(server_url="http://localhost:8000/v1")

        Check server status:
        >>> response = client.server.ping_server()
        >>> assert response.status == 'ok'

        Create and manage model instances:
        >>> # Create a new model instance
        >>> response = client.models.create_model_instance({
        ...     "model_name": "BetaBernoulli-v1",
        ... })
        >>> instance_id = response.instance_id
        >>> 
        >>> # Delete the model instance when done
        >>> client.models.delete_model_instance(instance_id=instance_id)
    """
    
    def __init__(self, api_key: Optional[str] = None, server_url: Optional[str] = None):
        """Initialize the RxInfer client.
        
        Parameters:
            api_key: Optional API key for authentication. If not provided,
                    the client will attempt to generate a temporary API key.
            server_url: Optional server URL. If provided, overrides the default
                       server URL configuration.
        """
        self._api_client = ApiClient()
        
        if server_url is not None:
            self._api_client.configuration.host = server_url
        
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
    