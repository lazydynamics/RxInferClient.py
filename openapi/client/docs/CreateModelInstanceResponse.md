# CreateModelInstanceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_id** | **str** | Unique identifier for the created model instance | 

## Example

```python
from rxinfer_openapi.models.create_model_instance_response import CreateModelInstanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateModelInstanceResponse from a JSON string
create_model_instance_response_instance = CreateModelInstanceResponse.from_json(json)
# print the JSON string representation of the object
print(CreateModelInstanceResponse.to_json())

# convert the object into a dict
create_model_instance_response_dict = create_model_instance_response_instance.to_dict()
# create an instance of CreateModelInstanceResponse from a dict
create_model_instance_response_from_dict = CreateModelInstanceResponse.from_dict(create_model_instance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


