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


from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr

class ChargeRequestPaymentMethod(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    expires_at: Optional[StrictInt] = Field(None, description="Method expiration date as unix timestamp")
    type: StrictStr = ...
    token_id: Optional[StrictStr] = None
    payment_source_id: Optional[StrictStr] = None
    __properties = ["expires_at", "type", "token_id", "payment_source_id"]

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
    def from_json(cls, json_str: str) -> ChargeRequestPaymentMethod:
        """Create an instance of ChargeRequestPaymentMethod from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ChargeRequestPaymentMethod:
        """Create an instance of ChargeRequestPaymentMethod from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ChargeRequestPaymentMethod.parse_obj(obj)

        _obj = ChargeRequestPaymentMethod.parse_obj({
            "expires_at": obj.get("expires_at"),
            "type": obj.get("type"),
            "token_id": obj.get("token_id"),
            "payment_source_id": obj.get("payment_source_id")
        })
        return _obj
