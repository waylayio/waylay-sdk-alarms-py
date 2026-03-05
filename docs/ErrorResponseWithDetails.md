# ErrorResponseWithDetails


**Source:** `waylay.services.alarms.models.error_response_with_details`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** |  | 
**error** | **str** |  | 
**details** | **List[str]** |  | [optional] 


## Example

```python
from waylay.services.alarms.models.error_response_with_details import (
    ErrorResponseWithDetails,
)

error_response_with_details = ErrorResponseWithDetails(
    status_code=..., error=..., details=...
)

# Create from JSON
error_response_with_details = ErrorResponseWithDetails.from_json(
    '{ "statusCode": ..., "error": ..., "details": ... }'
)

# Export to dictionary
error_response_with_details_dict = error_response_with_details.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


