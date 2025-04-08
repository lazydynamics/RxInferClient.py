# ServerInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rxinfer_version** | **str** | The version of RxInfer that the server is using, returns unknown if the version is unknown or hidden | 
**server_version** | **str** | The version of the RxInferServer, returns unknown if the version is unknown or hidden | 
**server_edition** | **str** | The edition of the RxInferServer, as set in RXINFER_EDITION environment variable | 
**julia_version** | **str** | The version of Julia as presented in VERSION | 
**api_version** | **str** | The version of the API being used | [default to 'v1']

## Example

```python
from rxinfer_openapi.models.server_info import ServerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ServerInfo from a JSON string
server_info_instance = ServerInfo.from_json(json)
# print the JSON string representation of the object
print(ServerInfo.to_json())

# convert the object into a dict
server_info_dict = server_info_instance.to_dict()
# create an instance of ServerInfo from a dict
server_info_from_dict = ServerInfo.from_dict(server_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


