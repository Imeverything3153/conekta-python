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
from pydantic import BaseModel, StrictBool

class DeleteApiKeysResponseAllOf(BaseModel):
    """
    DeleteApiKeysResponseAllOf
    """
    deleted: Optional[StrictBool] = None
    __properties = ["deleted"]

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
    def from_json(cls, json_str: str) -> DeleteApiKeysResponseAllOf:
        """Create an instance of DeleteApiKeysResponseAllOf from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DeleteApiKeysResponseAllOf:
        """Create an instance of DeleteApiKeysResponseAllOf from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DeleteApiKeysResponseAllOf.parse_obj(obj)

        _obj = DeleteApiKeysResponseAllOf.parse_obj({
            "deleted": obj.get("deleted")
        })
        return _obj

