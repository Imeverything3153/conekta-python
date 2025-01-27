# coding: utf-8

"""
    Conekta API

    Conekta sdk  # noqa: E501

    The version of the OpenAPI document: 2.1.0
    Contact: engineering@conekta.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, StrictInt, StrictStr

class PaymentMethodCashResponseAllOf(BaseModel):
    """
    use for cash responses
    """
    reference: Optional[StrictStr] = None
    barcode: Optional[StrictStr] = None
    barcode_url: Optional[StrictStr] = None
    expires_at: Optional[StrictInt] = None
    provider: Optional[StrictStr] = None
    __properties = ["reference", "barcode", "barcode_url", "expires_at", "provider"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> PaymentMethodCashResponseAllOf:
        """Create an instance of PaymentMethodCashResponseAllOf from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PaymentMethodCashResponseAllOf:
        """Create an instance of PaymentMethodCashResponseAllOf from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PaymentMethodCashResponseAllOf.parse_obj(obj)

        _obj = PaymentMethodCashResponseAllOf.parse_obj({
            "reference": obj.get("reference"),
            "barcode": obj.get("barcode"),
            "barcode_url": obj.get("barcode_url"),
            "expires_at": obj.get("expires_at"),
            "provider": obj.get("provider")
        })
        return _obj

