# ModelInstance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_id** | **str** | Unique identifier for the created model instance | 
**model_name** | **str** | Name of the model (including version identifier if applicable, e.g. \&quot;BetaBernoulli-v1\&quot;) | 
**created_at** | **datetime** | Timestamp of when the model was created | 
**description** | **str** | Description of the created model instance | 
**arguments** | **Dict[str, object]** | Model-specific configuration arguments | 
**current_episode** | **str** | Name of the current episode for this model | 

## Example

```python
from rxinferclient.models.model_instance import ModelInstance

# TODO update the JSON string below
json = "{}"
# create an instance of ModelInstance from a JSON string
model_instance_instance = ModelInstance.from_json(json)
# print the JSON string representation of the object
print(ModelInstance.to_json())

# convert the object into a dict
model_instance_dict = model_instance_instance.to_dict()
# create an instance of ModelInstance from a dict
model_instance_from_dict = ModelInstance.from_dict(model_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


