# InferRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **Dict[str, object]** | Model-specific data to run inference on | 
**timestamp** | **datetime** | Timestamp of the inference request, used to mark the event in the episode | [optional] 
**episode_name** | **str** | Name of the episode to run inference on | [optional] default to 'default'

## Example

```python
from rxinfer_openapi.models.infer_request import InferRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InferRequest from a JSON string
infer_request_instance = InferRequest.from_json(json)
# print the JSON string representation of the object
print(InferRequest.to_json())

# convert the object into a dict
infer_request_dict = infer_request_instance.to_dict()
# create an instance of InferRequest from a dict
infer_request_from_dict = InferRequest.from_dict(infer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


