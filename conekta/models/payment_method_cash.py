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
from pydantic import BaseModel, StrictInt, StrictStr

class PaymentMethodCash(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    type: Optional[StrictStr] = None
    object: StrictStr = ...
    auth_code: Optional[StrictInt] = None
    cashier_id: Optional[StrictStr] = None
    reference: Optional[StrictStr] = None
    barcode_url: Optional[StrictStr] = None
    expires_at: Optional[StrictInt] = None
    service_name: Optional[StrictStr] = None
    store: Optional[StrictStr] = None
    store_name: Optional[StrictStr] = None
    __properties = ["type", "object", "auth_code", "cashier_id", "reference", "barcode_url", "expires_at", "service_name", "store", "store_name"]

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
    def from_json(cls, json_str: str) -> PaymentMethodCash:
        """Create an instance of PaymentMethodCash from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if auth_code (nullable) is None
        if self.auth_code is None:
            _dict['auth_code'] = None

        # set to None if cashier_id (nullable) is None
        if self.cashier_id is None:
            _dict['cashier_id'] = None

        # set to None if store (nullable) is None
        if self.store is None:
            _dict['store'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PaymentMethodCash:
        """Create an instance of PaymentMethodCash from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return PaymentMethodCash.parse_obj(obj)

        _obj = PaymentMethodCash.parse_obj({
            "type": obj.get("type"),
            "object": obj.get("object"),
            "auth_code": obj.get("auth_code"),
            "cashier_id": obj.get("cashier_id"),
            "reference": obj.get("reference"),
            "barcode_url": obj.get("barcode_url"),
            "expires_at": obj.get("expires_at"),
            "service_name": obj.get("service_name"),
            "store": obj.get("store"),
            "store_name": obj.get("store_name")
        })
        return _obj
