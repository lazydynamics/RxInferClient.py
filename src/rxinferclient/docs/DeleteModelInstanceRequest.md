# DeleteModelInstanceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_id** | **str** | ID of the model instance to delete | 

## Example

```python
from rxinferclient.models.delete_model_instance_request import DeleteModelInstanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteModelInstanceRequest from a JSON string
delete_model_instance_request_instance = DeleteModelInstanceRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteModelInstanceRequest.to_json())

# convert the object into a dict
delete_model_instance_request_dict = delete_model_instance_request_instance.to_dict()
# create an instance of DeleteModelInstanceRequest from a dict
delete_model_instance_request_from_dict = DeleteModelInstanceRequest.from_dict(delete_model_instance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


