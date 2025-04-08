# CreateEpisodeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the episode to create | 

## Example

```python
from rxinferclient.models.create_episode_request import CreateEpisodeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEpisodeRequest from a JSON string
create_episode_request_instance = CreateEpisodeRequest.from_json(json)
# print the JSON string representation of the object
print(CreateEpisodeRequest.to_json())

# convert the object into a dict
create_episode_request_dict = create_episode_request_instance.to_dict()
# create an instance of CreateEpisodeRequest from a dict
create_episode_request_from_dict = CreateEpisodeRequest.from_dict(create_episode_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


