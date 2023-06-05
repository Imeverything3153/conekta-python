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

from pydantic import Field, StrictStr, conint

from typing import Optional

from conekta.models.event_response import EventResponse
from conekta.models.events_resend_response import EventsResendResponse
from conekta.models.get_events_response import GetEventsResponse

from conekta.api_client import ApiClient
from conekta.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class EventsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_event(self, id : Annotated[StrictStr, Field(..., description="Identifier of the resource")], accept_language : Annotated[Optional[StrictStr], Field(description="Use for knowing which language to use")] = None, x_child_company_id : Annotated[Optional[StrictStr], Field(description="In the case of a holding company, the company id of the child company to which will process the request.")] = None, **kwargs) -> EventResponse:  # noqa: E501
        """Get Event  # noqa: E501

        Returns a single event  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_event(id, accept_language, x_child_company_id, async_req=True)
        >>> result = thread.get()

        :param id: Identifier of the resource (required)
        :type id: str
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
        :rtype: EventResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.get_event_with_http_info(id, accept_language, x_child_company_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_event_with_http_info(self, id : Annotated[StrictStr, Field(..., description="Identifier of the resource")], accept_language : Annotated[Optional[StrictStr], Field(description="Use for knowing which language to use")] = None, x_child_company_id : Annotated[Optional[StrictStr], Field(description="In the case of a holding company, the company id of the child company to which will process the request.")] = None, **kwargs):  # noqa: E501
        """Get Event  # noqa: E501

        Returns a single event  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_event_with_http_info(id, accept_language, x_child_company_id, async_req=True)
        >>> result = thread.get()

        :param id: Identifier of the resource (required)
        :type id: str
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
        :rtype: tuple(EventResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'id',
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
                    " to method get_event" % _key
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

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.conekta-v2.1.0+json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['bearerAuth']  # noqa: E501

        _response_types_map = {
            '200': "EventResponse",
            '401': "Error",
            '404': "Error",
            '500': "Error",
        }

        return self.api_client.call_api(
            '/events/{id}', 'GET',
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
    def get_events(self, accept_language : Annotated[Optional[StrictStr], Field(description="Use for knowing which language to use")] = None, x_child_company_id : Annotated[Optional[StrictStr], Field(description="In the case of a holding company, the company id of the child company to which will process the request.")] = None, limit : Annotated[Optional[conint(strict=True, le=250, ge=1)], Field(description="The numbers of items to return, the maximum value is 250")] = None, search : Annotated[Optional[StrictStr], Field(description="General order search, e.g. by mail, reference etc.")] = None, next : Annotated[Optional[StrictStr], Field(description="next page")] = None, previous : Annotated[Optional[StrictStr], Field(description="previous page")] = None, **kwargs) -> GetEventsResponse:  # noqa: E501
        """Get list of Events  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_events(accept_language, x_child_company_id, limit, search, next, previous, async_req=True)
        >>> result = thread.get()

        :param accept_language: Use for knowing which language to use
        :type accept_language: str
        :param x_child_company_id: In the case of a holding company, the company id of the child company to which will process the request.
        :type x_child_company_id: str
        :param limit: The numbers of items to return, the maximum value is 250
        :type limit: int
        :param search: General order search, e.g. by mail, reference etc.
        :type search: str
        :param next: next page
        :type next: str
        :param previous: previous page
        :type previous: str
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
        :rtype: GetEventsResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.get_events_with_http_info(accept_language, x_child_company_id, limit, search, next, previous, **kwargs)  # noqa: E501

    @validate_arguments
    def get_events_with_http_info(self, accept_language : Annotated[Optional[StrictStr], Field(description="Use for knowing which language to use")] = None, x_child_company_id : Annotated[Optional[StrictStr], Field(description="In the case of a holding company, the company id of the child company to which will process the request.")] = None, limit : Annotated[Optional[conint(strict=True, le=250, ge=1)], Field(description="The numbers of items to return, the maximum value is 250")] = None, search : Annotated[Optional[StrictStr], Field(description="General order search, e.g. by mail, reference etc.")] = None, next : Annotated[Optional[StrictStr], Field(description="next page")] = None, previous : Annotated[Optional[StrictStr], Field(description="previous page")] = None, **kwargs):  # noqa: E501
        """Get list of Events  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_events_with_http_info(accept_language, x_child_company_id, limit, search, next, previous, async_req=True)
        >>> result = thread.get()

        :param accept_language: Use for knowing which language to use
        :type accept_language: str
        :param x_child_company_id: In the case of a holding company, the company id of the child company to which will process the request.
        :type x_child_company_id: str
        :param limit: The numbers of items to return, the maximum value is 250
        :type limit: int
        :param search: General order search, e.g. by mail, reference etc.
        :type search: str
        :param next: next page
        :type next: str
        :param previous: previous page
        :type previous: str
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
        :rtype: tuple(GetEventsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'accept_language',
            'x_child_company_id',
            'limit',
            'search',
            'next',
            'previous'
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
                    " to method get_events" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('limit') is not None:  # noqa: E501
            _query_params.append(('limit', _params['limit']))
        if _params.get('search') is not None:  # noqa: E501
            _query_params.append(('search', _params['search']))
        if _params.get('next') is not None:  # noqa: E501
            _query_params.append(('next', _params['next']))
        if _params.get('previous') is not None:  # noqa: E501
            _query_params.append(('previous', _params['previous']))

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
            '200': "GetEventsResponse",
            '401': "Error",
            '500': "Error",
        }

        return self.api_client.call_api(
            '/events', 'GET',
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
    def resend_event(self, event_id : Annotated[StrictStr, Field(..., description="event identifier")], webhook_log_id : Annotated[StrictStr, Field(..., description="webhook log identifier")], accept_language : Annotated[Optional[StrictStr], Field(description="Use for knowing which language to use")] = None, **kwargs) -> EventsResendResponse:  # noqa: E501
        """Resend Event  # noqa: E501

        Try to send an event  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.resend_event(event_id, webhook_log_id, accept_language, async_req=True)
        >>> result = thread.get()

        :param event_id: event identifier (required)
        :type event_id: str
        :param webhook_log_id: webhook log identifier (required)
        :type webhook_log_id: str
        :param accept_language: Use for knowing which language to use
        :type accept_language: str
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
        :rtype: EventsResendResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.resend_event_with_http_info(event_id, webhook_log_id, accept_language, **kwargs)  # noqa: E501

    @validate_arguments
    def resend_event_with_http_info(self, event_id : Annotated[StrictStr, Field(..., description="event identifier")], webhook_log_id : Annotated[StrictStr, Field(..., description="webhook log identifier")], accept_language : Annotated[Optional[StrictStr], Field(description="Use for knowing which language to use")] = None, **kwargs):  # noqa: E501
        """Resend Event  # noqa: E501

        Try to send an event  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.resend_event_with_http_info(event_id, webhook_log_id, accept_language, async_req=True)
        >>> result = thread.get()

        :param event_id: event identifier (required)
        :type event_id: str
        :param webhook_log_id: webhook log identifier (required)
        :type webhook_log_id: str
        :param accept_language: Use for knowing which language to use
        :type accept_language: str
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
        :rtype: tuple(EventsResendResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'event_id',
            'webhook_log_id',
            'accept_language'
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
                    " to method resend_event" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['event_id']:
            _path_params['event_id'] = _params['event_id']
        if _params['webhook_log_id']:
            _path_params['webhook_log_id'] = _params['webhook_log_id']

        # process the query parameters
        _query_params = []

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['accept_language']:
            _header_params['Accept-Language'] = _params['accept_language']

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
            '200': "EventsResendResponse",
            '401': "Error",
            '404': "Error",
            '500': "Error",
        }

        return self.api_client.call_api(
            '/events/{event_id}/webhook_logs/{webhook_log_id}/resend', 'POST',
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