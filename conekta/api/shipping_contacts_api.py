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

from conekta.models.customer_shipping_contacts import CustomerShippingContacts
from conekta.models.customer_shipping_contacts_response import CustomerShippingContactsResponse
from conekta.models.customer_update_shipping_contacts import CustomerUpdateShippingContacts

from conekta.api_client import ApiClient
from conekta.api_response import ApiResponse
from conekta.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ShippingContactsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def create_customer_shipping_contacts(self, id : Annotated[StrictStr, Field(..., description="Identifier of the resource")], customer_shipping_contacts : Annotated[CustomerShippingContacts, Field(..., description="requested field for customer shippings contacts")], accept_language : Annotated[Optional[StrictStr], Field(description="Use for knowing which language to use")] = None, x_child_company_id : Annotated[Optional[StrictStr], Field(description="In the case of a holding company, the company id of the child company to which will process the request.")] = None, **kwargs) -> CustomerShippingContactsResponse:  # noqa: E501
        """Create a shipping contacts  # noqa: E501

        Create a shipping contacts for a customer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_customer_shipping_contacts(id, customer_shipping_contacts, accept_language, x_child_company_id, async_req=True)
        >>> result = thread.get()

        :param id: Identifier of the resource (required)
        :type id: str
        :param customer_shipping_contacts: requested field for customer shippings contacts (required)
        :type customer_shipping_contacts: CustomerShippingContacts
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
        :rtype: CustomerShippingContactsResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the create_customer_shipping_contacts_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.create_customer_shipping_contacts_with_http_info(id, customer_shipping_contacts, accept_language, x_child_company_id, **kwargs)  # noqa: E501

    @validate_arguments
    def create_customer_shipping_contacts_with_http_info(self, id : Annotated[StrictStr, Field(..., description="Identifier of the resource")], customer_shipping_contacts : Annotated[CustomerShippingContacts, Field(..., description="requested field for customer shippings contacts")], accept_language : Annotated[Optional[StrictStr], Field(description="Use for knowing which language to use")] = None, x_child_company_id : Annotated[Optional[StrictStr], Field(description="In the case of a holding company, the company id of the child company to which will process the request.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Create a shipping contacts  # noqa: E501

        Create a shipping contacts for a customer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_customer_shipping_contacts_with_http_info(id, customer_shipping_contacts, accept_language, x_child_company_id, async_req=True)
        >>> result = thread.get()

        :param id: Identifier of the resource (required)
        :type id: str
        :param customer_shipping_contacts: requested field for customer shippings contacts (required)
        :type customer_shipping_contacts: CustomerShippingContacts
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
        :rtype: tuple(CustomerShippingContactsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'id',
            'customer_shipping_contacts',
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
                    " to method create_customer_shipping_contacts" % _key
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
        if _params['customer_shipping_contacts'] is not None:
            _body_params = _params['customer_shipping_contacts']

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
            '200': "CustomerShippingContactsResponse",
            '401': "Error",
            '404': "Error",
            '422': "Error",
            '500': "Error",
        }

        return self.api_client.call_api(
            '/customers/{id}/shipping_contacts', 'POST',
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
    def delete_customer_shipping_contacts(self, id : Annotated[StrictStr, Field(..., description="Identifier of the resource")], shipping_contacts_id : Annotated[StrictStr, Field(..., description="identifier")], accept_language : Annotated[Optional[StrictStr], Field(description="Use for knowing which language to use")] = None, x_child_company_id : Annotated[Optional[StrictStr], Field(description="In the case of a holding company, the company id of the child company to which will process the request.")] = None, **kwargs) -> CustomerShippingContactsResponse:  # noqa: E501
        """Delete shipping contacts  # noqa: E501

        Delete shipping contact that corresponds to a customer ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_customer_shipping_contacts(id, shipping_contacts_id, accept_language, x_child_company_id, async_req=True)
        >>> result = thread.get()

        :param id: Identifier of the resource (required)
        :type id: str
        :param shipping_contacts_id: identifier (required)
        :type shipping_contacts_id: str
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
        :rtype: CustomerShippingContactsResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the delete_customer_shipping_contacts_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.delete_customer_shipping_contacts_with_http_info(id, shipping_contacts_id, accept_language, x_child_company_id, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_customer_shipping_contacts_with_http_info(self, id : Annotated[StrictStr, Field(..., description="Identifier of the resource")], shipping_contacts_id : Annotated[StrictStr, Field(..., description="identifier")], accept_language : Annotated[Optional[StrictStr], Field(description="Use for knowing which language to use")] = None, x_child_company_id : Annotated[Optional[StrictStr], Field(description="In the case of a holding company, the company id of the child company to which will process the request.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Delete shipping contacts  # noqa: E501

        Delete shipping contact that corresponds to a customer ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_customer_shipping_contacts_with_http_info(id, shipping_contacts_id, accept_language, x_child_company_id, async_req=True)
        >>> result = thread.get()

        :param id: Identifier of the resource (required)
        :type id: str
        :param shipping_contacts_id: identifier (required)
        :type shipping_contacts_id: str
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
        :rtype: tuple(CustomerShippingContactsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'id',
            'shipping_contacts_id',
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
                    " to method delete_customer_shipping_contacts" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']

        if _params['shipping_contacts_id']:
            _path_params['shipping_contacts_id'] = _params['shipping_contacts_id']


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
            '200': "CustomerShippingContactsResponse",
            '401': "Error",
            '404': "Error",
            '422': "Error",
            '500': "Error",
        }

        return self.api_client.call_api(
            '/customers/{id}/shipping_contacts/{shipping_contacts_id}', 'DELETE',
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
    def update_customer_shipping_contacts(self, id : Annotated[StrictStr, Field(..., description="Identifier of the resource")], shipping_contacts_id : Annotated[StrictStr, Field(..., description="identifier")], customer_update_shipping_contacts : Annotated[CustomerUpdateShippingContacts, Field(..., description="requested field for customer update shippings contacts")], accept_language : Annotated[Optional[StrictStr], Field(description="Use for knowing which language to use")] = None, x_child_company_id : Annotated[Optional[StrictStr], Field(description="In the case of a holding company, the company id of the child company to which will process the request.")] = None, **kwargs) -> CustomerShippingContactsResponse:  # noqa: E501
        """Update shipping contacts  # noqa: E501

        Update shipping contact that corresponds to a customer ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_customer_shipping_contacts(id, shipping_contacts_id, customer_update_shipping_contacts, accept_language, x_child_company_id, async_req=True)
        >>> result = thread.get()

        :param id: Identifier of the resource (required)
        :type id: str
        :param shipping_contacts_id: identifier (required)
        :type shipping_contacts_id: str
        :param customer_update_shipping_contacts: requested field for customer update shippings contacts (required)
        :type customer_update_shipping_contacts: CustomerUpdateShippingContacts
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
        :rtype: CustomerShippingContactsResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the update_customer_shipping_contacts_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.update_customer_shipping_contacts_with_http_info(id, shipping_contacts_id, customer_update_shipping_contacts, accept_language, x_child_company_id, **kwargs)  # noqa: E501

    @validate_arguments
    def update_customer_shipping_contacts_with_http_info(self, id : Annotated[StrictStr, Field(..., description="Identifier of the resource")], shipping_contacts_id : Annotated[StrictStr, Field(..., description="identifier")], customer_update_shipping_contacts : Annotated[CustomerUpdateShippingContacts, Field(..., description="requested field for customer update shippings contacts")], accept_language : Annotated[Optional[StrictStr], Field(description="Use for knowing which language to use")] = None, x_child_company_id : Annotated[Optional[StrictStr], Field(description="In the case of a holding company, the company id of the child company to which will process the request.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Update shipping contacts  # noqa: E501

        Update shipping contact that corresponds to a customer ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_customer_shipping_contacts_with_http_info(id, shipping_contacts_id, customer_update_shipping_contacts, accept_language, x_child_company_id, async_req=True)
        >>> result = thread.get()

        :param id: Identifier of the resource (required)
        :type id: str
        :param shipping_contacts_id: identifier (required)
        :type shipping_contacts_id: str
        :param customer_update_shipping_contacts: requested field for customer update shippings contacts (required)
        :type customer_update_shipping_contacts: CustomerUpdateShippingContacts
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
        :rtype: tuple(CustomerShippingContactsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'id',
            'shipping_contacts_id',
            'customer_update_shipping_contacts',
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
                    " to method update_customer_shipping_contacts" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']

        if _params['shipping_contacts_id']:
            _path_params['shipping_contacts_id'] = _params['shipping_contacts_id']


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
        if _params['customer_update_shipping_contacts'] is not None:
            _body_params = _params['customer_update_shipping_contacts']

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
            '200': "CustomerShippingContactsResponse",
            '401': "Error",
            '404': "Error",
            '422': "Error",
            '500': "Error",
        }

        return self.api_client.call_api(
            '/customers/{id}/shipping_contacts/{shipping_contacts_id}', 'PUT',
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
