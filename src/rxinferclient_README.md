# rxinferclient
API for RxInferServer.jl - A Julia server for RxInfer probabilistic programming framework **Warning** The specification is not yet stable and may undergo significant changes. 

The `rxinferclient` package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.0.1
- Package version: 1.0.0
- Generator version: 7.13.0-SNAPSHOT
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://github.com/lazydynamics/RxInferServer](https://github.com/lazydynamics/RxInferServer)

## Requirements.

Python 3.8+

## Installation & Usage

This python library package is generated without supporting files like setup.py or requirements files

To be able to use it, you will need these dependencies in your own package that uses this library:

* urllib3 >= 1.25.3, < 3.0.0
* python-dateutil >= 2.8.2
* pydantic >= 2
* typing-extensions >= 4.7.1

## Getting Started

In your own code, to use this library to connect and interact with rxinferclient,
you can run the following:

```python

import rxinferclient
from rxinferclient.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = rxinferclient.Configuration(
    host = "http://localhost:8000/v1"
)



# Enter a context with an instance of the API client
with rxinferclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rxinferclient.AuthenticationApi(api_client)

    try:
        # Generate authentication token
        api_response = api_instance.token_generate()
        print("The response of AuthenticationApi->token_generate:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->token_generate: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:8000/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthenticationApi* | [**token_generate**](docs/AuthenticationApi.md#token_generate) | **POST** /token/generate | Generate authentication token
*AuthenticationApi* | [**token_roles**](docs/AuthenticationApi.md#token_roles) | **GET** /token/roles | Get token roles
*ModelsApi* | [**attach_events_to_episode**](docs/ModelsApi.md#attach_events_to_episode) | **POST** /models/i/{instance_id}/episodes/{episode_name}/attach-events | Attach events to an episode
*ModelsApi* | [**attach_metadata_to_event**](docs/ModelsApi.md#attach_metadata_to_event) | **POST** /models/i/{instance_id}/episodes/{episode_name}/events/{event_id}/attach-metadata | Attach metadata to an event
*ModelsApi* | [**create_episode**](docs/ModelsApi.md#create_episode) | **POST** /models/i/{instance_id}/create-episode | Create a new episode for a model instance
*ModelsApi* | [**create_model_instance**](docs/ModelsApi.md#create_model_instance) | **POST** /models/create-instance | Create a new model instance
*ModelsApi* | [**delete_episode**](docs/ModelsApi.md#delete_episode) | **DELETE** /models/i/{instance_id}/episodes/{episode_name} | Delete an episode for a model
*ModelsApi* | [**delete_model_instance**](docs/ModelsApi.md#delete_model_instance) | **DELETE** /models/i/{instance_id} | Delete a model instance
*ModelsApi* | [**get_available_model**](docs/ModelsApi.md#get_available_model) | **GET** /models/available/{model_name} | Get information about a specific model available for creation
*ModelsApi* | [**get_available_models**](docs/ModelsApi.md#get_available_models) | **GET** /models/available | Get models available for creation
*ModelsApi* | [**get_episode_info**](docs/ModelsApi.md#get_episode_info) | **GET** /models/i/{instance_id}/episodes/{episode_name} | Get episode information
*ModelsApi* | [**get_episodes**](docs/ModelsApi.md#get_episodes) | **GET** /models/i/{instance_id}/episodes | Get all episodes for a model instance
*ModelsApi* | [**get_model_instance**](docs/ModelsApi.md#get_model_instance) | **GET** /models/i/{instance_id} | Get model instance information
*ModelsApi* | [**get_model_instance_parameters**](docs/ModelsApi.md#get_model_instance_parameters) | **GET** /models/i/{instance_id}/parameters | Get the parameters of a model instance
*ModelsApi* | [**get_model_instance_state**](docs/ModelsApi.md#get_model_instance_state) | **GET** /models/i/{instance_id}/state | Get the state of a model instance
*ModelsApi* | [**get_model_instances**](docs/ModelsApi.md#get_model_instances) | **GET** /models/instances | Get all created model instances
*ModelsApi* | [**run_inference**](docs/ModelsApi.md#run_inference) | **POST** /models/i/{instance_id}/infer | Run inference
*ModelsApi* | [**run_learning**](docs/ModelsApi.md#run_learning) | **POST** /models/i/{instance_id}/learn | Learn from previous observations
*ModelsApi* | [**wipe_episode**](docs/ModelsApi.md#wipe_episode) | **POST** /models/i/{instance_id}/episodes/{episode_name}/wipe | Wipe all events from an episode
*ServerApi* | [**get_server_info**](docs/ServerApi.md#get_server_info) | **GET** /info | Get server information
*ServerApi* | [**ping_server**](docs/ServerApi.md#ping_server) | **GET** /ping | Health check endpoint


## Documentation For Models

 - [AttachEventsToEpisodeRequest](docs/AttachEventsToEpisodeRequest.md)
 - [AttachEventsToEpisodeRequestEventsInner](docs/AttachEventsToEpisodeRequestEventsInner.md)
 - [AttachMetadataToEventRequest](docs/AttachMetadataToEventRequest.md)
 - [AvailableModel](docs/AvailableModel.md)
 - [AvailableModelDetails](docs/AvailableModelDetails.md)
 - [CreateEpisodeRequest](docs/CreateEpisodeRequest.md)
 - [CreateModelInstanceRequest](docs/CreateModelInstanceRequest.md)
 - [CreateModelInstanceResponse](docs/CreateModelInstanceResponse.md)
 - [DeleteModelInstanceRequest](docs/DeleteModelInstanceRequest.md)
 - [EpisodeInfo](docs/EpisodeInfo.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [InferRequest](docs/InferRequest.md)
 - [InferResponse](docs/InferResponse.md)
 - [LearnRequest](docs/LearnRequest.md)
 - [LearnResponse](docs/LearnResponse.md)
 - [ModelInstance](docs/ModelInstance.md)
 - [ModelInstanceParameters](docs/ModelInstanceParameters.md)
 - [ModelInstanceState](docs/ModelInstanceState.md)
 - [NotFoundResponse](docs/NotFoundResponse.md)
 - [PingResponse](docs/PingResponse.md)
 - [ServerInfo](docs/ServerInfo.md)
 - [SuccessResponse](docs/SuccessResponse.md)
 - [TokenGenerateResponse](docs/TokenGenerateResponse.md)
 - [TokenRolesResponse](docs/TokenRolesResponse.md)
 - [UnauthorizedResponse](docs/UnauthorizedResponse.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="ApiKeyAuth"></a>
### ApiKeyAuth

- **Type**: Bearer authentication


## Author




