# UnauthorizedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Error type, always \&quot;Unauthorized\&quot; for this error | 
**message** | **str** | Detailed message explaining why authentication failed | 

## Example

```python
from rxinferclient.models.unauthorized_response import UnauthorizedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnauthorizedResponse from a JSON string
unauthorized_response_instance = UnauthorizedResponse.from_json(json)
# print the JSON string representation of the object
print(UnauthorizedResponse.to_json())

# convert the object into a dict
unauthorized_response_dict = unauthorized_response_instance.to_dict()
# create an instance of UnauthorizedResponse from a dict
unauthorized_response_from_dict = UnauthorizedResponse.from_dict(unauthorized_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


