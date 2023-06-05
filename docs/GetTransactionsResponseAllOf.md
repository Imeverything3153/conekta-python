# GetTransactionsResponseAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TransactionResponse]**](TransactionResponse.md) | Transactions | [optional] 

## Example

```python
from conekta.models.get_transactions_response_all_of import GetTransactionsResponseAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionsResponseAllOf from a JSON string
get_transactions_response_all_of_instance = GetTransactionsResponseAllOf.from_json(json)
# print the JSON string representation of the object
print GetTransactionsResponseAllOf.to_json()

# convert the object into a dict
get_transactions_response_all_of_dict = get_transactions_response_all_of_instance.to_dict()
# create an instance of GetTransactionsResponseAllOf from a dict
get_transactions_response_all_of_form_dict = get_transactions_response_all_of.from_dict(get_transactions_response_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

