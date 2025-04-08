# coding: utf-8

# flake8: noqa

"""
    RxInferServer OpenAPI specification

    API for RxInferServer.jl - A Julia server for RxInfer probabilistic programming framework **Warning** The specification is not yet stable and may undergo significant changes. 

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "0.1.0"

# import apis into sdk package
from rxinfer_openapi.api.authentication_api import AuthenticationApi
from rxinfer_openapi.api.models_api import ModelsApi
from rxinfer_openapi.api.server_api import ServerApi

# import ApiClient
from rxinfer_openapi.api_response import ApiResponse
from rxinfer_openapi.api_client import ApiClient
from rxinfer_openapi.configuration import Configuration
from rxinfer_openapi.exceptions import OpenApiException
from rxinfer_openapi.exceptions import ApiTypeError
from rxinfer_openapi.exceptions import ApiValueError
from rxinfer_openapi.exceptions import ApiKeyError
from rxinfer_openapi.exceptions import ApiAttributeError
from rxinfer_openapi.exceptions import ApiException

# import models into sdk package
from rxinfer_openapi.models.attach_events_to_episode_request import AttachEventsToEpisodeRequest
from rxinfer_openapi.models.attach_events_to_episode_request_events_inner import AttachEventsToEpisodeRequestEventsInner
from rxinfer_openapi.models.attach_metadata_to_event_request import AttachMetadataToEventRequest
from rxinfer_openapi.models.available_model import AvailableModel
from rxinfer_openapi.models.available_model_details import AvailableModelDetails
from rxinfer_openapi.models.create_episode_request import CreateEpisodeRequest
from rxinfer_openapi.models.create_model_instance_request import CreateModelInstanceRequest
from rxinfer_openapi.models.create_model_instance_response import CreateModelInstanceResponse
from rxinfer_openapi.models.delete_model_instance_request import DeleteModelInstanceRequest
from rxinfer_openapi.models.episode_info import EpisodeInfo
from rxinfer_openapi.models.error_response import ErrorResponse
from rxinfer_openapi.models.infer_request import InferRequest
from rxinfer_openapi.models.infer_response import InferResponse
from rxinfer_openapi.models.learn_request import LearnRequest
from rxinfer_openapi.models.learn_response import LearnResponse
from rxinfer_openapi.models.model_instance import ModelInstance
from rxinfer_openapi.models.model_instance_parameters import ModelInstanceParameters
from rxinfer_openapi.models.model_instance_state import ModelInstanceState
from rxinfer_openapi.models.not_found_response import NotFoundResponse
from rxinfer_openapi.models.ping_response import PingResponse
from rxinfer_openapi.models.server_info import ServerInfo
from rxinfer_openapi.models.success_response import SuccessResponse
from rxinfer_openapi.models.token_generate_response import TokenGenerateResponse
from rxinfer_openapi.models.token_roles_response import TokenRolesResponse
from rxinfer_openapi.models.unauthorized_response import UnauthorizedResponse
