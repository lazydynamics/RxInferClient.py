# rxinferclient.ModelsApi

All URIs are relative to *http://localhost:8000/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_events_to_episode**](ModelsApi.md#attach_events_to_episode) | **POST** /models/i/{instance_id}/episodes/{episode_name}/attach-events | Attach events to an episode
[**attach_metadata_to_event**](ModelsApi.md#attach_metadata_to_event) | **POST** /models/i/{instance_id}/episodes/{episode_name}/events/{event_id}/attach-metadata | Attach metadata to an event
[**create_episode**](ModelsApi.md#create_episode) | **POST** /models/i/{instance_id}/create-episode | Create a new episode for a model instance
[**create_model_instance**](ModelsApi.md#create_model_instance) | **POST** /models/create-instance | Create a new model instance
[**delete_episode**](ModelsApi.md#delete_episode) | **DELETE** /models/i/{instance_id}/episodes/{episode_name} | Delete an episode for a model
[**delete_model_instance**](ModelsApi.md#delete_model_instance) | **DELETE** /models/i/{instance_id} | Delete a model instance
[**get_available_model**](ModelsApi.md#get_available_model) | **GET** /models/available/{model_name} | Get information about a specific model available for creation
[**get_available_models**](ModelsApi.md#get_available_models) | **GET** /models/available | Get models available for creation
[**get_episode_info**](ModelsApi.md#get_episode_info) | **GET** /models/i/{instance_id}/episodes/{episode_name} | Get episode information
[**get_episodes**](ModelsApi.md#get_episodes) | **GET** /models/i/{instance_id}/episodes | Get all episodes for a model instance
[**get_model_instance**](ModelsApi.md#get_model_instance) | **GET** /models/i/{instance_id} | Get model instance information
[**get_model_instance_parameters**](ModelsApi.md#get_model_instance_parameters) | **GET** /models/i/{instance_id}/parameters | Get the parameters of a model instance
[**get_model_instance_state**](ModelsApi.md#get_model_instance_state) | **GET** /models/i/{instance_id}/state | Get the state of a model instance
[**get_model_instances**](ModelsApi.md#get_model_instances) | **GET** /models/instances | Get all created model instances
[**run_inference**](ModelsApi.md#run_inference) | **POST** /models/i/{instance_id}/infer | Run inference
[**run_learning**](ModelsApi.md#run_learning) | **POST** /models/i/{instance_id}/learn | Learn from previous observations
[**wipe_episode**](ModelsApi.md#wipe_episode) | **POST** /models/i/{instance_id}/episodes/{episode_name}/wipe | Wipe all events from an episode


# **attach_events_to_episode**
> SuccessResponse attach_events_to_episode(instance_id, episode_name, attach_events_to_episode_request)

Attach events to an episode

Attach events to a specific episode for a model

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import rxinferclient
from rxinferclient.models.attach_events_to_episode_request import AttachEventsToEpisodeRequest
from rxinferclient.models.success_response import SuccessResponse
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
with rxinferclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rxinferclient.ModelsApi(api_client)
    instance_id = 'instance_id_example' # str | ID of the model instance to attach events to
    episode_name = 'episode_name_example' # str | Name of the episode to attach events to
    attach_events_to_episode_request = rxinferclient.AttachEventsToEpisodeRequest() # AttachEventsToEpisodeRequest | 

    try:
        # Attach events to an episode
        api_response = api_instance.attach_events_to_episode(instance_id, episode_name, attach_events_to_episode_request)
        print("The response of ModelsApi->attach_events_to_episode:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->attach_events_to_episode: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| ID of the model instance to attach events to | 
 **episode_name** | **str**| Name of the episode to attach events to | 
 **attach_events_to_episode_request** | [**AttachEventsToEpisodeRequest**](AttachEventsToEpisodeRequest.md)|  | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully attached events to the episode |  -  |
**400** | Bad request, e.g. invalid data |  -  |
**401** | Access token is missing, invalid or has no access to the specific model |  -  |
**404** | Model or episode not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_metadata_to_event**
> SuccessResponse attach_metadata_to_event(instance_id, episode_name, event_id, attach_metadata_to_event_request)

Attach metadata to an event

Attach metadata to a specific event for a model

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import rxinferclient
from rxinferclient.models.attach_metadata_to_event_request import AttachMetadataToEventRequest
from rxinferclient.models.success_response import SuccessResponse
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
with rxinferclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rxinferclient.ModelsApi(api_client)
    instance_id = 'instance_id_example' # str | ID of the model instance to attach metadata to
    episode_name = 'episode_name_example' # str | Name of the episode to attach metadata to
    event_id = 56 # int | ID of the event to attach metadata to
    attach_metadata_to_event_request = rxinferclient.AttachMetadataToEventRequest() # AttachMetadataToEventRequest | 

    try:
        # Attach metadata to an event
        api_response = api_instance.attach_metadata_to_event(instance_id, episode_name, event_id, attach_metadata_to_event_request)
        print("The response of ModelsApi->attach_metadata_to_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->attach_metadata_to_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| ID of the model instance to attach metadata to | 
 **episode_name** | **str**| Name of the episode to attach metadata to | 
 **event_id** | **int**| ID of the event to attach metadata to | 
 **attach_metadata_to_event_request** | [**AttachMetadataToEventRequest**](AttachMetadataToEventRequest.md)|  | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully attached metadata to the event |  -  |
**401** | Access token is missing, invalid or has no access to the specific model |  -  |
**404** | Model or episode not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_episode**
> EpisodeInfo create_episode(instance_id, create_episode_request)

Create a new episode for a model instance

Create a new episode for a specific model instance.
Note that the default episode is created automatically when the model instance is created. 
When a new episode is created, it becomes the current episode for the model instance.


### Example

* Bearer Authentication (ApiKeyAuth):

```python
import rxinferclient
from rxinferclient.models.create_episode_request import CreateEpisodeRequest
from rxinferclient.models.episode_info import EpisodeInfo
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
with rxinferclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rxinferclient.ModelsApi(api_client)
    instance_id = 'instance_id_example' # str | ID of the model instance to create episode for
    create_episode_request = rxinferclient.CreateEpisodeRequest() # CreateEpisodeRequest | 

    try:
        # Create a new episode for a model instance
        api_response = api_instance.create_episode(instance_id, create_episode_request)
        print("The response of ModelsApi->create_episode:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->create_episode: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| ID of the model instance to create episode for | 
 **create_episode_request** | [**CreateEpisodeRequest**](CreateEpisodeRequest.md)|  | 

### Return type

[**EpisodeInfo**](EpisodeInfo.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created episode |  -  |
**400** | Episode cannot be created, e.g. it already exists |  -  |
**401** | Access token is missing, invalid or has no access to the specific model |  -  |
**404** | Model instance not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_model_instance**
> CreateModelInstanceResponse create_model_instance(create_model_instance_request)

Create a new model instance

Creates a new instance of a model with the specified configuration

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import rxinferclient
from rxinferclient.models.create_model_instance_request import CreateModelInstanceRequest
from rxinferclient.models.create_model_instance_response import CreateModelInstanceResponse
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
with rxinferclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rxinferclient.ModelsApi(api_client)
    create_model_instance_request = rxinferclient.CreateModelInstanceRequest() # CreateModelInstanceRequest | 

    try:
        # Create a new model instance
        api_response = api_instance.create_model_instance(create_model_instance_request)
        print("The response of ModelsApi->create_model_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->create_model_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_model_instance_request** | [**CreateModelInstanceRequest**](CreateModelInstanceRequest.md)|  | 

### Return type

[**CreateModelInstanceResponse**](CreateModelInstanceResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Model instance created successfully |  -  |
**401** | Access token is missing or invalid |  -  |
**400** | Bad request |  -  |
**404** | Model not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_episode**
> SuccessResponse delete_episode(instance_id, episode_name)

Delete an episode for a model

Delete a specific episode for a model instance.
Note that the default episode cannot be deleted, but you can wipe data from it.
If the deleted episode was the current episode, the default episode will become the current episode.


### Example

* Bearer Authentication (ApiKeyAuth):

```python
import rxinferclient
from rxinferclient.models.success_response import SuccessResponse
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
with rxinferclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rxinferclient.ModelsApi(api_client)
    instance_id = 'instance_id_example' # str | ID of the model instance to delete episode for
    episode_name = 'episode_name_example' # str | Name of the episode to delete

    try:
        # Delete an episode for a model
        api_response = api_instance.delete_episode(instance_id, episode_name)
        print("The response of ModelsApi->delete_episode:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->delete_episode: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| ID of the model instance to delete episode for | 
 **episode_name** | **str**| Name of the episode to delete | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully deleted episode |  -  |
**400** | Episode cannot be deleted, e.g. it is the default episode |  -  |
**401** | Access token is missing, invalid or has no access to the specific model |  -  |
**404** | Model or episode not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_model_instance**
> SuccessResponse delete_model_instance(instance_id)

Delete a model instance

Delete a specific model instance by its ID

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import rxinferclient
from rxinferclient.models.success_response import SuccessResponse
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
with rxinferclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rxinferclient.ModelsApi(api_client)
    instance_id = 'instance_id_example' # str | ID of the model instance to delete

    try:
        # Delete a model instance
        api_response = api_instance.delete_model_instance(instance_id)
        print("The response of ModelsApi->delete_model_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->delete_model_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| ID of the model instance to delete | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Model successfully deleted |  -  |
**401** | Access token is missing, invalid or has no access to the specific model |  -  |
**404** | Model not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_model**
> AvailableModel get_available_model(model_name)

Get information about a specific model available for creation

Retrieve detailed information about a specific model available for creation

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import rxinferclient
from rxinferclient.models.available_model import AvailableModel
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
with rxinferclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rxinferclient.ModelsApi(api_client)
    model_name = 'model_name_example' # str | Name of the model to retrieve information for (including version identifier if applicable, e.g. \"BetaBernoulli-v1\")

    try:
        # Get information about a specific model available for creation
        api_response = api_instance.get_available_model(model_name)
        print("The response of ModelsApi->get_available_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->get_available_model: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_name** | **str**| Name of the model to retrieve information for (including version identifier if applicable, e.g. \&quot;BetaBernoulli-v1\&quot;) | 

### Return type

[**AvailableModel**](AvailableModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved model details |  -  |
**401** | Access token is missing or invalid |  -  |
**404** | Model cannot be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_models**
> List[AvailableModel] get_available_models()

Get models available for creation

Retrieve the list of models available for creation for a given token.
This list specifies names and available arguments for each model.

**Note** The list of available models might differ for different access tokens.
For example, a token with only the "user" role might not have access to all models.


### Example

* Bearer Authentication (ApiKeyAuth):

```python
import rxinferclient
from rxinferclient.models.available_model import AvailableModel
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
with rxinferclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rxinferclient.ModelsApi(api_client)

    try:
        # Get models available for creation
        api_response = api_instance.get_available_models()
        print("The response of ModelsApi->get_available_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->get_available_models: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AvailableModel]**](AvailableModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved list of models available for creation |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_episode_info**
> EpisodeInfo get_episode_info(instance_id, episode_name)

Get episode information

Retrieve information about a specific episode of a model

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import rxinferclient
from rxinferclient.models.episode_info import EpisodeInfo
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
with rxinferclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rxinferclient.ModelsApi(api_client)
    instance_id = 'instance_id_example' # str | ID of the model instance to retrieve episode for
    episode_name = 'episode_name_example' # str | Name of the episode to retrieve

    try:
        # Get episode information
        api_response = api_instance.get_episode_info(instance_id, episode_name)
        print("The response of ModelsApi->get_episode_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->get_episode_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| ID of the model instance to retrieve episode for | 
 **episode_name** | **str**| Name of the episode to retrieve | 

### Return type

[**EpisodeInfo**](EpisodeInfo.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved episode information |  -  |
**401** | Access token is missing, invalid or has no access to the specific model |  -  |
**404** | Model or episode not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_episodes**
> List[EpisodeInfo] get_episodes(instance_id)

Get all episodes for a model instance

Retrieve all episodes for a specific model instance

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import rxinferclient
from rxinferclient.models.episode_info import EpisodeInfo
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
with rxinferclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rxinferclient.ModelsApi(api_client)
    instance_id = 'instance_id_example' # str | ID of the model instance to retrieve episodes for

    try:
        # Get all episodes for a model instance
        api_response = api_instance.get_episodes(instance_id)
        print("The response of ModelsApi->get_episodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->get_episodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| ID of the model instance to retrieve episodes for | 

### Return type

[**List[EpisodeInfo]**](EpisodeInfo.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved list of episodes |  -  |
**401** | Access token is missing, invalid or has no access to the specific model |  -  |
**404** | Model not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_instance**
> ModelInstance get_model_instance(instance_id)

Get model instance information

Retrieve detailed information about a specific model instance

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import rxinferclient
from rxinferclient.models.model_instance import ModelInstance
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
with rxinferclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rxinferclient.ModelsApi(api_client)
    instance_id = 'instance_id_example' # str | ID of the model instance to retrieve information for

    try:
        # Get model instance information
        api_response = api_instance.get_model_instance(instance_id)
        print("The response of ModelsApi->get_model_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->get_model_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| ID of the model instance to retrieve information for | 

### Return type

[**ModelInstance**](ModelInstance.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved model information |  -  |
**401** | Access token is missing, invalid or has no access to the specific model |  -  |
**404** | Model not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_instance_parameters**
> ModelInstanceParameters get_model_instance_parameters(instance_id)

Get the parameters of a model instance

Retrieve the parameters of a specific model instance

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import rxinferclient
from rxinferclient.models.model_instance_parameters import ModelInstanceParameters
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
with rxinferclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rxinferclient.ModelsApi(api_client)
    instance_id = 'instance_id_example' # str | 

    try:
        # Get the parameters of a model instance
        api_response = api_instance.get_model_instance_parameters(instance_id)
        print("The response of ModelsApi->get_model_instance_parameters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->get_model_instance_parameters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**|  | 

### Return type

[**ModelInstanceParameters**](ModelInstanceParameters.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved model parameters |  -  |
**400** | Model parameters cannot be retrieved due to internal error |  -  |
**401** | Access token is missing, invalid or has no access to the specific model |  -  |
**404** | Model not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_instance_state**
> ModelInstanceState get_model_instance_state(instance_id)

Get the state of a model instance

Retrieve the state of a specific model instance

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import rxinferclient
from rxinferclient.models.model_instance_state import ModelInstanceState
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
with rxinferclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rxinferclient.ModelsApi(api_client)
    instance_id = 'instance_id_example' # str | ID of the model instance to retrieve state for

    try:
        # Get the state of a model instance
        api_response = api_instance.get_model_instance_state(instance_id)
        print("The response of ModelsApi->get_model_instance_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->get_model_instance_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| ID of the model instance to retrieve state for | 

### Return type

[**ModelInstanceState**](ModelInstanceState.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved model state. Each model has its own state, which is a dictionary of arbitrary key-value pairs. Check model-specific documentation for more details. |  -  |
**400** | Model state cannot be retrieved due to internal error |  -  |
**401** | Access token is missing, invalid or has no access to the specific model |  -  |
**404** | Model not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_instances**
> List[ModelInstance] get_model_instances()

Get all created model instances

Retrieve detailed information about all created model instances for a specific token

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import rxinferclient
from rxinferclient.models.model_instance import ModelInstance
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
with rxinferclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rxinferclient.ModelsApi(api_client)

    try:
        # Get all created model instances
        api_response = api_instance.get_model_instances()
        print("The response of ModelsApi->get_model_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->get_model_instances: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ModelInstance]**](ModelInstance.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved list of created model instances |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_inference**
> InferResponse run_inference(instance_id, infer_request)

Run inference

Run inference on a specific model instance

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import rxinferclient
from rxinferclient.models.infer_request import InferRequest
from rxinferclient.models.infer_response import InferResponse
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
with rxinferclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rxinferclient.ModelsApi(api_client)
    instance_id = 'instance_id_example' # str | ID of the model instance to run inference on
    infer_request = rxinferclient.InferRequest() # InferRequest | 

    try:
        # Run inference
        api_response = api_instance.run_inference(instance_id, infer_request)
        print("The response of ModelsApi->run_inference:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->run_inference: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| ID of the model instance to run inference on | 
 **infer_request** | [**InferRequest**](InferRequest.md)|  | 

### Return type

[**InferResponse**](InferResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully ran inference on the model |  -  |
**401** | Access token is missing, invalid or has no access to the specific model |  -  |
**404** | Model not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_learning**
> LearnResponse run_learning(instance_id, learn_request)

Learn from previous observations

Learn from previous episodes for a specific model

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import rxinferclient
from rxinferclient.models.learn_request import LearnRequest
from rxinferclient.models.learn_response import LearnResponse
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
with rxinferclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rxinferclient.ModelsApi(api_client)
    instance_id = 'instance_id_example' # str | 
    learn_request = rxinferclient.LearnRequest() # LearnRequest | 

    try:
        # Learn from previous observations
        api_response = api_instance.run_learning(instance_id, learn_request)
        print("The response of ModelsApi->run_learning:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->run_learning: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**|  | 
 **learn_request** | [**LearnRequest**](LearnRequest.md)|  | 

### Return type

[**LearnResponse**](LearnResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully ran learning on the model |  -  |
**401** | Access token is missing, invalid or has no access to the specific model |  -  |
**404** | Model not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wipe_episode**
> SuccessResponse wipe_episode(instance_id, episode_name)

Wipe all events from an episode

Wipe all events from a specific episode for a model

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import rxinferclient
from rxinferclient.models.success_response import SuccessResponse
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
with rxinferclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rxinferclient.ModelsApi(api_client)
    instance_id = 'instance_id_example' # str | ID of the model instance to wipe episode for
    episode_name = 'episode_name_example' # str | Name of the episode to wipe

    try:
        # Wipe all events from an episode
        api_response = api_instance.wipe_episode(instance_id, episode_name)
        print("The response of ModelsApi->wipe_episode:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->wipe_episode: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| ID of the model instance to wipe episode for | 
 **episode_name** | **str**| Name of the episode to wipe | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully wiped episode |  -  |
**401** | Access token is missing, invalid or has no access to the specific model |  -  |
**404** | Model or episode not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

