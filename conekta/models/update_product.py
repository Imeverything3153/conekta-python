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


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, StrictStr, conint, constr

class UpdateProduct(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    antifraud_info: Optional[Dict[str, Dict[str, Any]]] = None
    description: Optional[constr(strict=True, max_length=250)] = None
    sku: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    unit_price: Optional[conint(strict=True, ge=0)] = None
    quantity: Optional[conint(strict=True, ge=1)] = None
    tags: Optional[List[StrictStr]] = None
    brand: Optional[StrictStr] = None
    metadata: Optional[Dict[str, StrictStr]] = None
    __properties = ["antifraud_info", "description", "sku", "name", "unit_price", "quantity", "tags", "brand", "metadata"]

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
    def from_json(cls, json_str: str) -> UpdateProduct:
        """Create an instance of UpdateProduct from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpdateProduct:
        """Create an instance of UpdateProduct from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return UpdateProduct.parse_obj(obj)

        _obj = UpdateProduct.parse_obj({
            "antifraud_info": obj.get("antifraud_info"),
            "description": obj.get("description"),
            "sku": obj.get("sku"),
            "name": obj.get("name"),
            "unit_price": obj.get("unit_price"),
            "quantity": obj.get("quantity"),
            "tags": obj.get("tags"),
            "brand": obj.get("brand"),
            "metadata": obj.get("metadata")
        })
        return _obj

