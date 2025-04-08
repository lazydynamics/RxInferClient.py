# ModelInstanceState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **Dict[str, object]** | An object containing the current state of the model instance.  May include arbitrary fields specific to the model. See the model documentation for more details.  | 

## Example

```python
from rxinfer_openapi.models.model_instance_state import ModelInstanceState

# TODO update the JSON string below
json = "{}"
# create an instance of ModelInstanceState from a JSON string
model_instance_state_instance = ModelInstanceState.from_json(json)
# print the JSON string representation of the object
print(ModelInstanceState.to_json())

# convert the object into a dict
model_instance_state_dict = model_instance_state_instance.to_dict()
# create an instance of ModelInstanceState from a dict
model_instance_state_from_dict = ModelInstanceState.from_dict(model_instance_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


