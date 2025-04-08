# AvailableModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | [**AvailableModelDetails**](AvailableModelDetails.md) |  | 
**config** | **Dict[str, object]** | The entire model configuration as in the &#x60;config.yaml&#x60; file.  May include arbitrary fields, which are not part of the public interface. Note that this information also includes the properties from the &#x60;details&#x60; object.  | 

## Example

```python
from rxinfer_openapi.models.available_model import AvailableModel

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableModel from a JSON string
available_model_instance = AvailableModel.from_json(json)
# print the JSON string representation of the object
print(AvailableModel.to_json())

# convert the object into a dict
available_model_dict = available_model_instance.to_dict()
# create an instance of AvailableModel from a dict
available_model_from_dict = AvailableModel.from_dict(available_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


