# ErrorResponseWithDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** |  | 
**error** | **str** |  | 
**details** | **List[str]** |  | [optional] 

## Example

```python
from waylay.services.alarms.models.error_response_with_details import ErrorResponseWithDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorResponseWithDetails from a JSON string
error_response_with_details_instance = ErrorResponseWithDetails.from_json(json)
# print the JSON string representation of the object
print ErrorResponseWithDetails.to_json()

# convert the object into a dict
error_response_with_details_dict = error_response_with_details_instance.to_dict()
# create an instance of ErrorResponseWithDetails from a dict
error_response_with_details_form_dict = error_response_with_details.from_dict(error_response_with_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


