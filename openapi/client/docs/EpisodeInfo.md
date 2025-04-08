# EpisodeInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_id** | **str** | ID of the model instance this episode belongs to | 
**episode_name** | **str** | Name of the episode | 
**created_at** | **datetime** | Timestamp of when the episode was created | 
**events** | **List[Dict[str, object]]** | List of events that have occurred in the episode | 

## Example

```python
from rxinfer_openapi.models.episode_info import EpisodeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of EpisodeInfo from a JSON string
episode_info_instance = EpisodeInfo.from_json(json)
# print the JSON string representation of the object
print(EpisodeInfo.to_json())

# convert the object into a dict
episode_info_dict = episode_info_instance.to_dict()
# create an instance of EpisodeInfo from a dict
episode_info_from_dict = EpisodeInfo.from_dict(episode_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


