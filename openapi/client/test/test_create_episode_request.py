# coding: utf-8

"""
    RxInferServer OpenAPI specification

    API for RxInferServer.jl - A Julia server for RxInfer probabilistic programming framework **Warning** The specification is not yet stable and may undergo significant changes. 

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from rxinfer_openapi.models.create_episode_request import CreateEpisodeRequest

class TestCreateEpisodeRequest(unittest.TestCase):
    """CreateEpisodeRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateEpisodeRequest:
        """Test CreateEpisodeRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateEpisodeRequest`
        """
        model = CreateEpisodeRequest()
        if include_optional:
            return CreateEpisodeRequest(
                name = ''
            )
        else:
            return CreateEpisodeRequest(
                name = '',
        )
        """

    def testCreateEpisodeRequest(self):
        """Test CreateEpisodeRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
