# LearnRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**episodes** | **List[str]** | List of episodes to learn from | [default to ["default"]]

## Example

```python
from rxinfer_openapi.models.learn_request import LearnRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LearnRequest from a JSON string
learn_request_instance = LearnRequest.from_json(json)
# print the JSON string representation of the object
print(LearnRequest.to_json())

# convert the object into a dict
learn_request_dict = learn_request_instance.to_dict()
# create an instance of LearnRequest from a dict
learn_request_from_dict = LearnRequest.from_dict(learn_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


