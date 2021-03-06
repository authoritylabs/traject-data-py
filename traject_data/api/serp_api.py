"""
    Traject Data • SERP Data API

    Traject Data • trajectdata.com • SERP Data API • SERP Data API for Scale | Locale SEO | Agencies | Brands  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Contact: support@trajectdata.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from traject_data.api_client import ApiClient, Endpoint as _Endpoint
from traject_data.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from traject_data.model.error import Error
from traject_data.model.post_keyword_result import PostKeywordResult


class SerpApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_engine_locale(
            self,
            engine="google",
            locale="en-us",
            **kwargs
        ):
            """Locale details for a given engine  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_engine_locale(engine="google", locale="en-us", async_req=True)
            >>> result = thread.get()

            Args:
                engine (str): Engine (baidu | bing | gmaps | google | yahoo | yandex). defaults to "google", must be one of ["google"]
                locale (str): Locale such as en-us. defaults to "en-us", must be one of ["en-us"]

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['engine'] = \
                engine
            kwargs['locale'] = \
                locale
            return self.call_with_http_info(**kwargs)

        self.get_engine_locale = _Endpoint(
            settings={
                'response_type': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                'auth': [
                    'ApiKeyAuth'
                ],
                'endpoint_path': '/supported/{engine}/{locale}.json',
                'operation_id': 'get_engine_locale',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'engine',
                    'locale',
                ],
                'required': [
                    'engine',
                    'locale',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'engine':
                        (str,),
                    'locale':
                        (str,),
                },
                'attribute_map': {
                    'engine': 'engine',
                    'locale': 'locale',
                },
                'location_map': {
                    'engine': 'path',
                    'locale': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_engine_locale
        )

        def __get_locales(
            self,
            engine="google",
            **kwargs
        ):
            """Fetch supported locales for a given engine  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_locales(engine="google", async_req=True)
            >>> result = thread.get()

            Args:
                engine (str): Engine (baidu | bing | gmaps | google | yahoo | yandex) to display supported locales for. defaults to "google", must be one of ["google"]

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['engine'] = \
                engine
            return self.call_with_http_info(**kwargs)

        self.get_locales = _Endpoint(
            settings={
                'response_type': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                'auth': [
                    'ApiKeyAuth'
                ],
                'endpoint_path': '/supported/{engine}.json',
                'operation_id': 'get_locales',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'engine',
                ],
                'required': [
                    'engine',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'engine':
                        (str,),
                },
                'attribute_map': {
                    'engine': 'engine',
                },
                'location_map': {
                    'engine': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_locales
        )

        def __get_serp(
            self,
            json_id,
            **kwargs
        ):
            """Fetches SERP json  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_serp(json_id, async_req=True)
            >>> result = thread.get()

            Args:
                json_id (str): Json identifier (received via webhook)

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['json_id'] = \
                json_id
            return self.call_with_http_info(**kwargs)

        self.get_serp = _Endpoint(
            settings={
                'response_type': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                'auth': [
                    'ApiKeyAuth'
                ],
                'endpoint_path': '/keywords/get.json',
                'operation_id': 'get_serp',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'json_id',
                ],
                'required': [
                    'json_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'json_id':
                        (str,),
                },
                'attribute_map': {
                    'json_id': 'json_id',
                },
                'location_map': {
                    'json_id': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'text/html'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_serp
        )

        def __get_serp_html(
            self,
            html_id,
            data_format="HTML",
            **kwargs
        ):
            """Fetches SERP html  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_serp_html(html_id, data_format="HTML", async_req=True)
            >>> result = thread.get()

            Args:
                html_id (str): Html identifier (received via webhook)
                data_format (str): Specify HTML format. defaults to "HTML", must be one of ["HTML"]

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                str
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['html_id'] = \
                html_id
            kwargs['data_format'] = \
                data_format
            return self.call_with_http_info(**kwargs)

        self.get_serp_html = _Endpoint(
            settings={
                'response_type': (str,),
                'auth': [
                    'ApiKeyAuth'
                ],
                'endpoint_path': '/keywords/get.html',
                'operation_id': 'get_serp_html',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'html_id',
                    'data_format',
                ],
                'required': [
                    'html_id',
                    'data_format',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'html_id':
                        (str,),
                    'data_format':
                        (str,),
                },
                'attribute_map': {
                    'html_id': 'html_id',
                    'data_format': 'data_format',
                },
                'location_map': {
                    'html_id': 'query',
                    'data_format': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/html',
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_serp_html
        )

        def __post_keyword(
            self,
            keyword,
            **kwargs
        ):
            """Create keyword search  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.post_keyword(keyword, async_req=True)
            >>> result = thread.get()

            Args:
                keyword (str): keywords to search by

            Keyword Args:
                locale (str): locale. [optional] if omitted the server will use the default value of "en-us"
                geo (str): geographical location. [optional]
                engine (str): Search engine. [optional] if omitted the server will use the default value of "google"
                mobile (bool): Mobile if true, desktop if false. [optional] if omitted the server will use the default value of False
                param_callback (str): webhook url to be notified with search result (not required if configured for your account level). [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                PostKeywordResult
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['keyword'] = \
                keyword
            return self.call_with_http_info(**kwargs)

        self.post_keyword = _Endpoint(
            settings={
                'response_type': (PostKeywordResult,),
                'auth': [
                    'ApiKeyAuth'
                ],
                'endpoint_path': '/keywords',
                'operation_id': 'post_keyword',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'keyword',
                    'locale',
                    'geo',
                    'engine',
                    'mobile',
                    'param_callback',
                ],
                'required': [
                    'keyword',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'keyword':
                        (str,),
                    'locale':
                        (str,),
                    'geo':
                        (str,),
                    'engine':
                        (str,),
                    'mobile':
                        (bool,),
                    'param_callback':
                        (str,),
                },
                'attribute_map': {
                    'keyword': 'keyword',
                    'locale': 'locale',
                    'geo': 'geo',
                    'engine': 'engine',
                    'mobile': 'mobile',
                    'param_callback': 'callback',
                },
                'location_map': {
                    'keyword': 'query',
                    'locale': 'query',
                    'geo': 'query',
                    'engine': 'query',
                    'mobile': 'query',
                    'param_callback': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'text/html'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__post_keyword
        )

        def __post_keyword_priority(
            self,
            keyword,
            **kwargs
        ):
            """Priority create keyword search  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.post_keyword_priority(keyword, async_req=True)
            >>> result = thread.get()

            Args:
                keyword (str): keywords to search by

            Keyword Args:
                locale (str): locale. [optional] if omitted the server will use the default value of "en-us"
                geo (str): geographical location. [optional]
                engine (str): Search engine. [optional] if omitted the server will use the default value of "google"
                mobile (bool): Mobile if true, desktop if false. [optional] if omitted the server will use the default value of False
                param_callback (str): webhook url to be notified with search result (not required if configured for your account level). [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                PostKeywordResult
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['keyword'] = \
                keyword
            return self.call_with_http_info(**kwargs)

        self.post_keyword_priority = _Endpoint(
            settings={
                'response_type': (PostKeywordResult,),
                'auth': [
                    'ApiKeyAuth'
                ],
                'endpoint_path': '/keywords/priority',
                'operation_id': 'post_keyword_priority',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'keyword',
                    'locale',
                    'geo',
                    'engine',
                    'mobile',
                    'param_callback',
                ],
                'required': [
                    'keyword',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'keyword':
                        (str,),
                    'locale':
                        (str,),
                    'geo':
                        (str,),
                    'engine':
                        (str,),
                    'mobile':
                        (bool,),
                    'param_callback':
                        (str,),
                },
                'attribute_map': {
                    'keyword': 'keyword',
                    'locale': 'locale',
                    'geo': 'geo',
                    'engine': 'engine',
                    'mobile': 'mobile',
                    'param_callback': 'callback',
                },
                'location_map': {
                    'keyword': 'query',
                    'locale': 'query',
                    'geo': 'query',
                    'engine': 'query',
                    'mobile': 'query',
                    'param_callback': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'text/html'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__post_keyword_priority
        )
