# AttachMetadataToEventRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **Dict[str, object]** | Metadata to attach to the event | 

## Example

```python
from rxinferclient.models.attach_metadata_to_event_request import AttachMetadataToEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AttachMetadataToEventRequest from a JSON string
attach_metadata_to_event_request_instance = AttachMetadataToEventRequest.from_json(json)
# print the JSON string representation of the object
print(AttachMetadataToEventRequest.to_json())

# convert the object into a dict
attach_metadata_to_event_request_dict = attach_metadata_to_event_request_instance.to_dict()
# create an instance of AttachMetadataToEventRequest from a dict
attach_metadata_to_event_request_from_dict = AttachMetadataToEventRequest.from_dict(attach_metadata_to_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


