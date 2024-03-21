# IdObject

A JSON object with an id field indicating the resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 

## Example

```python
from waylay.services.alarms.models.id_object import IdObject

# TODO update the JSON string below
json = "{}"
# create an instance of IdObject from a JSON string
id_object_instance = IdObject.from_json(json)
# print the JSON string representation of the object
print IdObject.to_json()

# convert the object into a dict
id_object_dict = id_object_instance.to_dict()
# create an instance of IdObject from a dict
id_object_form_dict = id_object.from_dict(id_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


