# coding: utf-8

"""
    Conekta API

    Conekta sdk  # noqa: E501

    The version of the OpenAPI document: 2.1.0
    Contact: engineering@conekta.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import Field, StrictStr

from typing import Optional

from conekta.models.product import Product
from conekta.models.product_order_response import ProductOrderResponse
from conekta.models.update_product import UpdateProduct

from conekta.api_client import ApiClient
from conekta.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ProductsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def orders_create_product(self, id : Annotated[StrictStr, Field(..., description="Identifier of the resource")], product : Annotated[Product, Field(..., description="requested field for a product")], accept_language : Annotated[Optional[StrictStr], Field(description="Use for knowing which language to use")] = None, x_child_company_id : Annotated[Optional[StrictStr], Field(description="In the case of a holding company, the company id of the child company to which will process the request.")] = None, **kwargs) -> ProductOrderResponse:  # noqa: E501
        """Create Product  # noqa: E501

        Create a new product for an existing order.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.orders_create_product(id, product, accept_language, x_child_company_id, async_req=True)
        >>> result = thread.get()

        :param id: Identifier of the resource (required)
        :type id: str
        :param product: requested field for a product (required)
        :type product: Product
        :param accept_language: Use for knowing which language to use
        :type accept_language: str
        :param x_child_company_id: In the case of a holding company, the company id of the child company to which will process the request.
        :type x_child_company_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ProductOrderResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.orders_create_product_with_http_info(id, product, accept_language, x_child_company_id, **kwargs)  # noqa: E501

    @validate_arguments
    def orders_create_product_with_http_info(self, id : Annotated[StrictStr, Field(..., description="Identifier of the resource")], product : Annotated[Product, Field(..., description="requested field for a product")], accept_language : Annotated[Optional[StrictStr], Field(description="Use for knowing which language to use")] = None, x_child_company_id : Annotated[Optional[StrictStr], Field(description="In the case of a holding company, the company id of the child company to which will process the request.")] = None, **kwargs):  # noqa: E501
        """Create Product  # noqa: E501

        Create a new product for an existing order.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.orders_create_product_with_http_info(id, product, accept_language, x_child_company_id, async_req=True)
        >>> result = thread.get()

        :param id: Identifier of the resource (required)
        :type id: str
        :param product: requested field for a product (required)
        :type product: Product
        :param accept_language: Use for knowing which language to use
        :type accept_language: str
        :param x_child_company_id: In the case of a holding company, the company id of the child company to which will process the request.
        :type x_child_company_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
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
        :rtype: tuple(ProductOrderResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'id',
            'product',
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
                    " to method orders_create_product" % _key
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
        if _params['product']:
            _body_params = _params['product']

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
            '200': "ProductOrderResponse",
            '401': "Error",
            '404': "Error",
            '500': "Error",
        }

        return self.api_client.call_api(
            '/orders/{id}/line_items', 'POST',
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
    def orders_delete_product(self, id : Annotated[StrictStr, Field(..., description="Identifier of the resource")], line_item_id : Annotated[StrictStr, Field(..., description="identifier")], accept_language : Annotated[Optional[StrictStr], Field(description="Use for knowing which language to use")] = None, x_child_company_id : Annotated[Optional[StrictStr], Field(description="In the case of a holding company, the company id of the child company to which will process the request.")] = None, **kwargs) -> ProductOrderResponse:  # noqa: E501
        """Delete Product  # noqa: E501

        Delete product for an existing orden  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.orders_delete_product(id, line_item_id, accept_language, x_child_company_id, async_req=True)
        >>> result = thread.get()

        :param id: Identifier of the resource (required)
        :type id: str
        :param line_item_id: identifier (required)
        :type line_item_id: str
        :param accept_language: Use for knowing which language to use
        :type accept_language: str
        :param x_child_company_id: In the case of a holding company, the company id of the child company to which will process the request.
        :type x_child_company_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ProductOrderResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.orders_delete_product_with_http_info(id, line_item_id, accept_language, x_child_company_id, **kwargs)  # noqa: E501

    @validate_arguments
    def orders_delete_product_with_http_info(self, id : Annotated[StrictStr, Field(..., description="Identifier of the resource")], line_item_id : Annotated[StrictStr, Field(..., description="identifier")], accept_language : Annotated[Optional[StrictStr], Field(description="Use for knowing which language to use")] = None, x_child_company_id : Annotated[Optional[StrictStr], Field(description="In the case of a holding company, the company id of the child company to which will process the request.")] = None, **kwargs):  # noqa: E501
        """Delete Product  # noqa: E501

        Delete product for an existing orden  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.orders_delete_product_with_http_info(id, line_item_id, accept_language, x_child_company_id, async_req=True)
        >>> result = thread.get()

        :param id: Identifier of the resource (required)
        :type id: str
        :param line_item_id: identifier (required)
        :type line_item_id: str
        :param accept_language: Use for knowing which language to use
        :type accept_language: str
        :param x_child_company_id: In the case of a holding company, the company id of the child company to which will process the request.
        :type x_child_company_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
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
        :rtype: tuple(ProductOrderResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'id',
            'line_item_id',
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
                    " to method orders_delete_product" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']
        if _params['line_item_id']:
            _path_params['line_item_id'] = _params['line_item_id']

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
            '200': "ProductOrderResponse",
            '401': "Error",
            '422': "Error",
            '404': "Error",
            '500': "Error",
        }

        return self.api_client.call_api(
            '/orders/{id}/line_items/{line_item_id}', 'DELETE',
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
    def orders_update_product(self, id : Annotated[StrictStr, Field(..., description="Identifier of the resource")], line_item_id : Annotated[StrictStr, Field(..., description="identifier")], update_product : Annotated[UpdateProduct, Field(..., description="requested field for products")], accept_language : Annotated[Optional[StrictStr], Field(description="Use for knowing which language to use")] = None, x_child_company_id : Annotated[Optional[StrictStr], Field(description="In the case of a holding company, the company id of the child company to which will process the request.")] = None, **kwargs) -> ProductOrderResponse:  # noqa: E501
        """Update Product  # noqa: E501

        Update an existing product for an existing orden  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.orders_update_product(id, line_item_id, update_product, accept_language, x_child_company_id, async_req=True)
        >>> result = thread.get()

        :param id: Identifier of the resource (required)
        :type id: str
        :param line_item_id: identifier (required)
        :type line_item_id: str
        :param update_product: requested field for products (required)
        :type update_product: UpdateProduct
        :param accept_language: Use for knowing which language to use
        :type accept_language: str
        :param x_child_company_id: In the case of a holding company, the company id of the child company to which will process the request.
        :type x_child_company_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ProductOrderResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.orders_update_product_with_http_info(id, line_item_id, update_product, accept_language, x_child_company_id, **kwargs)  # noqa: E501

    @validate_arguments
    def orders_update_product_with_http_info(self, id : Annotated[StrictStr, Field(..., description="Identifier of the resource")], line_item_id : Annotated[StrictStr, Field(..., description="identifier")], update_product : Annotated[UpdateProduct, Field(..., description="requested field for products")], accept_language : Annotated[Optional[StrictStr], Field(description="Use for knowing which language to use")] = None, x_child_company_id : Annotated[Optional[StrictStr], Field(description="In the case of a holding company, the company id of the child company to which will process the request.")] = None, **kwargs):  # noqa: E501
        """Update Product  # noqa: E501

        Update an existing product for an existing orden  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.orders_update_product_with_http_info(id, line_item_id, update_product, accept_language, x_child_company_id, async_req=True)
        >>> result = thread.get()

        :param id: Identifier of the resource (required)
        :type id: str
        :param line_item_id: identifier (required)
        :type line_item_id: str
        :param update_product: requested field for products (required)
        :type update_product: UpdateProduct
        :param accept_language: Use for knowing which language to use
        :type accept_language: str
        :param x_child_company_id: In the case of a holding company, the company id of the child company to which will process the request.
        :type x_child_company_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
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
        :rtype: tuple(ProductOrderResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'id',
            'line_item_id',
            'update_product',
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
                    " to method orders_update_product" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']
        if _params['line_item_id']:
            _path_params['line_item_id'] = _params['line_item_id']

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
        if _params['update_product']:
            _body_params = _params['update_product']

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
            '200': "ProductOrderResponse",
            '401': "Error",
            '422': "Error",
            '404': "Error",
            '500': "Error",
        }

        return self.api_client.call_api(
            '/orders/{id}/line_items/{line_item_id}', 'PUT',
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
