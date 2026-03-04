# ErrorResponse


**Source:** `waylay.services.alarms.models.error_response`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** |  | 
**error** | **str** |  | 


## Example

```python
from waylay.services.alarms.models.error_response import ErrorResponse

error_response = ErrorResponse(status_code=..., error=...)

# Create from JSON
error_response = ErrorResponse.from_json('{ "statusCode": ..., "error": ... }')

# Export to dictionary
error_response_dict = error_response.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


