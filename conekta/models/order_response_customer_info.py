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
from pydantic import BaseModel, StrictBool, StrictStr

class OrderResponseCustomerInfo(BaseModel):
    """
    OrderResponseCustomerInfo
    """
    object: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    phone: Optional[StrictStr] = None
    corporate: Optional[StrictBool] = False
    customer_id: Optional[StrictStr] = None
    __properties = ["object", "name", "email", "phone", "corporate", "customer_id"]

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
    def from_json(cls, json_str: str) -> OrderResponseCustomerInfo:
        """Create an instance of OrderResponseCustomerInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OrderResponseCustomerInfo:
        """Create an instance of OrderResponseCustomerInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OrderResponseCustomerInfo.parse_obj(obj)

        _obj = OrderResponseCustomerInfo.parse_obj({
            "object": obj.get("object"),
            "name": obj.get("name"),
            "email": obj.get("email"),
            "phone": obj.get("phone"),
            "corporate": obj.get("corporate") if obj.get("corporate") is not None else False,
            "customer_id": obj.get("customer_id")
        })
        return _obj

