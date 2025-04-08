# TokenGenerateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | The token to use in the Authorization header with the format \&quot;Bearer {token}\&quot; | 

## Example

```python
from rxinferclient.models.token_generate_response import TokenGenerateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TokenGenerateResponse from a JSON string
token_generate_response_instance = TokenGenerateResponse.from_json(json)
# print the JSON string representation of the object
print(TokenGenerateResponse.to_json())

# convert the object into a dict
token_generate_response_dict = token_generate_response_instance.to_dict()
# create an instance of TokenGenerateResponse from a dict
token_generate_response_from_dict = TokenGenerateResponse.from_dict(token_generate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


