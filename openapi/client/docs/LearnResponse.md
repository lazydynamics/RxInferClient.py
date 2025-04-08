# LearnResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**learned_parameters** | **Dict[str, object]** | A dictionary of learned parameters and their values | 

## Example

```python
from rxinfer_openapi.models.learn_response import LearnResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LearnResponse from a JSON string
learn_response_instance = LearnResponse.from_json(json)
# print the JSON string representation of the object
print(LearnResponse.to_json())

# convert the object into a dict
learn_response_dict = learn_response_instance.to_dict()
# create an instance of LearnResponse from a dict
learn_response_from_dict = LearnResponse.from_dict(learn_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


