# AvailableModelDetails

Primary model details. Note that these are also included in the `config` object. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the model (usually with the version identifier, e.g. \&quot;BetaBernoulli-v1\&quot;) | [optional] 
**description** | **str** | Brief description of the model | [optional] 
**author** | **str** | Author of the model | [optional] 
**roles** | **List[str]** | List of roles that can access the model | [optional] 

## Example

```python
from rxinferclient.models.available_model_details import AvailableModelDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableModelDetails from a JSON string
available_model_details_instance = AvailableModelDetails.from_json(json)
# print the JSON string representation of the object
print(AvailableModelDetails.to_json())

# convert the object into a dict
available_model_details_dict = available_model_details_instance.to_dict()
# create an instance of AvailableModelDetails from a dict
available_model_details_from_dict = AvailableModelDetails.from_dict(available_model_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


