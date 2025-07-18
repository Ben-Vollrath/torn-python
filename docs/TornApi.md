# openapi_client.TornApi

All URIs are relative to *https://api.torn.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**a4fedadcac3aada40131288e4e3d6c2d**](TornApi.md#a4fedadcac3aada40131288e4e3d6c2d) | **GET** /torn/{ids}/items | Get information about items
[**ad45b0f57a1109977f605581fc294bda**](TornApi.md#ad45b0f57a1109977f605581fc294bda) | **GET** /torn/{crimeId}/subcrimes | Get Subcrimes information
[**b64b8cf22cd9e9c8916bc01439f6b069**](TornApi.md#b64b8cf22cd9e9c8916bc01439f6b069) | **GET** /torn/organizedcrimes | Get organized crimes information
[**b73ff4e5a9dd28905060da24ca76efde**](TornApi.md#b73ff4e5a9dd28905060da24ca76efde) | **GET** /torn/crimes | Get crimes information
[**c44f572f4672071280a28e6f8217c3b6**](TornApi.md#c44f572f4672071280a28e6f8217c3b6) | **GET** /torn/properties | Get properties details
[**call_0f4c4c07e1dfacbda689b2a0d62ccda4**](TornApi.md#call_0f4c4c07e1dfacbda689b2a0d62ccda4) | **GET** /torn/items | Get information about items
[**call_1846c4cf1e6878553e36571dc9cac29f**](TornApi.md#call_1846c4cf1e6878553e36571dc9cac29f) | **GET** /torn | Get any Torn selection
[**call_279e811630fa497fb2cae268c70992e2**](TornApi.md#call_279e811630fa497fb2cae268c70992e2) | **GET** /torn/bounties | Get bounties
[**call_2a67e4b84813ee97a398be48e544abf5**](TornApi.md#call_2a67e4b84813ee97a398be48e544abf5) | **GET** /torn/factionhof | Get faction hall of fame positions for a specific category
[**call_2baae03f953cd57fd5303dd1d04efae0**](TornApi.md#call_2baae03f953cd57fd5303dd1d04efae0) | **GET** /torn/lookup | Get all available torn selections
[**call_2e799e84fcfa9b722f856e859df909f8**](TornApi.md#call_2e799e84fcfa9b722f856e859df909f8) | **GET** /torn/itemammo | Get information about ammo
[**call_2f68d7e04d218e26005be3eeca6de583**](TornApi.md#call_2f68d7e04d218e26005be3eeca6de583) | **GET** /torn/logcategories | Get available log categories
[**call_37f1828422f3080da21f9eb4aa576686**](TornApi.md#call_37f1828422f3080da21f9eb4aa576686) | **GET** /torn/territory | Get territory details
[**call_61c2d0bc6980cf8d730fe48eb81f417b**](TornApi.md#call_61c2d0bc6980cf8d730fe48eb81f417b) | **GET** /torn/attacklog | Get attack log details
[**call_6f8cffcdae9fe97110b8d46c3991f109**](TornApi.md#call_6f8cffcdae9fe97110b8d46c3991f109) | **GET** /torn/timestamp | Get current server time
[**call_7be904fbcb98a7bb724f0c5b02a37a25**](TornApi.md#call_7be904fbcb98a7bb724f0c5b02a37a25) | **GET** /torn/{logCategoryId}/logtypes | Get available log ids for a specific log category
[**call_80ad6ebd50b6c075427c04d2f54d7af5**](TornApi.md#call_80ad6ebd50b6c075427c04d2f54d7af5) | **GET** /torn/itemmods | Get information about weapon upgrades
[**call_911d56b49218cef2102be3de73f82f01**](TornApi.md#call_911d56b49218cef2102be3de73f82f01) | **GET** /torn/hof | Get player hall of fame positions for a specific category
[**call_992f8b71435ca78ba96f1e5298c25152**](TornApi.md#call_992f8b71435ca78ba96f1e5298c25152) | **GET** /torn/education | Get education information
[**d4cb87bc2502a517c49525b910a6dd82**](TornApi.md#d4cb87bc2502a517c49525b910a6dd82) | **GET** /torn/logtypes | Get all available log ids
[**e95c96ef528248341647a5704630320e**](TornApi.md#e95c96ef528248341647a5704630320e) | **GET** /torn/calendar | Get calendar information
[**f45431b364546bb20b0ca909e9ac686e**](TornApi.md#f45431b364546bb20b0ca909e9ac686e) | **GET** /torn/factiontree | Get full faction tree


# **a4fedadcac3aada40131288e4e3d6c2d**
> TornItemsResponse a4fedadcac3aada40131288e4e3d6c2d(ids, sort=sort, timestamp=timestamp, comment=comment, key=key)

Get information about items

Requires public key.<br>Details are always populated when available.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.torn_items_response import TornItemsResponse
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
    api_instance = openapi_client.TornApi(api_client)
    ids = [56] # List[int] | Item id or a list of item ids (comma separated)
    sort = ASC # str | Sort rows from newest to oldest<br>Default ordering is ascending (optional) (default to ASC)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get information about items
        api_response = api_instance.a4fedadcac3aada40131288e4e3d6c2d(ids, sort=sort, timestamp=timestamp, comment=comment, key=key)
        print("The response of TornApi->a4fedadcac3aada40131288e4e3d6c2d:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TornApi->a4fedadcac3aada40131288e4e3d6c2d: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**List[int]**](int.md)| Item id or a list of item ids (comma separated) | 
 **sort** | **str**| Sort rows from newest to oldest&lt;br&gt;Default ordering is ascending | [optional] [default to ASC]
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**TornItemsResponse**](TornItemsResponse.md)

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

# **ad45b0f57a1109977f605581fc294bda**
> TornSubcrimesResponse ad45b0f57a1109977f605581fc294bda(crime_id, timestamp=timestamp, comment=comment, key=key)

Get Subcrimes information

Requires public access key. <br> Return the details about possible actions for a specific crime.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.torn_subcrimes_response import TornSubcrimesResponse
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
    api_instance = openapi_client.TornApi(api_client)
    crime_id = 56 # int | Crime id
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get Subcrimes information
        api_response = api_instance.ad45b0f57a1109977f605581fc294bda(crime_id, timestamp=timestamp, comment=comment, key=key)
        print("The response of TornApi->ad45b0f57a1109977f605581fc294bda:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TornApi->ad45b0f57a1109977f605581fc294bda: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crime_id** | **int**| Crime id | 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**TornSubcrimesResponse**](TornSubcrimesResponse.md)

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

# **b64b8cf22cd9e9c8916bc01439f6b069**
> TornOrganizedCrimeResponse b64b8cf22cd9e9c8916bc01439f6b069(timestamp=timestamp, comment=comment, key=key)

Get organized crimes information

Requires public access key. <br> Return the details about released faction organized crimes.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.torn_organized_crime_response import TornOrganizedCrimeResponse
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
    api_instance = openapi_client.TornApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get organized crimes information
        api_response = api_instance.b64b8cf22cd9e9c8916bc01439f6b069(timestamp=timestamp, comment=comment, key=key)
        print("The response of TornApi->b64b8cf22cd9e9c8916bc01439f6b069:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TornApi->b64b8cf22cd9e9c8916bc01439f6b069: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**TornOrganizedCrimeResponse**](TornOrganizedCrimeResponse.md)

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

# **b73ff4e5a9dd28905060da24ca76efde**
> TornCrimesResponse b73ff4e5a9dd28905060da24ca76efde(timestamp=timestamp, comment=comment, key=key)

Get crimes information

Requires public access key. <br> Return the details about released crimes.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.torn_crimes_response import TornCrimesResponse
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
    api_instance = openapi_client.TornApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get crimes information
        api_response = api_instance.b73ff4e5a9dd28905060da24ca76efde(timestamp=timestamp, comment=comment, key=key)
        print("The response of TornApi->b73ff4e5a9dd28905060da24ca76efde:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TornApi->b73ff4e5a9dd28905060da24ca76efde: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**TornCrimesResponse**](TornCrimesResponse.md)

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

# **c44f572f4672071280a28e6f8217c3b6**
> TornProperties c44f572f4672071280a28e6f8217c3b6(timestamp=timestamp, comment=comment, key=key)

Get properties details

Requires public access key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.torn_properties import TornProperties
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
    api_instance = openapi_client.TornApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get properties details
        api_response = api_instance.c44f572f4672071280a28e6f8217c3b6(timestamp=timestamp, comment=comment, key=key)
        print("The response of TornApi->c44f572f4672071280a28e6f8217c3b6:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TornApi->c44f572f4672071280a28e6f8217c3b6: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**TornProperties**](TornProperties.md)

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

# **call_0f4c4c07e1dfacbda689b2a0d62ccda4**
> TornItemsResponse call_0f4c4c07e1dfacbda689b2a0d62ccda4(cat=cat, sort=sort, timestamp=timestamp, comment=comment, key=key)

Get information about items

Requires public key.<br>Default category is 'All'.<br>Details are not populated when requesting the category 'All'.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.torn_item_category import TornItemCategory
from openapi_client.models.torn_items_response import TornItemsResponse
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
    api_instance = openapi_client.TornApi(api_client)
    cat = openapi_client.TornItemCategory() # TornItemCategory | Item category type (optional)
    sort = ASC # str | Sort rows from newest to oldest<br>Default ordering is ascending (optional) (default to ASC)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get information about items
        api_response = api_instance.call_0f4c4c07e1dfacbda689b2a0d62ccda4(cat=cat, sort=sort, timestamp=timestamp, comment=comment, key=key)
        print("The response of TornApi->call_0f4c4c07e1dfacbda689b2a0d62ccda4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TornApi->call_0f4c4c07e1dfacbda689b2a0d62ccda4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cat** | [**TornItemCategory**](.md)| Item category type | [optional] 
 **sort** | **str**| Sort rows from newest to oldest&lt;br&gt;Default ordering is ascending | [optional] [default to ASC]
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**TornItemsResponse**](TornItemsResponse.md)

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

# **call_1846c4cf1e6878553e36571dc9cac29f**
> Model1846c4cf1e6878553e36571dc9cac29f200Response call_1846c4cf1e6878553e36571dc9cac29f(selections=selections, id=id, striptags=striptags, limit=limit, to=to, var_from=var_from, sort=sort, cat=cat, offset=offset, timestamp=timestamp, comment=comment, key=key)

Get any Torn selection

Requires public access key. <br> Choose one or more selections (comma separated).

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.model1846c4cf1e6878553e36571dc9cac29f200_response import Model1846c4cf1e6878553e36571dc9cac29f200Response
from openapi_client.models.torn_selection_name import TornSelectionName
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
    api_instance = openapi_client.TornApi(api_client)
    selections = [openapi_client.TornSelectionName()] # List[TornSelectionName] | Selection names (optional)
    id = openapi_client.Model1846c4cf1e6878553e36571dc9cac29fIdParameter() # Model1846c4cf1e6878553e36571dc9cac29fIdParameter | selection id (optional)
    striptags = 'striptags_example' # str | Determines if fields include HTML or not ('Hospitalized by <a href=...>user</a>' vs 'Hospitalized by user'). (optional)
    limit = 56 # int |  (optional)
    to = 56 # int | Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time (optional)
    var_from = 56 # int | Timestamp that sets the lower limit for the data returned. Data returned will be after this time (optional)
    sort = 'sort_example' # str | Sorted by the greatest timestamps (optional)
    cat = openapi_client.Model1846c4cf1e6878553e36571dc9cac29fCatParameter() # Model1846c4cf1e6878553e36571dc9cac29fCatParameter | Selection category (optional)
    offset = 56 # int |  (optional)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get any Torn selection
        api_response = api_instance.call_1846c4cf1e6878553e36571dc9cac29f(selections=selections, id=id, striptags=striptags, limit=limit, to=to, var_from=var_from, sort=sort, cat=cat, offset=offset, timestamp=timestamp, comment=comment, key=key)
        print("The response of TornApi->call_1846c4cf1e6878553e36571dc9cac29f:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TornApi->call_1846c4cf1e6878553e36571dc9cac29f: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **selections** | [**List[TornSelectionName]**](TornSelectionName.md)| Selection names | [optional] 
 **id** | [**Model1846c4cf1e6878553e36571dc9cac29fIdParameter**](.md)| selection id | [optional] 
 **striptags** | **str**| Determines if fields include HTML or not (&#39;Hospitalized by &lt;a href&#x3D;...&gt;user&lt;/a&gt;&#39; vs &#39;Hospitalized by user&#39;). | [optional] 
 **limit** | **int**|  | [optional] 
 **to** | **int**| Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time | [optional] 
 **var_from** | **int**| Timestamp that sets the lower limit for the data returned. Data returned will be after this time | [optional] 
 **sort** | **str**| Sorted by the greatest timestamps | [optional] 
 **cat** | [**Model1846c4cf1e6878553e36571dc9cac29fCatParameter**](.md)| Selection category | [optional] 
 **offset** | **int**|  | [optional] 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**Model1846c4cf1e6878553e36571dc9cac29f200Response**](Model1846c4cf1e6878553e36571dc9cac29f200Response.md)

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

# **call_279e811630fa497fb2cae268c70992e2**
> TornBountiesResponse call_279e811630fa497fb2cae268c70992e2(limit=limit, offset=offset, timestamp=timestamp, comment=comment, key=key)

Get bounties

Requires public key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.torn_bounties_response import TornBountiesResponse
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
    api_instance = openapi_client.TornApi(api_client)
    limit = 100 # int |  (optional) (default to 100)
    offset = 0 # int |  (optional) (default to 0)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get bounties
        api_response = api_instance.call_279e811630fa497fb2cae268c70992e2(limit=limit, offset=offset, timestamp=timestamp, comment=comment, key=key)
        print("The response of TornApi->call_279e811630fa497fb2cae268c70992e2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TornApi->call_279e811630fa497fb2cae268c70992e2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] [default to 0]
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**TornBountiesResponse**](TornBountiesResponse.md)

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

# **call_2a67e4b84813ee97a398be48e544abf5**
> TornFactionHofResponse call_2a67e4b84813ee97a398be48e544abf5(cat, limit=limit, offset=offset, timestamp=timestamp, comment=comment, key=key)

Get faction hall of fame positions for a specific category

Requires public access key. <br> 

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.torn_faction_hof_category import TornFactionHofCategory
from openapi_client.models.torn_faction_hof_response import TornFactionHofResponse
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
    api_instance = openapi_client.TornApi(api_client)
    cat = openapi_client.TornFactionHofCategory() # TornFactionHofCategory | Leaderboards category
    limit = 100 # int |  (optional) (default to 100)
    offset = 0 # int |  (optional) (default to 0)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get faction hall of fame positions for a specific category
        api_response = api_instance.call_2a67e4b84813ee97a398be48e544abf5(cat, limit=limit, offset=offset, timestamp=timestamp, comment=comment, key=key)
        print("The response of TornApi->call_2a67e4b84813ee97a398be48e544abf5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TornApi->call_2a67e4b84813ee97a398be48e544abf5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cat** | [**TornFactionHofCategory**](.md)| Leaderboards category | 
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] [default to 0]
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**TornFactionHofResponse**](TornFactionHofResponse.md)

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

# **call_2baae03f953cd57fd5303dd1d04efae0**
> TornLookupResponse call_2baae03f953cd57fd5303dd1d04efae0(timestamp=timestamp, comment=comment, key=key)

Get all available torn selections

Requires public key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.torn_lookup_response import TornLookupResponse
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
    api_instance = openapi_client.TornApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get all available torn selections
        api_response = api_instance.call_2baae03f953cd57fd5303dd1d04efae0(timestamp=timestamp, comment=comment, key=key)
        print("The response of TornApi->call_2baae03f953cd57fd5303dd1d04efae0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TornApi->call_2baae03f953cd57fd5303dd1d04efae0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**TornLookupResponse**](TornLookupResponse.md)

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

# **call_2e799e84fcfa9b722f856e859df909f8**
> TornItemAmmoResponse call_2e799e84fcfa9b722f856e859df909f8(timestamp=timestamp, comment=comment, key=key)

Get information about ammo

Requires public key.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.torn_item_ammo_response import TornItemAmmoResponse
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
    api_instance = openapi_client.TornApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get information about ammo
        api_response = api_instance.call_2e799e84fcfa9b722f856e859df909f8(timestamp=timestamp, comment=comment, key=key)
        print("The response of TornApi->call_2e799e84fcfa9b722f856e859df909f8:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TornApi->call_2e799e84fcfa9b722f856e859df909f8: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**TornItemAmmoResponse**](TornItemAmmoResponse.md)

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

# **call_2f68d7e04d218e26005be3eeca6de583**
> TornLogCategoriesResponse call_2f68d7e04d218e26005be3eeca6de583(timestamp=timestamp, comment=comment, key=key)

Get available log categories

Requires public key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.torn_log_categories_response import TornLogCategoriesResponse
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
    api_instance = openapi_client.TornApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get available log categories
        api_response = api_instance.call_2f68d7e04d218e26005be3eeca6de583(timestamp=timestamp, comment=comment, key=key)
        print("The response of TornApi->call_2f68d7e04d218e26005be3eeca6de583:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TornApi->call_2f68d7e04d218e26005be3eeca6de583: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**TornLogCategoriesResponse**](TornLogCategoriesResponse.md)

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

# **call_37f1828422f3080da21f9eb4aa576686**
> TornTerritoriesResponse call_37f1828422f3080da21f9eb4aa576686(ids=ids, offset=offset, limit=limit, timestamp=timestamp, comment=comment, key=key)

Get territory details

Requires public access key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.faction_territory_enum import FactionTerritoryEnum
from openapi_client.models.torn_territories_response import TornTerritoriesResponse
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
    api_instance = openapi_client.TornApi(api_client)
    ids = [openapi_client.FactionTerritoryEnum()] # List[FactionTerritoryEnum] | Specific territory id or a list of territory ids (comma separated) (optional)
    offset = 0 # int |  (optional) (default to 0)
    limit = 20 # int |  (optional) (default to 20)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get territory details
        api_response = api_instance.call_37f1828422f3080da21f9eb4aa576686(ids=ids, offset=offset, limit=limit, timestamp=timestamp, comment=comment, key=key)
        print("The response of TornApi->call_37f1828422f3080da21f9eb4aa576686:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TornApi->call_37f1828422f3080da21f9eb4aa576686: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**List[FactionTerritoryEnum]**](FactionTerritoryEnum.md)| Specific territory id or a list of territory ids (comma separated) | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 20]
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**TornTerritoriesResponse**](TornTerritoriesResponse.md)

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

# **call_61c2d0bc6980cf8d730fe48eb81f417b**
> AttackLogResponse call_61c2d0bc6980cf8d730fe48eb81f417b(log, offset=offset, sort=sort, striptags=striptags, timestamp=timestamp, comment=comment, key=key)

Get attack log details

Requires public key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.attack_log_response import AttackLogResponse
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
    api_instance = openapi_client.TornApi(api_client)
    log = 'log_example' # str | Code of the attack log. E.g. d51ad4fe6be884b309b142e2d1d4f807
    offset = 0 # int |  (optional) (default to 0)
    sort = 'sort_example' # str | Sorted by the greatest timestamps (optional)
    striptags = true # str | Determines if fields include HTML or not ('Hospitalized by <a href=...>user</a>' vs 'Hospitalized by user'). (optional) (default to true)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get attack log details
        api_response = api_instance.call_61c2d0bc6980cf8d730fe48eb81f417b(log, offset=offset, sort=sort, striptags=striptags, timestamp=timestamp, comment=comment, key=key)
        print("The response of TornApi->call_61c2d0bc6980cf8d730fe48eb81f417b:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TornApi->call_61c2d0bc6980cf8d730fe48eb81f417b: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log** | **str**| Code of the attack log. E.g. d51ad4fe6be884b309b142e2d1d4f807 | 
 **offset** | **int**|  | [optional] [default to 0]
 **sort** | **str**| Sorted by the greatest timestamps | [optional] 
 **striptags** | **str**| Determines if fields include HTML or not (&#39;Hospitalized by &lt;a href&#x3D;...&gt;user&lt;/a&gt;&#39; vs &#39;Hospitalized by user&#39;). | [optional] [default to true]
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**AttackLogResponse**](AttackLogResponse.md)

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

# **call_6f8cffcdae9fe97110b8d46c3991f109**
> TimestampResponse call_6f8cffcdae9fe97110b8d46c3991f109(timestamp=timestamp, comment=comment, key=key)

Get current server time

Requires public key. <br>

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
    api_instance = openapi_client.TornApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get current server time
        api_response = api_instance.call_6f8cffcdae9fe97110b8d46c3991f109(timestamp=timestamp, comment=comment, key=key)
        print("The response of TornApi->call_6f8cffcdae9fe97110b8d46c3991f109:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TornApi->call_6f8cffcdae9fe97110b8d46c3991f109: %s\n" % e)
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

# **call_7be904fbcb98a7bb724f0c5b02a37a25**
> TornLogTypesResponse call_7be904fbcb98a7bb724f0c5b02a37a25(log_category_id, timestamp=timestamp, comment=comment, key=key)

Get available log ids for a specific log category

Requires public key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.torn_log_types_response import TornLogTypesResponse
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
    api_instance = openapi_client.TornApi(api_client)
    log_category_id = 56 # int | Log category id
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get available log ids for a specific log category
        api_response = api_instance.call_7be904fbcb98a7bb724f0c5b02a37a25(log_category_id, timestamp=timestamp, comment=comment, key=key)
        print("The response of TornApi->call_7be904fbcb98a7bb724f0c5b02a37a25:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TornApi->call_7be904fbcb98a7bb724f0c5b02a37a25: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_category_id** | **int**| Log category id | 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**TornLogTypesResponse**](TornLogTypesResponse.md)

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

# **call_80ad6ebd50b6c075427c04d2f54d7af5**
> TornItemModsResponse call_80ad6ebd50b6c075427c04d2f54d7af5(timestamp=timestamp, comment=comment, key=key)

Get information about weapon upgrades

Requires public key.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.torn_item_mods_response import TornItemModsResponse
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
    api_instance = openapi_client.TornApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get information about weapon upgrades
        api_response = api_instance.call_80ad6ebd50b6c075427c04d2f54d7af5(timestamp=timestamp, comment=comment, key=key)
        print("The response of TornApi->call_80ad6ebd50b6c075427c04d2f54d7af5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TornApi->call_80ad6ebd50b6c075427c04d2f54d7af5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**TornItemModsResponse**](TornItemModsResponse.md)

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

# **call_911d56b49218cef2102be3de73f82f01**
> TornHofResponse call_911d56b49218cef2102be3de73f82f01(cat, limit=limit, offset=offset, timestamp=timestamp, comment=comment, key=key)

Get player hall of fame positions for a specific category

Requires public key.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.torn_hof_category import TornHofCategory
from openapi_client.models.torn_hof_response import TornHofResponse
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
    api_instance = openapi_client.TornApi(api_client)
    cat = openapi_client.TornHofCategory() # TornHofCategory | Leaderboards category
    limit = 100 # int |  (optional) (default to 100)
    offset = 0 # int |  (optional) (default to 0)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get player hall of fame positions for a specific category
        api_response = api_instance.call_911d56b49218cef2102be3de73f82f01(cat, limit=limit, offset=offset, timestamp=timestamp, comment=comment, key=key)
        print("The response of TornApi->call_911d56b49218cef2102be3de73f82f01:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TornApi->call_911d56b49218cef2102be3de73f82f01: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cat** | [**TornHofCategory**](.md)| Leaderboards category | 
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] [default to 0]
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**TornHofResponse**](TornHofResponse.md)

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

# **call_992f8b71435ca78ba96f1e5298c25152**
> TornEducationResponse call_992f8b71435ca78ba96f1e5298c25152(timestamp=timestamp, comment=comment, key=key)

Get education information

Requires public access key.<br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.torn_education_response import TornEducationResponse
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
    api_instance = openapi_client.TornApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get education information
        api_response = api_instance.call_992f8b71435ca78ba96f1e5298c25152(timestamp=timestamp, comment=comment, key=key)
        print("The response of TornApi->call_992f8b71435ca78ba96f1e5298c25152:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TornApi->call_992f8b71435ca78ba96f1e5298c25152: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**TornEducationResponse**](TornEducationResponse.md)

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

# **d4cb87bc2502a517c49525b910a6dd82**
> TornLogTypesResponse d4cb87bc2502a517c49525b910a6dd82(timestamp=timestamp, comment=comment, key=key)

Get all available log ids

Requires public key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.torn_log_types_response import TornLogTypesResponse
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
    api_instance = openapi_client.TornApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get all available log ids
        api_response = api_instance.d4cb87bc2502a517c49525b910a6dd82(timestamp=timestamp, comment=comment, key=key)
        print("The response of TornApi->d4cb87bc2502a517c49525b910a6dd82:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TornApi->d4cb87bc2502a517c49525b910a6dd82: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**TornLogTypesResponse**](TornLogTypesResponse.md)

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

# **e95c96ef528248341647a5704630320e**
> TornCalendarResponse e95c96ef528248341647a5704630320e(timestamp=timestamp, comment=comment, key=key)

Get calendar information

Requires public access key. <br> Get the details about competitions & events in the running year.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.torn_calendar_response import TornCalendarResponse
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
    api_instance = openapi_client.TornApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get calendar information
        api_response = api_instance.e95c96ef528248341647a5704630320e(timestamp=timestamp, comment=comment, key=key)
        print("The response of TornApi->e95c96ef528248341647a5704630320e:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TornApi->e95c96ef528248341647a5704630320e: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**TornCalendarResponse**](TornCalendarResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **f45431b364546bb20b0ca909e9ac686e**
> TornFactionTreeResponse f45431b364546bb20b0ca909e9ac686e(timestamp=timestamp, comment=comment, key=key)

Get full faction tree

Requires public access key. <br> 

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.torn_faction_tree_response import TornFactionTreeResponse
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
    api_instance = openapi_client.TornApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get full faction tree
        api_response = api_instance.f45431b364546bb20b0ca909e9ac686e(timestamp=timestamp, comment=comment, key=key)
        print("The response of TornApi->f45431b364546bb20b0ca909e9ac686e:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TornApi->f45431b364546bb20b0ca909e9ac686e: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**TornFactionTreeResponse**](TornFactionTreeResponse.md)

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

