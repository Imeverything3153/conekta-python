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
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr, constr

class PlanResponse(BaseModel):
    """
    plans model
    """
    amount: Optional[StrictInt] = None
    created_at: Optional[StrictInt] = None
    currency: Optional[constr(strict=True, max_length=3)] = None
    expiry_count: Optional[StrictInt] = None
    frequency: Optional[StrictInt] = None
    id: Optional[StrictStr] = None
    interval: Optional[StrictStr] = None
    livemode: Optional[StrictBool] = None
    name: Optional[StrictStr] = None
    object: Optional[StrictStr] = None
    trial_period_days: Optional[StrictInt] = None
    __properties = ["amount", "created_at", "currency", "expiry_count", "frequency", "id", "interval", "livemode", "name", "object", "trial_period_days"]

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
    def from_json(cls, json_str: str) -> PlanResponse:
        """Create an instance of PlanResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if expiry_count (nullable) is None
        # and __fields_set__ contains the field
        if self.expiry_count is None and "expiry_count" in self.__fields_set__:
            _dict['expiry_count'] = None

        # set to None if trial_period_days (nullable) is None
        # and __fields_set__ contains the field
        if self.trial_period_days is None and "trial_period_days" in self.__fields_set__:
            _dict['trial_period_days'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PlanResponse:
        """Create an instance of PlanResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PlanResponse.parse_obj(obj)

        _obj = PlanResponse.parse_obj({
            "amount": obj.get("amount"),
            "created_at": obj.get("created_at"),
            "currency": obj.get("currency"),
            "expiry_count": obj.get("expiry_count"),
            "frequency": obj.get("frequency"),
            "id": obj.get("id"),
            "interval": obj.get("interval"),
            "livemode": obj.get("livemode"),
            "name": obj.get("name"),
            "object": obj.get("object"),
            "trial_period_days": obj.get("trial_period_days")
        })
        return _obj

