# IdObject

A JSON object with an id field indicating the resource.

**Source:** `waylay.services.alarms.models.id_object`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 


## Example

```python
from waylay.services.alarms.models.id_object import IdObject

id_object = IdObject(id=...)

# Create from JSON
id_object = IdObject.from_json('{ "id": ... }')

# Export to dictionary
id_object_dict = id_object.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


