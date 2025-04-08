# rxinfer_openapi.AuthenticationApi

All URIs are relative to *http://localhost:8000/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**token_generate**](AuthenticationApi.md#token_generate) | **POST** /token/generate | Generate authentication token
[**token_roles**](AuthenticationApi.md#token_roles) | **GET** /token/roles | Get token roles


# **token_generate**
> TokenGenerateResponse token_generate()

Generate authentication token

Generates a new authentication token for accessing protected endpoints

### Example


```python
import rxinfer_openapi
from rxinfer_openapi.models.token_generate_response import TokenGenerateResponse
from rxinfer_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rxinfer_openapi.Configuration(
    host = "http://localhost:8000/v1"
)


# Enter a context with an instance of the API client
with rxinfer_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rxinfer_openapi.AuthenticationApi(api_client)

    try:
        # Generate authentication token
        api_response = api_instance.token_generate()
        print("The response of AuthenticationApi->token_generate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->token_generate: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TokenGenerateResponse**](TokenGenerateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully generated authentication token |  -  |
**400** | Unable to generate token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **token_roles**
> TokenRolesResponse token_roles()

Get token roles

Retrieve the list of roles for a specific token

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import rxinfer_openapi
from rxinfer_openapi.models.token_roles_response import TokenRolesResponse
from rxinfer_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rxinfer_openapi.Configuration(
    host = "http://localhost:8000/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKeyAuth
configuration = rxinfer_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with rxinfer_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rxinfer_openapi.AuthenticationApi(api_client)

    try:
        # Get token roles
        api_response = api_instance.token_roles()
        print("The response of AuthenticationApi->token_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->token_roles: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TokenRolesResponse**](TokenRolesResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved token roles |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

