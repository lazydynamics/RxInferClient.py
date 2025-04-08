# AttachEventsToEpisodeRequestEventsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** | Timestamp of the event | [optional] 
**data** | **Dict[str, object]** | Arbitrary data to attach to the event, model-specific | [optional] 
**metadata** | **Dict[str, object]** | Arbitrary metadata to attach to the event, model-specific | [optional] 

## Example

```python
from rxinferclient.models.attach_events_to_episode_request_events_inner import AttachEventsToEpisodeRequestEventsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AttachEventsToEpisodeRequestEventsInner from a JSON string
attach_events_to_episode_request_events_inner_instance = AttachEventsToEpisodeRequestEventsInner.from_json(json)
# print the JSON string representation of the object
print(AttachEventsToEpisodeRequestEventsInner.to_json())

# convert the object into a dict
attach_events_to_episode_request_events_inner_dict = attach_events_to_episode_request_events_inner_instance.to_dict()
# create an instance of AttachEventsToEpisodeRequestEventsInner from a dict
attach_events_to_episode_request_events_inner_from_dict = AttachEventsToEpisodeRequestEventsInner.from_dict(attach_events_to_episode_request_events_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


