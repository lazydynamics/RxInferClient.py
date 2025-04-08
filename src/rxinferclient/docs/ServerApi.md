# rxinferclient.ServerApi

All URIs are relative to *http://localhost:8000/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_server_info**](ServerApi.md#get_server_info) | **GET** /info | Get server information
[**ping_server**](ServerApi.md#ping_server) | **GET** /ping | Health check endpoint


# **get_server_info**
> ServerInfo get_server_info()

Get server information

Returns information about the server, such as the RxInferServer version, RxInfer version, Julia version, server edition and API version

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import rxinferclient
from rxinferclient.models.server_info import ServerInfo
from rxinferclient.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rxinferclient.Configuration(
    host = "http://localhost:8000/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKeyAuth
configuration = rxinferclient.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with rxinferclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rxinferclient.ServerApi(api_client)

    try:
        # Get server information
        api_response = await api_instance.get_server_info()
        print("The response of ServerApi->get_server_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerApi->get_server_info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ServerInfo**](ServerInfo.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved server information |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ping_server**
> PingResponse ping_server()

Health check endpoint

Simple endpoint to check if the server is alive and running

### Example


```python
import rxinferclient
from rxinferclient.models.ping_response import PingResponse
from rxinferclient.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rxinferclient.Configuration(
    host = "http://localhost:8000/v1"
)


# Enter a context with an instance of the API client
async with rxinferclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rxinferclient.ServerApi(api_client)

    try:
        # Health check endpoint
        api_response = await api_instance.ping_server()
        print("The response of ServerApi->ping_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerApi->ping_server: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PingResponse**](PingResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully pinged the server |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

