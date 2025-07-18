# openapi_client.MarketApi

All URIs are relative to *https://api.torn.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ad0c908328835d9672d157fe84eac884**](MarketApi.md#ad0c908328835d9672d157fe84eac884) | **GET** /market/timestamp | Get current server time
[**call_17e406574ff1eb686891c0fb0e15343a**](MarketApi.md#call_17e406574ff1eb686891c0fb0e15343a) | **GET** /market/{propertyTypeId}/properties | Get properties market listings
[**call_22a00095ad734485b6dacdc12c1f62ff**](MarketApi.md#call_22a00095ad734485b6dacdc12c1f62ff) | **GET** /market/lookup | Get all available market selections
[**call_38cd1a2c47e266a703a13e0dd401f4a9**](MarketApi.md#call_38cd1a2c47e266a703a13e0dd401f4a9) | **GET** /market/{propertyTypeId}/rentals | Get properties rental listings
[**call_422876deda064e2f3a2cc3c4bf6d73a9**](MarketApi.md#call_422876deda064e2f3a2cc3c4bf6d73a9) | **GET** /market/bazaar | Get bazaar directory
[**call_8254489388603bf1b21740e6f71bef06**](MarketApi.md#call_8254489388603bf1b21740e6f71bef06) | **GET** /market/{id}/bazaar | Get item specialized bazaar directory
[**call_8e78be3fa3d353f59f8654fcc1c2199c**](MarketApi.md#call_8e78be3fa3d353f59f8654fcc1c2199c) | **GET** /market | Get any Market selection
[**f535a33bf405e7bd60918e536f827e5c**](MarketApi.md#f535a33bf405e7bd60918e536f827e5c) | **GET** /market/{id}/itemmarket | Get item market listings


# **ad0c908328835d9672d157fe84eac884**
> TimestampResponse ad0c908328835d9672d157fe84eac884(timestamp=timestamp, comment=comment, key=key)

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
    api_instance = openapi_client.MarketApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get current server time
        api_response = api_instance.ad0c908328835d9672d157fe84eac884(timestamp=timestamp, comment=comment, key=key)
        print("The response of MarketApi->ad0c908328835d9672d157fe84eac884:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketApi->ad0c908328835d9672d157fe84eac884: %s\n" % e)
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

# **call_17e406574ff1eb686891c0fb0e15343a**
> MarketPropertiesResponse call_17e406574ff1eb686891c0fb0e15343a(property_type_id, offset=offset, limit=limit, sort=sort, timestamp=timestamp, comment=comment, key=key)

Get properties market listings

Requires public access key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.market_properties_response import MarketPropertiesResponse
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
    api_instance = openapi_client.MarketApi(api_client)
    property_type_id = 56 # int | Property type id
    offset = 0 # int |  (optional) (default to 0)
    limit = 20 # int |  (optional) (default to 20)
    sort = 'sort_example' # str | Sorted by the greatest timestamps (optional)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get properties market listings
        api_response = api_instance.call_17e406574ff1eb686891c0fb0e15343a(property_type_id, offset=offset, limit=limit, sort=sort, timestamp=timestamp, comment=comment, key=key)
        print("The response of MarketApi->call_17e406574ff1eb686891c0fb0e15343a:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketApi->call_17e406574ff1eb686891c0fb0e15343a: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_type_id** | **int**| Property type id | 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 20]
 **sort** | **str**| Sorted by the greatest timestamps | [optional] 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**MarketPropertiesResponse**](MarketPropertiesResponse.md)

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

# **call_22a00095ad734485b6dacdc12c1f62ff**
> MarketLookupResponse call_22a00095ad734485b6dacdc12c1f62ff(timestamp=timestamp, comment=comment, key=key)

Get all available market selections

Requires public access key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.market_lookup_response import MarketLookupResponse
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
    api_instance = openapi_client.MarketApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get all available market selections
        api_response = api_instance.call_22a00095ad734485b6dacdc12c1f62ff(timestamp=timestamp, comment=comment, key=key)
        print("The response of MarketApi->call_22a00095ad734485b6dacdc12c1f62ff:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketApi->call_22a00095ad734485b6dacdc12c1f62ff: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**MarketLookupResponse**](MarketLookupResponse.md)

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

# **call_38cd1a2c47e266a703a13e0dd401f4a9**
> MarketRentalsResponse call_38cd1a2c47e266a703a13e0dd401f4a9(property_type_id, offset=offset, limit=limit, sort=sort, timestamp=timestamp, comment=comment, key=key)

Get properties rental listings

Requires public access key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.market_rentals_response import MarketRentalsResponse
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
    api_instance = openapi_client.MarketApi(api_client)
    property_type_id = 56 # int | Property type id
    offset = 0 # int |  (optional) (default to 0)
    limit = 20 # int |  (optional) (default to 20)
    sort = 'sort_example' # str | Sorted by the greatest timestamps (optional)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get properties rental listings
        api_response = api_instance.call_38cd1a2c47e266a703a13e0dd401f4a9(property_type_id, offset=offset, limit=limit, sort=sort, timestamp=timestamp, comment=comment, key=key)
        print("The response of MarketApi->call_38cd1a2c47e266a703a13e0dd401f4a9:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketApi->call_38cd1a2c47e266a703a13e0dd401f4a9: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_type_id** | **int**| Property type id | 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 20]
 **sort** | **str**| Sorted by the greatest timestamps | [optional] 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**MarketRentalsResponse**](MarketRentalsResponse.md)

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

# **call_422876deda064e2f3a2cc3c4bf6d73a9**
> BazaarResponse call_422876deda064e2f3a2cc3c4bf6d73a9(cat=cat, timestamp=timestamp, comment=comment, key=key)

Get bazaar directory

Requires public access key. <br> The default response is of type 'BazaarWeekly', but if a category is chosen, the response will be of type 'BazaarSpecialized'.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.bazaar_response import BazaarResponse
from openapi_client.models.market_specialized_bazaar_category_enum import MarketSpecializedBazaarCategoryEnum
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
    api_instance = openapi_client.MarketApi(api_client)
    cat = openapi_client.MarketSpecializedBazaarCategoryEnum() # MarketSpecializedBazaarCategoryEnum | Category of specialized bazaars returned (optional)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get bazaar directory
        api_response = api_instance.call_422876deda064e2f3a2cc3c4bf6d73a9(cat=cat, timestamp=timestamp, comment=comment, key=key)
        print("The response of MarketApi->call_422876deda064e2f3a2cc3c4bf6d73a9:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketApi->call_422876deda064e2f3a2cc3c4bf6d73a9: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cat** | [**MarketSpecializedBazaarCategoryEnum**](.md)| Category of specialized bazaars returned | [optional] 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**BazaarResponse**](BazaarResponse.md)

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

# **call_8254489388603bf1b21740e6f71bef06**
> BazaarResponseSpecialized call_8254489388603bf1b21740e6f71bef06(id, timestamp=timestamp, comment=comment, key=key)

Get item specialized bazaar directory

Requires public access key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.bazaar_response_specialized import BazaarResponseSpecialized
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
    api_instance = openapi_client.MarketApi(api_client)
    id = 56 # int | Item id
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get item specialized bazaar directory
        api_response = api_instance.call_8254489388603bf1b21740e6f71bef06(id, timestamp=timestamp, comment=comment, key=key)
        print("The response of MarketApi->call_8254489388603bf1b21740e6f71bef06:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketApi->call_8254489388603bf1b21740e6f71bef06: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Item id | 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**BazaarResponseSpecialized**](BazaarResponseSpecialized.md)

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

# **call_8e78be3fa3d353f59f8654fcc1c2199c**
> Model8e78be3fa3d353f59f8654fcc1c2199c200Response call_8e78be3fa3d353f59f8654fcc1c2199c(selections=selections, id=id, cat=cat, bonus=bonus, sort=sort, offset=offset, limit=limit, timestamp=timestamp, comment=comment, key=key)

Get any Market selection

Requires public access key. <br>Choose one or more selections (comma separated).

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.market_selection_name import MarketSelectionName
from openapi_client.models.market_specialized_bazaar_category_enum import MarketSpecializedBazaarCategoryEnum
from openapi_client.models.model8e78be3fa3d353f59f8654fcc1c2199c200_response import Model8e78be3fa3d353f59f8654fcc1c2199c200Response
from openapi_client.models.weapon_bonus_enum import WeaponBonusEnum
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
    api_instance = openapi_client.MarketApi(api_client)
    selections = [openapi_client.MarketSelectionName()] # List[MarketSelectionName] | Selection names (optional)
    id = openapi_client.Model8e78be3fa3d353f59f8654fcc1c2199cIdParameter() # Model8e78be3fa3d353f59f8654fcc1c2199cIdParameter | selection id (optional)
    cat = openapi_client.MarketSpecializedBazaarCategoryEnum() # MarketSpecializedBazaarCategoryEnum | Category of specialized bazaars returned (optional)
    bonus = openapi_client.WeaponBonusEnum() # WeaponBonusEnum | Used to filter weapons with a specific bonus (optional)
    sort = 'sort_example' # str | Direction to sort rows in (optional)
    offset = 56 # int |  (optional)
    limit = 20 # int |  (optional) (default to 20)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get any Market selection
        api_response = api_instance.call_8e78be3fa3d353f59f8654fcc1c2199c(selections=selections, id=id, cat=cat, bonus=bonus, sort=sort, offset=offset, limit=limit, timestamp=timestamp, comment=comment, key=key)
        print("The response of MarketApi->call_8e78be3fa3d353f59f8654fcc1c2199c:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketApi->call_8e78be3fa3d353f59f8654fcc1c2199c: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **selections** | [**List[MarketSelectionName]**](MarketSelectionName.md)| Selection names | [optional] 
 **id** | [**Model8e78be3fa3d353f59f8654fcc1c2199cIdParameter**](.md)| selection id | [optional] 
 **cat** | [**MarketSpecializedBazaarCategoryEnum**](.md)| Category of specialized bazaars returned | [optional] 
 **bonus** | [**WeaponBonusEnum**](.md)| Used to filter weapons with a specific bonus | [optional] 
 **sort** | **str**| Direction to sort rows in | [optional] 
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 20]
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**Model8e78be3fa3d353f59f8654fcc1c2199c200Response**](Model8e78be3fa3d353f59f8654fcc1c2199c200Response.md)

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

# **f535a33bf405e7bd60918e536f827e5c**
> MarketItemMarketResponse f535a33bf405e7bd60918e536f827e5c(id, bonus=bonus, offset=offset, timestamp=timestamp, comment=comment, key=key)

Get item market listings

Requires public access key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.market_item_market_response import MarketItemMarketResponse
from openapi_client.models.weapon_bonus_enum import WeaponBonusEnum
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
    api_instance = openapi_client.MarketApi(api_client)
    id = 56 # int | Item id
    bonus = openapi_client.WeaponBonusEnum() # WeaponBonusEnum | Used to filter weapons with a specific bonus. (optional)
    offset = 0 # int |  (optional) (default to 0)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get item market listings
        api_response = api_instance.f535a33bf405e7bd60918e536f827e5c(id, bonus=bonus, offset=offset, timestamp=timestamp, comment=comment, key=key)
        print("The response of MarketApi->f535a33bf405e7bd60918e536f827e5c:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketApi->f535a33bf405e7bd60918e536f827e5c: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Item id | 
 **bonus** | [**WeaponBonusEnum**](.md)| Used to filter weapons with a specific bonus. | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**MarketItemMarketResponse**](MarketItemMarketResponse.md)

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

