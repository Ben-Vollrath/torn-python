# openapi_client.KeyApi

All URIs are relative to *https://api.torn.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**c6ccbb0a05ebf3b307c82a4c89275e52**](KeyApi.md#c6ccbb0a05ebf3b307c82a4c89275e52) | **GET** /key | Get any Key selection
[**call_0d6dae59c9b3419c18d2a4ca0da757e6**](KeyApi.md#call_0d6dae59c9b3419c18d2a4ca0da757e6) | **GET** /key/log | Get current key log history
[**e6d387f16971004628eeca2d6473f825**](KeyApi.md#e6d387f16971004628eeca2d6473f825) | **GET** /key/info | Get current key info


# **c6ccbb0a05ebf3b307c82a4c89275e52**
> C6ccbb0a05ebf3b307c82a4c89275e52200Response c6ccbb0a05ebf3b307c82a4c89275e52(selections=selections, limit=limit, offset=offset, timestamp=timestamp, comment=comment, key=key)

Get any Key selection

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.c6ccbb0a05ebf3b307c82a4c89275e52200_response import C6ccbb0a05ebf3b307c82a4c89275e52200Response
from openapi_client.models.key_selection_name import KeySelectionName
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.torn.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.torn.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KeyApi(api_client)
    selections = [openapi_client.KeySelectionName()] # List[KeySelectionName] | Selection names (optional)
    limit = 100 # int |  (optional) (default to 100)
    offset = 56 # int |  (optional)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get any Key selection
        api_response = api_instance.c6ccbb0a05ebf3b307c82a4c89275e52(selections=selections, limit=limit, offset=offset, timestamp=timestamp, comment=comment, key=key)
        print("The response of KeyApi->c6ccbb0a05ebf3b307c82a4c89275e52:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeyApi->c6ccbb0a05ebf3b307c82a4c89275e52: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **selections** | [**List[KeySelectionName]**](KeySelectionName.md)| Selection names | [optional] 
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**C6ccbb0a05ebf3b307c82a4c89275e52200Response**](C6ccbb0a05ebf3b307c82a4c89275e52200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_0d6dae59c9b3419c18d2a4ca0da757e6**
> KeyLogResponse call_0d6dae59c9b3419c18d2a4ca0da757e6(limit=limit, offset=offset, timestamp=timestamp, comment=comment, key=key)

Get current key log history

Available for any key. <br>
 * This selection contains up to last 250 request logs.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.key_log_response import KeyLogResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.torn.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.torn.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KeyApi(api_client)
    limit = 100 # int |  (optional) (default to 100)
    offset = 56 # int |  (optional)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get current key log history
        api_response = api_instance.call_0d6dae59c9b3419c18d2a4ca0da757e6(limit=limit, offset=offset, timestamp=timestamp, comment=comment, key=key)
        print("The response of KeyApi->call_0d6dae59c9b3419c18d2a4ca0da757e6:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeyApi->call_0d6dae59c9b3419c18d2a4ca0da757e6: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**KeyLogResponse**](KeyLogResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **e6d387f16971004628eeca2d6473f825**
> KeyInfoResponse e6d387f16971004628eeca2d6473f825(timestamp=timestamp, comment=comment, key=key)

Get current key info

Available for any key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.key_info_response import KeyInfoResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.torn.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.torn.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KeyApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get current key info
        api_response = api_instance.e6d387f16971004628eeca2d6473f825(timestamp=timestamp, comment=comment, key=key)
        print("The response of KeyApi->e6d387f16971004628eeca2d6473f825:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeyApi->e6d387f16971004628eeca2d6473f825: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**KeyInfoResponse**](KeyInfoResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

