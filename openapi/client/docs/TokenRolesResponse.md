# TokenRolesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roles** | **List[str]** | List of roles for the token | 

## Example

```python
from rxinfer_openapi.models.token_roles_response import TokenRolesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TokenRolesResponse from a JSON string
token_roles_response_instance = TokenRolesResponse.from_json(json)
# print the JSON string representation of the object
print(TokenRolesResponse.to_json())

# convert the object into a dict
token_roles_response_dict = token_roles_response_instance.to_dict()
# create an instance of TokenRolesResponse from a dict
token_roles_response_from_dict = TokenRolesResponse.from_dict(token_roles_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


