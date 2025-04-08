# InferResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **int** | Unique identifier for the inference event | 
**results** | **Dict[str, object]** | Model-specific results of the inference | 
**errors** | [**List[ErrorResponse]**](ErrorResponse.md) | List of errors that occurred during the inference call, but were not fatal and the inference was still completed successfully | 

## Example

```python
from rxinfer_openapi.models.infer_response import InferResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InferResponse from a JSON string
infer_response_instance = InferResponse.from_json(json)
# print the JSON string representation of the object
print(InferResponse.to_json())

# convert the object into a dict
infer_response_dict = infer_response_instance.to_dict()
# create an instance of InferResponse from a dict
infer_response_from_dict = InferResponse.from_dict(infer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


