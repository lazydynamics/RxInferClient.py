# AttachEventsToEpisodeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[AttachEventsToEpisodeRequestEventsInner]**](AttachEventsToEpisodeRequestEventsInner.md) | List of events to attach to the episode | 

## Example

```python
from rxinfer_openapi.models.attach_events_to_episode_request import AttachEventsToEpisodeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AttachEventsToEpisodeRequest from a JSON string
attach_events_to_episode_request_instance = AttachEventsToEpisodeRequest.from_json(json)
# print the JSON string representation of the object
print(AttachEventsToEpisodeRequest.to_json())

# convert the object into a dict
attach_events_to_episode_request_dict = attach_events_to_episode_request_instance.to_dict()
# create an instance of AttachEventsToEpisodeRequest from a dict
attach_events_to_episode_request_from_dict = AttachEventsToEpisodeRequest.from_dict(attach_events_to_episode_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


