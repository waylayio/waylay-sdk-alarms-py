# VersionResponse


**Source:** `waylay.services.alarms.models.version_response`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | 
**name** | **str** |  | 


## Example

```python
from waylay.services.alarms.models.version_response import VersionResponse

version_response = VersionResponse(version=..., name=...)

# Create from JSON
version_response = VersionResponse.from_json('{ "version": ..., "name": ... }')

# Export to dictionary
version_response_dict = version_response.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


