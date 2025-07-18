# openapi_client.RacingApi

All URIs are relative to *https://api.torn.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ab5b44b00bf70d7a8587a3c2c9deeb17**](RacingApi.md#ab5b44b00bf70d7a8587a3c2c9deeb17) | **GET** /racing/cars | Get cars and their racing stats
[**c9e76cf48aa3c4bac4c8b33f1c0c9a17**](RacingApi.md#c9e76cf48aa3c4bac4c8b33f1c0c9a17) | **GET** /racing/carupgrades | Get all possible car upgrades
[**call_39b8ce36e3fffc9e2aa1d0aed9ebccda**](RacingApi.md#call_39b8ce36e3fffc9e2aa1d0aed9ebccda) | **GET** /racing | Get any Racing selection
[**call_4be921a67d32b5e82c68835ef56175d0**](RacingApi.md#call_4be921a67d32b5e82c68835ef56175d0) | **GET** /racing/races | Get races
[**call_5fbc62db3b9380b155d7e33100620da7**](RacingApi.md#call_5fbc62db3b9380b155d7e33100620da7) | **GET** /racing/{trackId}/records | Get track records
[**call_6e4507cc442d6f099d0170b78a35bf8d**](RacingApi.md#call_6e4507cc442d6f099d0170b78a35bf8d) | **GET** /racing/tracks | Get race tracks and descriptions
[**call_76925256951bb63fd28534c8c479b27b**](RacingApi.md#call_76925256951bb63fd28534c8c479b27b) | **GET** /racing/{raceId}/race | Get specific race details
[**call_8bd16be9aa517fedf717c9a79ff47e2c**](RacingApi.md#call_8bd16be9aa517fedf717c9a79ff47e2c) | **GET** /racing/lookup | Get all available racing selections
[**eb1ae216aa2949a8db0702df474d174c**](RacingApi.md#eb1ae216aa2949a8db0702df474d174c) | **GET** /racing/timestamp | Get current server time


# **ab5b44b00bf70d7a8587a3c2c9deeb17**
> RacingCarsResponse ab5b44b00bf70d7a8587a3c2c9deeb17(timestamp=timestamp, comment=comment, key=key)

Get cars and their racing stats

Requires public access key. <br>Returns the stat details about racing cars.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.racing_cars_response import RacingCarsResponse
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
    api_instance = openapi_client.RacingApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get cars and their racing stats
        api_response = api_instance.ab5b44b00bf70d7a8587a3c2c9deeb17(timestamp=timestamp, comment=comment, key=key)
        print("The response of RacingApi->ab5b44b00bf70d7a8587a3c2c9deeb17:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RacingApi->ab5b44b00bf70d7a8587a3c2c9deeb17: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**RacingCarsResponse**](RacingCarsResponse.md)

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

# **c9e76cf48aa3c4bac4c8b33f1c0c9a17**
> RacingCarUpgradesResponse c9e76cf48aa3c4bac4c8b33f1c0c9a17(timestamp=timestamp, comment=comment, key=key)

Get all possible car upgrades

Requires public access key. <br>Returns the details about all possible car upgrades.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.racing_car_upgrades_response import RacingCarUpgradesResponse
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
    api_instance = openapi_client.RacingApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get all possible car upgrades
        api_response = api_instance.c9e76cf48aa3c4bac4c8b33f1c0c9a17(timestamp=timestamp, comment=comment, key=key)
        print("The response of RacingApi->c9e76cf48aa3c4bac4c8b33f1c0c9a17:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RacingApi->c9e76cf48aa3c4bac4c8b33f1c0c9a17: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**RacingCarUpgradesResponse**](RacingCarUpgradesResponse.md)

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

# **call_39b8ce36e3fffc9e2aa1d0aed9ebccda**
> Model39b8ce36e3fffc9e2aa1d0aed9ebccda200Response call_39b8ce36e3fffc9e2aa1d0aed9ebccda(selections=selections, id=id, limit=limit, sort=sort, to=to, var_from=var_from, cat=cat, offset=offset, timestamp=timestamp, comment=comment, key=key)

Get any Racing selection

Requires public access key. <br>Choose one or more selections (comma separated).

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.model39b8ce36e3fffc9e2aa1d0aed9ebccda200_response import Model39b8ce36e3fffc9e2aa1d0aed9ebccda200Response
from openapi_client.models.racing_selection_name import RacingSelectionName
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
    api_instance = openapi_client.RacingApi(api_client)
    selections = [openapi_client.RacingSelectionName()] # List[RacingSelectionName] | Selection names (optional)
    id = openapi_client.Model39b8ce36e3fffc9e2aa1d0aed9ebccdaIdParameter() # Model39b8ce36e3fffc9e2aa1d0aed9ebccdaIdParameter | selection id (optional)
    limit = 56 # int |  (optional)
    sort = 'sort_example' # str | Sorted by the greatest timestamps (optional)
    to = 56 # int | Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time (optional)
    var_from = 56 # int | Timestamp that sets the lower limit for the data returned. Data returned will be after this time (optional)
    cat = openapi_client.Model39b8ce36e3fffc9e2aa1d0aed9ebccdaCatParameter() # Model39b8ce36e3fffc9e2aa1d0aed9ebccdaCatParameter | Selection category (optional)
    offset = 56 # int |  (optional)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get any Racing selection
        api_response = api_instance.call_39b8ce36e3fffc9e2aa1d0aed9ebccda(selections=selections, id=id, limit=limit, sort=sort, to=to, var_from=var_from, cat=cat, offset=offset, timestamp=timestamp, comment=comment, key=key)
        print("The response of RacingApi->call_39b8ce36e3fffc9e2aa1d0aed9ebccda:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RacingApi->call_39b8ce36e3fffc9e2aa1d0aed9ebccda: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **selections** | [**List[RacingSelectionName]**](RacingSelectionName.md)| Selection names | [optional] 
 **id** | [**Model39b8ce36e3fffc9e2aa1d0aed9ebccdaIdParameter**](.md)| selection id | [optional] 
 **limit** | **int**|  | [optional] 
 **sort** | **str**| Sorted by the greatest timestamps | [optional] 
 **to** | **int**| Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time | [optional] 
 **var_from** | **int**| Timestamp that sets the lower limit for the data returned. Data returned will be after this time | [optional] 
 **cat** | [**Model39b8ce36e3fffc9e2aa1d0aed9ebccdaCatParameter**](.md)| Selection category | [optional] 
 **offset** | **int**|  | [optional] 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**Model39b8ce36e3fffc9e2aa1d0aed9ebccda200Response**](Model39b8ce36e3fffc9e2aa1d0aed9ebccda200Response.md)

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

# **call_4be921a67d32b5e82c68835ef56175d0**
> RacingRacesResponse call_4be921a67d32b5e82c68835ef56175d0(limit=limit, sort=sort, to=to, var_from=var_from, cat=cat, timestamp=timestamp, comment=comment, key=key)

Get races

Requires public access key. <br>Returns a list of races, ordered by race start timestamp.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.racing_race_type_enum import RacingRaceTypeEnum
from openapi_client.models.racing_races_response import RacingRacesResponse
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
    api_instance = openapi_client.RacingApi(api_client)
    limit = 100 # int |  (optional) (default to 100)
    sort = DESC # str | Sorted by the greatest timestamps (optional) (default to DESC)
    to = 56 # int | Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time (optional)
    var_from = 56 # int | Timestamp that sets the lower limit for the data returned. Data returned will be after this time (optional)
    cat = openapi_client.RacingRaceTypeEnum() # RacingRaceTypeEnum | Category of races returned (optional)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get races
        api_response = api_instance.call_4be921a67d32b5e82c68835ef56175d0(limit=limit, sort=sort, to=to, var_from=var_from, cat=cat, timestamp=timestamp, comment=comment, key=key)
        print("The response of RacingApi->call_4be921a67d32b5e82c68835ef56175d0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RacingApi->call_4be921a67d32b5e82c68835ef56175d0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 100]
 **sort** | **str**| Sorted by the greatest timestamps | [optional] [default to DESC]
 **to** | **int**| Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time | [optional] 
 **var_from** | **int**| Timestamp that sets the lower limit for the data returned. Data returned will be after this time | [optional] 
 **cat** | [**RacingRaceTypeEnum**](.md)| Category of races returned | [optional] 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**RacingRacesResponse**](RacingRacesResponse.md)

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

# **call_5fbc62db3b9380b155d7e33100620da7**
> RacingTrackRecordsResponse call_5fbc62db3b9380b155d7e33100620da7(track_id, cat, timestamp=timestamp, comment=comment, key=key)

Get track records

Requires public access key. <br>Returns a list of 5 best lap records for the chosen track and car class.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.race_class_enum import RaceClassEnum
from openapi_client.models.racing_track_records_response import RacingTrackRecordsResponse
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
    api_instance = openapi_client.RacingApi(api_client)
    track_id = 56 # int | Track id
    cat = openapi_client.RaceClassEnum() # RaceClassEnum | Car class
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get track records
        api_response = api_instance.call_5fbc62db3b9380b155d7e33100620da7(track_id, cat, timestamp=timestamp, comment=comment, key=key)
        print("The response of RacingApi->call_5fbc62db3b9380b155d7e33100620da7:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RacingApi->call_5fbc62db3b9380b155d7e33100620da7: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **track_id** | **int**| Track id | 
 **cat** | [**RaceClassEnum**](.md)| Car class | 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**RacingTrackRecordsResponse**](RacingTrackRecordsResponse.md)

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

# **call_6e4507cc442d6f099d0170b78a35bf8d**
> RacingTracksResponse call_6e4507cc442d6f099d0170b78a35bf8d(timestamp=timestamp, comment=comment, key=key)

Get race tracks and descriptions

Requires public access key. <br>Returns the details about racing tracks.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.racing_tracks_response import RacingTracksResponse
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
    api_instance = openapi_client.RacingApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get race tracks and descriptions
        api_response = api_instance.call_6e4507cc442d6f099d0170b78a35bf8d(timestamp=timestamp, comment=comment, key=key)
        print("The response of RacingApi->call_6e4507cc442d6f099d0170b78a35bf8d:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RacingApi->call_6e4507cc442d6f099d0170b78a35bf8d: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**RacingTracksResponse**](RacingTracksResponse.md)

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

# **call_76925256951bb63fd28534c8c479b27b**
> RacingRaceDetailsResponse call_76925256951bb63fd28534c8c479b27b(race_id, timestamp=timestamp, comment=comment, key=key)

Get specific race details

Requires public access key. <br>Returns the details of a race.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.racing_race_details_response import RacingRaceDetailsResponse
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
    api_instance = openapi_client.RacingApi(api_client)
    race_id = 56 # int | Race id
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get specific race details
        api_response = api_instance.call_76925256951bb63fd28534c8c479b27b(race_id, timestamp=timestamp, comment=comment, key=key)
        print("The response of RacingApi->call_76925256951bb63fd28534c8c479b27b:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RacingApi->call_76925256951bb63fd28534c8c479b27b: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **race_id** | **int**| Race id | 
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**RacingRaceDetailsResponse**](RacingRaceDetailsResponse.md)

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

# **call_8bd16be9aa517fedf717c9a79ff47e2c**
> RacingLookupResponse call_8bd16be9aa517fedf717c9a79ff47e2c(timestamp=timestamp, comment=comment, key=key)

Get all available racing selections

Requires public access key. <br>

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.racing_lookup_response import RacingLookupResponse
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
    api_instance = openapi_client.RacingApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get all available racing selections
        api_response = api_instance.call_8bd16be9aa517fedf717c9a79ff47e2c(timestamp=timestamp, comment=comment, key=key)
        print("The response of RacingApi->call_8bd16be9aa517fedf717c9a79ff47e2c:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RacingApi->call_8bd16be9aa517fedf717c9a79ff47e2c: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp to bypass cache | [optional] 
 **comment** | **str**| Comment for your tool/service/bot/website to be visible in the logs. | [optional] 
 **key** | **str**| API key (Public).&lt;br&gt;It&#39;s not required to use this parameter when passing the API key via the Authorization header. | [optional] 

### Return type

[**RacingLookupResponse**](RacingLookupResponse.md)

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

# **eb1ae216aa2949a8db0702df474d174c**
> TimestampResponse eb1ae216aa2949a8db0702df474d174c(timestamp=timestamp, comment=comment, key=key)

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
    api_instance = openapi_client.RacingApi(api_client)
    timestamp = 'timestamp_example' # str | Timestamp to bypass cache (optional)
    comment = 'comment_example' # str | Comment for your tool/service/bot/website to be visible in the logs. (optional)
    key = 'key_example' # str | API key (Public).<br>It's not required to use this parameter when passing the API key via the Authorization header. (optional)

    try:
        # Get current server time
        api_response = api_instance.eb1ae216aa2949a8db0702df474d174c(timestamp=timestamp, comment=comment, key=key)
        print("The response of RacingApi->eb1ae216aa2949a8db0702df474d174c:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RacingApi->eb1ae216aa2949a8db0702df474d174c: %s\n" % e)
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

