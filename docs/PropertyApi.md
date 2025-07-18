# openapi_client.PropertyApi

All URIs are relative to *https://api.torn.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**call_2a45b6d9d77224d9a1e13d0b698f6c4b**](PropertyApi.md#call_2a45b6d9d77224d9a1e13d0b698f6c4b) | **GET** /property | Get any property selection
[**call_423c130a5cdf6bc801c42537c07fddec**](PropertyApi.md#call_423c130a5cdf6bc801c42537c07fddec) | **GET** /property/timestamp | Get current server time
[**call_87bd73ddaf3749bce7cbf5aa28e921e2**](PropertyApi.md#call_87bd73ddaf3749bce7cbf5aa28e921e2) | **GET** /property/{id}/property | Get a specific property
[**call_87fe6e3a7ec186e108922fed781c8d6d**](PropertyApi.md#call_87fe6e3a7ec186e108922fed781c8d6d) | **GET** /property/lookup | Get all available property selections


# **call_2a45b6d9d77224d9a1e13d0b698f6c4b**
> Model2a45b6d9d77224d9a1e13d0b698f6c4b200Response call_2a45b6d9d77224d9a1e13d0b698f6c4b(id, selections=selections, timestamp=timestamp, comment=comment, key=key)

Get any property selection

Requires public access key. <br>Choose one or more selections (comma separated).

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.model2a45b6d9d77224d9a1e13d0b698f6c4b200_response import Model2a45b6d9d77224d9a1e13d0b698f6c4b200Response
from openapi_client.models.property_selection_name import PropertySelectionName
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
    api_instance = openapi_client.PropertyApi(api_client)
    id = 56 # int | Property id
    selections = [openapi_client.PropertySelectionName()] # List[PropertySelectionName] | Selection names (optional)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get any property selection
        api_response = api_instance.call_2a45b6d9d77224d9a1e13d0b698f6c4b(id, selections=selections, timestamp=timestamp, comment=comment, key=key)
        print("The response of PropertyApi->call_2a45b6d9d77224d9a1e13d0b698f6c4b:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyApi->call_2a45b6d9d77224d9a1e13d0b698f6c4b: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Property id | 
 **selections** | [**List[PropertySelectionName]**](PropertySelectionName.md)| Selection names | [optional] 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**Model2a45b6d9d77224d9a1e13d0b698f6c4b200Response**](Model2a45b6d9d77224d9a1e13d0b698f6c4b200Response.md)

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

# **call_423c130a5cdf6bc801c42537c07fddec**
> TimestampResponse call_423c130a5cdf6bc801c42537c07fddec(timestamp=timestamp, comment=comment, key=key)

Get current server time

Requires public access key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.timestamp_response import TimestampResponse
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
    api_instance = openapi_client.PropertyApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get current server time
        api_response = api_instance.call_423c130a5cdf6bc801c42537c07fddec(timestamp=timestamp, comment=comment, key=key)
        print("The response of PropertyApi->call_423c130a5cdf6bc801c42537c07fddec:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyApi->call_423c130a5cdf6bc801c42537c07fddec: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**TimestampResponse**](TimestampResponse.md)

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

# **call_87bd73ddaf3749bce7cbf5aa28e921e2**
> UserPropertyResponse call_87bd73ddaf3749bce7cbf5aa28e921e2(id, timestamp=timestamp, comment=comment, key=key)

Get a specific property

Requires public access key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.user_property_response import UserPropertyResponse
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
    api_instance = openapi_client.PropertyApi(api_client)
    id = 56 # int | Property id
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get a specific property
        api_response = api_instance.call_87bd73ddaf3749bce7cbf5aa28e921e2(id, timestamp=timestamp, comment=comment, key=key)
        print("The response of PropertyApi->call_87bd73ddaf3749bce7cbf5aa28e921e2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyApi->call_87bd73ddaf3749bce7cbf5aa28e921e2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Property id | 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**UserPropertyResponse**](UserPropertyResponse.md)

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

# **call_87fe6e3a7ec186e108922fed781c8d6d**
> PropertyLookupResponse call_87fe6e3a7ec186e108922fed781c8d6d(timestamp=timestamp, comment=comment, key=key)

Get all available property selections

Requires public access key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.property_lookup_response import PropertyLookupResponse
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
    api_instance = openapi_client.PropertyApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get all available property selections
        api_response = api_instance.call_87fe6e3a7ec186e108922fed781c8d6d(timestamp=timestamp, comment=comment, key=key)
        print("The response of PropertyApi->call_87fe6e3a7ec186e108922fed781c8d6d:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyApi->call_87fe6e3a7ec186e108922fed781c8d6d: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**PropertyLookupResponse**](PropertyLookupResponse.md)

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

