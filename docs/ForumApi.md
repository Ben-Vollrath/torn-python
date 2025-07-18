# openapi_client.ForumApi

All URIs are relative to *https://api.torn.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**a4618a3901c01413c14b75e984495a9b**](ForumApi.md#a4618a3901c01413c14b75e984495a9b) | **GET** /forum/{threadId}/thread | Get specific thread details
[**call_21915cf0228ce3677261cdce27fb39e2**](ForumApi.md#call_21915cf0228ce3677261cdce27fb39e2) | **GET** /forum | Get any Forum selection
[**call_715cb3a4df0a9bf8094a53dc3259b633**](ForumApi.md#call_715cb3a4df0a9bf8094a53dc3259b633) | **GET** /forum/{categoryIds}/threads | Get threads for specific public forum category or categories
[**call_79b21191b87da275f3b87a7a1a233d04**](ForumApi.md#call_79b21191b87da275f3b87a7a1a233d04) | **GET** /forum/categories | Get publicly available forum categories
[**call_9c5eeb1aebb102b7c62fab11974c359a**](ForumApi.md#call_9c5eeb1aebb102b7c62fab11974c359a) | **GET** /forum/{threadId}/posts | Get specific forum thread posts
[**d2d64a69cedfdce19a50eff117e2c166**](ForumApi.md#d2d64a69cedfdce19a50eff117e2c166) | **GET** /forum/threads | Get threads across all forum categories
[**ec72c2a8cd96c88e4d228221bf6bf42f**](ForumApi.md#ec72c2a8cd96c88e4d228221bf6bf42f) | **GET** /forum/timestamp | Get current server time
[**f0805d0b7ad26c62ddd2fa8d0d332ba4**](ForumApi.md#f0805d0b7ad26c62ddd2fa8d0d332ba4) | **GET** /forum/lookup | Get all available forum selections


# **a4618a3901c01413c14b75e984495a9b**
> ForumThreadResponse a4618a3901c01413c14b75e984495a9b(thread_id, timestamp=timestamp, comment=comment, key=key)

Get specific thread details

Requires public access key. <br>Contains details of a thread including topic content and poll (if any).

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.forum_thread_response import ForumThreadResponse
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
    api_instance = openapi_client.ForumApi(api_client)
    thread_id = 56 # int | Thread id
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get specific thread details
        api_response = api_instance.a4618a3901c01413c14b75e984495a9b(thread_id, timestamp=timestamp, comment=comment, key=key)
        print("The response of ForumApi->a4618a3901c01413c14b75e984495a9b:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ForumApi->a4618a3901c01413c14b75e984495a9b: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **int**| Thread id | 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**ForumThreadResponse**](ForumThreadResponse.md)

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

# **call_21915cf0228ce3677261cdce27fb39e2**
> Model21915cf0228ce3677261cdce27fb39e2200Response call_21915cf0228ce3677261cdce27fb39e2(selections=selections, id=id, striptags=striptags, limit=limit, sort=sort, var_from=var_from, to=to, offset=offset, timestamp=timestamp, comment=comment, key=key)

Get any Forum selection

Requires public access key. <br>Choose one or more selections (comma separated).

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.forum_selection_name import ForumSelectionName
from openapi_client.models.model21915cf0228ce3677261cdce27fb39e2200_response import Model21915cf0228ce3677261cdce27fb39e2200Response
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
    api_instance = openapi_client.ForumApi(api_client)
    selections = [openapi_client.ForumSelectionName()] # List[ForumSelectionName] | Selection names (optional)
    id = openapi_client.Model21915cf0228ce3677261cdce27fb39e2IdParameter() # Model21915cf0228ce3677261cdce27fb39e2IdParameter | selection id (optional)
    striptags = 'striptags_example' # str | Determines if fields include HTML or not ('Hospitalized by <a href=...>user</a>' vs 'Hospitalized by user'). (optional)
    limit = 56 # int |  (optional)
    sort = 'sort_example' # str | Sorted by the greatest timestamps (optional)
    var_from = 56 # int | Timestamp that sets the lower limit for the data returned. Data returned will be after this time (optional)
    to = 56 # int | Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time (optional)
    offset = 56 # int |  (optional)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get any Forum selection
        api_response = api_instance.call_21915cf0228ce3677261cdce27fb39e2(selections=selections, id=id, striptags=striptags, limit=limit, sort=sort, var_from=var_from, to=to, offset=offset, timestamp=timestamp, comment=comment, key=key)
        print("The response of ForumApi->call_21915cf0228ce3677261cdce27fb39e2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ForumApi->call_21915cf0228ce3677261cdce27fb39e2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **selections** | [**List[ForumSelectionName]**](ForumSelectionName.md)| Selection names | [optional] 
 **id** | [**Model21915cf0228ce3677261cdce27fb39e2IdParameter**](.md)| selection id | [optional] 
 **striptags** | **str**| Determines if fields include HTML or not (&#39;Hospitalized by &lt;a href&#x3D;...&gt;user&lt;/a&gt;&#39; vs &#39;Hospitalized by user&#39;). | [optional] 
 **limit** | **int**|  | [optional] 
 **sort** | **str**| Sorted by the greatest timestamps | [optional] 
 **var_from** | **int**| Timestamp that sets the lower limit for the data returned. Data returned will be after this time | [optional] 
 **to** | **int**| Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time | [optional] 
 **offset** | **int**|  | [optional] 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**Model21915cf0228ce3677261cdce27fb39e2200Response**](Model21915cf0228ce3677261cdce27fb39e2200Response.md)

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

# **call_715cb3a4df0a9bf8094a53dc3259b633**
> ForumThreadsResponse call_715cb3a4df0a9bf8094a53dc3259b633(category_ids, limit=limit, sort=sort, var_from=var_from, to=to, timestamp=timestamp, comment=comment, key=key)

Get threads for specific public forum category or categories

Requires public access key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.forum_threads_response import ForumThreadsResponse
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
    api_instance = openapi_client.ForumApi(api_client)
    category_ids = [56] # List[int] | Category id or a list of category ids (comma separated)
    limit = 100 # int |  (optional) (default to 100)
    sort = 'sort_example' # str | Sorted by the greatest timestamps (optional)
    var_from = 56 # int | Timestamp that sets the lower limit for the data returned. Data returned will be after this time (optional)
    to = 56 # int | Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time (optional)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get threads for specific public forum category or categories
        api_response = api_instance.call_715cb3a4df0a9bf8094a53dc3259b633(category_ids, limit=limit, sort=sort, var_from=var_from, to=to, timestamp=timestamp, comment=comment, key=key)
        print("The response of ForumApi->call_715cb3a4df0a9bf8094a53dc3259b633:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ForumApi->call_715cb3a4df0a9bf8094a53dc3259b633: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_ids** | [**List[int]**](int.md)| Category id or a list of category ids (comma separated) | 
 **limit** | **int**|  | [optional] [default to 100]
 **sort** | **str**| Sorted by the greatest timestamps | [optional] 
 **var_from** | **int**| Timestamp that sets the lower limit for the data returned. Data returned will be after this time | [optional] 
 **to** | **int**| Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time | [optional] 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**ForumThreadsResponse**](ForumThreadsResponse.md)

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

# **call_79b21191b87da275f3b87a7a1a233d04**
> ForumCategoriesResponse call_79b21191b87da275f3b87a7a1a233d04(timestamp=timestamp, comment=comment, key=key)

Get publicly available forum categories

Requires public access key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.forum_categories_response import ForumCategoriesResponse
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
    api_instance = openapi_client.ForumApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get publicly available forum categories
        api_response = api_instance.call_79b21191b87da275f3b87a7a1a233d04(timestamp=timestamp, comment=comment, key=key)
        print("The response of ForumApi->call_79b21191b87da275f3b87a7a1a233d04:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ForumApi->call_79b21191b87da275f3b87a7a1a233d04: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**ForumCategoriesResponse**](ForumCategoriesResponse.md)

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

# **call_9c5eeb1aebb102b7c62fab11974c359a**
> ForumPostsResponse call_9c5eeb1aebb102b7c62fab11974c359a(thread_id, offset=offset, striptags=striptags, timestamp=timestamp, comment=comment, key=key)

Get specific forum thread posts

Requires public access key. <br>Returns 20 posts per page for a specific thread.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.forum_posts_response import ForumPostsResponse
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
    api_instance = openapi_client.ForumApi(api_client)
    thread_id = 56 # int | Thread id
    offset = 56 # int |  (optional)
    striptags = true # str | Determines if fields include HTML or not ('Hospitalized by <a href=...>user</a>' vs 'Hospitalized by user'). (optional) (default to true)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get specific forum thread posts
        api_response = api_instance.call_9c5eeb1aebb102b7c62fab11974c359a(thread_id, offset=offset, striptags=striptags, timestamp=timestamp, comment=comment, key=key)
        print("The response of ForumApi->call_9c5eeb1aebb102b7c62fab11974c359a:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ForumApi->call_9c5eeb1aebb102b7c62fab11974c359a: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **int**| Thread id | 
 **offset** | **int**|  | [optional] 
 **striptags** | **str**| Determines if fields include HTML or not (&#39;Hospitalized by &lt;a href&#x3D;...&gt;user&lt;/a&gt;&#39; vs &#39;Hospitalized by user&#39;). | [optional] [default to true]
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**ForumPostsResponse**](ForumPostsResponse.md)

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

# **d2d64a69cedfdce19a50eff117e2c166**
> ForumThreadsResponse d2d64a69cedfdce19a50eff117e2c166(limit=limit, sort=sort, var_from=var_from, to=to, timestamp=timestamp, comment=comment, key=key)

Get threads across all forum categories

Requires public access key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.forum_threads_response import ForumThreadsResponse
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
    api_instance = openapi_client.ForumApi(api_client)
    limit = 100 # int |  (optional) (default to 100)
    sort = 'sort_example' # str | Sorted by the greatest timestamps (optional)
    var_from = 56 # int | Timestamp that sets the lower limit for the data returned. Data returned will be after this time (optional)
    to = 56 # int | Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time (optional)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get threads across all forum categories
        api_response = api_instance.d2d64a69cedfdce19a50eff117e2c166(limit=limit, sort=sort, var_from=var_from, to=to, timestamp=timestamp, comment=comment, key=key)
        print("The response of ForumApi->d2d64a69cedfdce19a50eff117e2c166:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ForumApi->d2d64a69cedfdce19a50eff117e2c166: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 100]
 **sort** | **str**| Sorted by the greatest timestamps | [optional] 
 **var_from** | **int**| Timestamp that sets the lower limit for the data returned. Data returned will be after this time | [optional] 
 **to** | **int**| Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time | [optional] 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**ForumThreadsResponse**](ForumThreadsResponse.md)

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

# **ec72c2a8cd96c88e4d228221bf6bf42f**
> TimestampResponse ec72c2a8cd96c88e4d228221bf6bf42f(timestamp=timestamp, comment=comment, key=key)

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
    api_instance = openapi_client.ForumApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get current server time
        api_response = api_instance.ec72c2a8cd96c88e4d228221bf6bf42f(timestamp=timestamp, comment=comment, key=key)
        print("The response of ForumApi->ec72c2a8cd96c88e4d228221bf6bf42f:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ForumApi->ec72c2a8cd96c88e4d228221bf6bf42f: %s\n" % e)
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

# **f0805d0b7ad26c62ddd2fa8d0d332ba4**
> ForumLookupResponse f0805d0b7ad26c62ddd2fa8d0d332ba4(timestamp=timestamp, comment=comment, key=key)

Get all available forum selections

Requires public access key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.forum_lookup_response import ForumLookupResponse
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
    api_instance = openapi_client.ForumApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get all available forum selections
        api_response = api_instance.f0805d0b7ad26c62ddd2fa8d0d332ba4(timestamp=timestamp, comment=comment, key=key)
        print("The response of ForumApi->f0805d0b7ad26c62ddd2fa8d0d332ba4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ForumApi->f0805d0b7ad26c62ddd2fa8d0d332ba4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**ForumLookupResponse**](ForumLookupResponse.md)

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

