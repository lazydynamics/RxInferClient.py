# ModelInstanceParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameters** | **Dict[str, object]** | An object containing the current parameters of the model instance. The keys are the parameter names as defined in the model configuration, and the values are the parameter values.  | 

## Example

```python
from rxinfer_openapi.models.model_instance_parameters import ModelInstanceParameters

# TODO update the JSON string below
json = "{}"
# create an instance of ModelInstanceParameters from a JSON string
model_instance_parameters_instance = ModelInstanceParameters.from_json(json)
# print the JSON string representation of the object
print(ModelInstanceParameters.to_json())

# convert the object into a dict
model_instance_parameters_dict = model_instance_parameters_instance.to_dict()
# create an instance of ModelInstanceParameters from a dict
model_instance_parameters_from_dict = ModelInstanceParameters.from_dict(model_instance_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


