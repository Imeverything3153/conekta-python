# coding: utf-8

"""
    Conekta API

    Conekta sdk  # noqa: E501

    The version of the OpenAPI document: 2.1.0
    Contact: engineering@conekta.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, Optional
from pydantic import BaseModel, StrictInt, StrictStr

class EventsResendResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    failed_attempts: Optional[StrictInt] = None
    id: Optional[StrictStr] = None
    last_attempted_at: Optional[StrictInt] = None
    last_http_response_status: Optional[StrictInt] = None
    response_data: Optional[Dict[str, Any]] = None
    url: Optional[StrictStr] = None
    __properties = ["failed_attempts", "id", "last_attempted_at", "last_http_response_status", "response_data", "url"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> EventsResendResponse:
        """Create an instance of EventsResendResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EventsResendResponse:
        """Create an instance of EventsResendResponse from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return EventsResendResponse.parse_obj(obj)

        _obj = EventsResendResponse.parse_obj({
            "failed_attempts": obj.get("failed_attempts"),
            "id": obj.get("id"),
            "last_attempted_at": obj.get("last_attempted_at"),
            "last_http_response_status": obj.get("last_http_response_status"),
            "response_data": obj.get("response_data"),
            "url": obj.get("url")
        })
        return _obj

