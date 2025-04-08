# CreateModelInstanceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_name** | **str** | The name of the model to create (including version identifier if applicable, e.g. \&quot;BetaBernoulli-v1\&quot;) | 
**arguments** | **Dict[str, object]** | Model-specific configuration arguments | [optional] 
**description** | **str** | Optional description of the model instance | [optional] 

## Example

```python
from rxinferclient.models.create_model_instance_request import CreateModelInstanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateModelInstanceRequest from a JSON string
create_model_instance_request_instance = CreateModelInstanceRequest.from_json(json)
# print the JSON string representation of the object
print(CreateModelInstanceRequest.to_json())

# convert the object into a dict
create_model_instance_request_dict = create_model_instance_request_instance.to_dict()
# create an instance of CreateModelInstanceRequest from a dict
create_model_instance_request_from_dict = CreateModelInstanceRequest.from_dict(create_model_instance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


