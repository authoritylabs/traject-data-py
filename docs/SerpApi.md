# traject_data.SerpApi

All URIs are relative to *https://api.trajectdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_engine_locale**](SerpApi.md#get_engine_locale) | **GET** /supported/{engine}/{locale}.json | Locale details for a given engine
[**get_locales**](SerpApi.md#get_locales) | **GET** /supported/{engine}.json | Fetch supported locales for a given engine
[**get_serp**](SerpApi.md#get_serp) | **GET** /keywords/get.json | Fetches SERP json
[**get_serp_html**](SerpApi.md#get_serp_html) | **GET** /keywords/get.html | Fetches SERP html
[**post_keyword**](SerpApi.md#post_keyword) | **POST** /keywords | Create keyword search
[**post_keyword_priority**](SerpApi.md#post_keyword_priority) | **POST** /keywords/priority | Priority create keyword search


# **get_engine_locale**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_engine_locale()

Locale details for a given engine

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import traject_data
from traject_data.api import serp_api
from traject_data.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.trajectdata.com
# See configuration.py for a list of all supported configuration parameters.
configuration = traject_data.Configuration(
    host = "https://api.trajectdata.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with traject_data.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = serp_api.SerpApi(api_client)

    # example passing only required values which don't have defaults set
    try:
        # Locale details for a given engine
        api_response = api_instance.get_engine_locale()
        pprint(api_response)
    except traject_data.ApiException as e:
        print("Exception when calling SerpApi->get_engine_locale: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine** | **str**| Engine (baidu | bing | gmaps | google | yahoo | yandex) | defaults to "google"
 **locale** | **str**| Locale such as en-us | defaults to "en-us"

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Locale details result |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_locales**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_locales()

Fetch supported locales for a given engine

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import traject_data
from traject_data.api import serp_api
from traject_data.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.trajectdata.com
# See configuration.py for a list of all supported configuration parameters.
configuration = traject_data.Configuration(
    host = "https://api.trajectdata.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with traject_data.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = serp_api.SerpApi(api_client)

    # example passing only required values which don't have defaults set
    try:
        # Fetch supported locales for a given engine
        api_response = api_instance.get_locales()
        pprint(api_response)
    except traject_data.ApiException as e:
        print("Exception when calling SerpApi->get_locales: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine** | **str**| Engine (baidu | bing | gmaps | google | yahoo | yandex) to display supported locales for | defaults to "google"

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Supported locales result |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_serp**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_serp(json_id)

Fetches SERP json

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import traject_data
from traject_data.api import serp_api
from traject_data.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.trajectdata.com
# See configuration.py for a list of all supported configuration parameters.
configuration = traject_data.Configuration(
    host = "https://api.trajectdata.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with traject_data.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = serp_api.SerpApi(api_client)
    json_id = "json_id_example" # str | Json identifier (received via webhook)

    # example passing only required values which don't have defaults set
    try:
        # Fetches SERP json
        api_response = api_instance.get_serp(json_id)
        pprint(api_response)
    except traject_data.ApiException as e:
        print("Exception when calling SerpApi->get_serp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_id** | **str**| Json identifier (received via webhook) |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SERP result |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_serp_html**
> str get_serp_html(html_id, )

Fetches SERP html

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import traject_data
from traject_data.api import serp_api
from traject_data.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.trajectdata.com
# See configuration.py for a list of all supported configuration parameters.
configuration = traject_data.Configuration(
    host = "https://api.trajectdata.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with traject_data.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = serp_api.SerpApi(api_client)
    html_id = "html_id_example" # str | Html identifier (received via webhook)

    # example passing only required values which don't have defaults set
    try:
        # Fetches SERP html
        api_response = api_instance.get_serp_html(html_id, )
        pprint(api_response)
    except traject_data.ApiException as e:
        print("Exception when calling SerpApi->get_serp_html: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **html_id** | **str**| Html identifier (received via webhook) |
 **data_format** | **str**| Specify HTML format | defaults to "HTML"

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SERP result html |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_keyword**
> PostKeywordResult post_keyword(keyword)

Create keyword search

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import traject_data
from traject_data.api import serp_api
from traject_data.model.post_keyword_result import PostKeywordResult
from traject_data.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.trajectdata.com
# See configuration.py for a list of all supported configuration parameters.
configuration = traject_data.Configuration(
    host = "https://api.trajectdata.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with traject_data.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = serp_api.SerpApi(api_client)
    keyword = "keyword_example" # str | keywords to search by
    locale = "en-us" # str | locale (optional) if omitted the server will use the default value of "en-us"
    geo = "Seattle, WA" # str | geographical location (optional)
    engine = "google" # str | Search engine (optional) if omitted the server will use the default value of "google"
    mobile = False # bool | Mobile if true, desktop if false (optional) if omitted the server will use the default value of False
    param_callback = "callback_example" # str | webhook url to be notified with search result (not required if configured for your account level) (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create keyword search
        api_response = api_instance.post_keyword(keyword)
        pprint(api_response)
    except traject_data.ApiException as e:
        print("Exception when calling SerpApi->post_keyword: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create keyword search
        api_response = api_instance.post_keyword(keyword, locale=locale, geo=geo, engine=engine, mobile=mobile, param_callback=param_callback)
        pprint(api_response)
    except traject_data.ApiException as e:
        print("Exception when calling SerpApi->post_keyword: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyword** | **str**| keywords to search by |
 **locale** | **str**| locale | [optional] if omitted the server will use the default value of "en-us"
 **geo** | **str**| geographical location | [optional]
 **engine** | **str**| Search engine | [optional] if omitted the server will use the default value of "google"
 **mobile** | **bool**| Mobile if true, desktop if false | [optional] if omitted the server will use the default value of False
 **param_callback** | **str**| webhook url to be notified with search result (not required if configured for your account level) | [optional]

### Return type

[**PostKeywordResult**](PostKeywordResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Post keyword result |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_keyword_priority**
> PostKeywordResult post_keyword_priority(keyword)

Priority create keyword search

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import traject_data
from traject_data.api import serp_api
from traject_data.model.post_keyword_result import PostKeywordResult
from traject_data.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.trajectdata.com
# See configuration.py for a list of all supported configuration parameters.
configuration = traject_data.Configuration(
    host = "https://api.trajectdata.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with traject_data.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = serp_api.SerpApi(api_client)
    keyword = "keyword_example" # str | keywords to search by
    locale = "en-us" # str | locale (optional) if omitted the server will use the default value of "en-us"
    geo = "seattle, wa" # str | geographical location (optional)
    engine = "google" # str | Search engine (optional) if omitted the server will use the default value of "google"
    mobile = False # bool | Mobile if true, desktop if false (optional) if omitted the server will use the default value of False
    param_callback = "callback_example" # str | webhook url to be notified with search result (not required if configured for your account level) (optional)

    # example passing only required values which don't have defaults set
    try:
        # Priority create keyword search
        api_response = api_instance.post_keyword_priority(keyword)
        pprint(api_response)
    except traject_data.ApiException as e:
        print("Exception when calling SerpApi->post_keyword_priority: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Priority create keyword search
        api_response = api_instance.post_keyword_priority(keyword, locale=locale, geo=geo, engine=engine, mobile=mobile, param_callback=param_callback)
        pprint(api_response)
    except traject_data.ApiException as e:
        print("Exception when calling SerpApi->post_keyword_priority: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyword** | **str**| keywords to search by |
 **locale** | **str**| locale | [optional] if omitted the server will use the default value of "en-us"
 **geo** | **str**| geographical location | [optional]
 **engine** | **str**| Search engine | [optional] if omitted the server will use the default value of "google"
 **mobile** | **bool**| Mobile if true, desktop if false | [optional] if omitted the server will use the default value of False
 **param_callback** | **str**| webhook url to be notified with search result (not required if configured for your account level) | [optional]

### Return type

[**PostKeywordResult**](PostKeywordResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Post keyword result |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

