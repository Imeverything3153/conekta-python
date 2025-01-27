# coding: utf-8

"""
    Conekta API

    Conekta sdk  # noqa: E501

    The version of the OpenAPI document: 2.1.0
    Contact: engineering@conekta.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import Field, StrictStr

from typing import Optional

from conekta.models.shipping_order_response import ShippingOrderResponse
from conekta.models.shipping_request import ShippingRequest

from conekta.api_client import ApiClient
from conekta.api_response import ApiResponse
from conekta.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ShippingsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def orders_create_shipping(self, id : Annotated[StrictStr, Field(..., description="Identifier of the resource")], shipping_request : Annotated[ShippingRequest, Field(..., description="requested field for a shipping")], accept_language : Annotated[Optional[StrictStr], Field(description="Use for knowing which language to use")] = None, x_child_company_id : Annotated[Optional[StrictStr], Field(description="In the case of a holding company, the company id of the child company to which will process the request.")] = None, **kwargs) -> ShippingOrderResponse:  # noqa: E501
        """Create Shipping  # noqa: E501

        Create new shipping for an existing orden  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.orders_create_shipping(id, shipping_request, accept_language, x_child_company_id, async_req=True)
        >>> result = thread.get()

        :param id: Identifier of the resource (required)
        :type id: str
        :param shipping_request: requested field for a shipping (required)
        :type shipping_request: ShippingRequest
        :param accept_language: Use for knowing which language to use
        :type accept_language: str
        :param x_child_company_id: In the case of a holding company, the company id of the child company to which will process the request.
        :type x_child_company_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ShippingOrderResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the orders_create_shipping_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.orders_create_shipping_with_http_info(id, shipping_request, accept_language, x_child_company_id, **kwargs)  # noqa: E501

    @validate_arguments
    def orders_create_shipping_with_http_info(self, id : Annotated[StrictStr, Field(..., description="Identifier of the resource")], shipping_request : Annotated[ShippingRequest, Field(..., description="requested field for a shipping")], accept_language : Annotated[Optional[StrictStr], Field(description="Use for knowing which language to use")] = None, x_child_company_id : Annotated[Optional[StrictStr], Field(description="In the case of a holding company, the company id of the child company to which will process the request.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Create Shipping  # noqa: E501

        Create new shipping for an existing orden  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.orders_create_shipping_with_http_info(id, shipping_request, accept_language, x_child_company_id, async_req=True)
        >>> result = thread.get()

        :param id: Identifier of the resource (required)
        :type id: str
        :param shipping_request: requested field for a shipping (required)
        :type shipping_request: ShippingRequest
        :param accept_language: Use for knowing which language to use
        :type accept_language: str
        :param x_child_company_id: In the case of a holding company, the company id of the child company to which will process the request.
        :type x_child_company_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ShippingOrderResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'id',
            'shipping_request',
            'accept_language',
            'x_child_company_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method orders_create_shipping" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['accept_language']:
            _header_params['Accept-Language'] = _params['accept_language']

        if _params['x_child_company_id']:
            _header_params['X-Child-Company-Id'] = _params['x_child_company_id']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['shipping_request'] is not None:
            _body_params = _params['shipping_request']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.conekta-v2.1.0+json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['bearerAuth']  # noqa: E501

        _response_types_map = {
            '200': "ShippingOrderResponse",
            '401': "Error",
            '404': "Error",
            '500': "Error",
        }

        return self.api_client.call_api(
            '/orders/{id}/shipping_lines', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def orders_delete_shipping(self, id : Annotated[StrictStr, Field(..., description="Identifier of the resource")], shipping_id : Annotated[StrictStr, Field(..., description="identifier")], accept_language : Annotated[Optional[StrictStr], Field(description="Use for knowing which language to use")] = None, x_child_company_id : Annotated[Optional[StrictStr], Field(description="In the case of a holding company, the company id of the child company to which will process the request.")] = None, **kwargs) -> ShippingOrderResponse:  # noqa: E501
        """Delete Shipping  # noqa: E501

        Delete shipping  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.orders_delete_shipping(id, shipping_id, accept_language, x_child_company_id, async_req=True)
        >>> result = thread.get()

        :param id: Identifier of the resource (required)
        :type id: str
        :param shipping_id: identifier (required)
        :type shipping_id: str
        :param accept_language: Use for knowing which language to use
        :type accept_language: str
        :param x_child_company_id: In the case of a holding company, the company id of the child company to which will process the request.
        :type x_child_company_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ShippingOrderResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the orders_delete_shipping_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.orders_delete_shipping_with_http_info(id, shipping_id, accept_language, x_child_company_id, **kwargs)  # noqa: E501

    @validate_arguments
    def orders_delete_shipping_with_http_info(self, id : Annotated[StrictStr, Field(..., description="Identifier of the resource")], shipping_id : Annotated[StrictStr, Field(..., description="identifier")], accept_language : Annotated[Optional[StrictStr], Field(description="Use for knowing which language to use")] = None, x_child_company_id : Annotated[Optional[StrictStr], Field(description="In the case of a holding company, the company id of the child company to which will process the request.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Delete Shipping  # noqa: E501

        Delete shipping  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.orders_delete_shipping_with_http_info(id, shipping_id, accept_language, x_child_company_id, async_req=True)
        >>> result = thread.get()

        :param id: Identifier of the resource (required)
        :type id: str
        :param shipping_id: identifier (required)
        :type shipping_id: str
        :param accept_language: Use for knowing which language to use
        :type accept_language: str
        :param x_child_company_id: In the case of a holding company, the company id of the child company to which will process the request.
        :type x_child_company_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ShippingOrderResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'id',
            'shipping_id',
            'accept_language',
            'x_child_company_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method orders_delete_shipping" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']

        if _params['shipping_id']:
            _path_params['shipping_id'] = _params['shipping_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['accept_language']:
            _header_params['Accept-Language'] = _params['accept_language']

        if _params['x_child_company_id']:
            _header_params['X-Child-Company-Id'] = _params['x_child_company_id']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.conekta-v2.1.0+json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['bearerAuth']  # noqa: E501

        _response_types_map = {
            '200': "ShippingOrderResponse",
            '401': "Error",
            '404': "Error",
            '422': "Error",
            '500': "Error",
        }

        return self.api_client.call_api(
            '/orders/{id}/shipping_lines/{shipping_id}', 'DELETE',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def orders_update_shipping(self, id : Annotated[StrictStr, Field(..., description="Identifier of the resource")], shipping_id : Annotated[StrictStr, Field(..., description="identifier")], shipping_request : Annotated[ShippingRequest, Field(..., description="requested field for a shipping")], accept_language : Annotated[Optional[StrictStr], Field(description="Use for knowing which language to use")] = None, x_child_company_id : Annotated[Optional[StrictStr], Field(description="In the case of a holding company, the company id of the child company to which will process the request.")] = None, **kwargs) -> ShippingOrderResponse:  # noqa: E501
        """Update Shipping  # noqa: E501

        Update existing shipping for an existing orden  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.orders_update_shipping(id, shipping_id, shipping_request, accept_language, x_child_company_id, async_req=True)
        >>> result = thread.get()

        :param id: Identifier of the resource (required)
        :type id: str
        :param shipping_id: identifier (required)
        :type shipping_id: str
        :param shipping_request: requested field for a shipping (required)
        :type shipping_request: ShippingRequest
        :param accept_language: Use for knowing which language to use
        :type accept_language: str
        :param x_child_company_id: In the case of a holding company, the company id of the child company to which will process the request.
        :type x_child_company_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ShippingOrderResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the orders_update_shipping_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.orders_update_shipping_with_http_info(id, shipping_id, shipping_request, accept_language, x_child_company_id, **kwargs)  # noqa: E501

    @validate_arguments
    def orders_update_shipping_with_http_info(self, id : Annotated[StrictStr, Field(..., description="Identifier of the resource")], shipping_id : Annotated[StrictStr, Field(..., description="identifier")], shipping_request : Annotated[ShippingRequest, Field(..., description="requested field for a shipping")], accept_language : Annotated[Optional[StrictStr], Field(description="Use for knowing which language to use")] = None, x_child_company_id : Annotated[Optional[StrictStr], Field(description="In the case of a holding company, the company id of the child company to which will process the request.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Update Shipping  # noqa: E501

        Update existing shipping for an existing orden  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.orders_update_shipping_with_http_info(id, shipping_id, shipping_request, accept_language, x_child_company_id, async_req=True)
        >>> result = thread.get()

        :param id: Identifier of the resource (required)
        :type id: str
        :param shipping_id: identifier (required)
        :type shipping_id: str
        :param shipping_request: requested field for a shipping (required)
        :type shipping_request: ShippingRequest
        :param accept_language: Use for knowing which language to use
        :type accept_language: str
        :param x_child_company_id: In the case of a holding company, the company id of the child company to which will process the request.
        :type x_child_company_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ShippingOrderResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'id',
            'shipping_id',
            'shipping_request',
            'accept_language',
            'x_child_company_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method orders_update_shipping" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']

        if _params['shipping_id']:
            _path_params['shipping_id'] = _params['shipping_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['accept_language']:
            _header_params['Accept-Language'] = _params['accept_language']

        if _params['x_child_company_id']:
            _header_params['X-Child-Company-Id'] = _params['x_child_company_id']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['shipping_request'] is not None:
            _body_params = _params['shipping_request']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.conekta-v2.1.0+json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['bearerAuth']  # noqa: E501

        _response_types_map = {
            '200': "ShippingOrderResponse",
            '401': "Error",
            '404': "Error",
            '422': "Error",
            '500': "Error",
        }

        return self.api_client.call_api(
            '/orders/{id}/shipping_lines/{shipping_id}', 'PUT',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
