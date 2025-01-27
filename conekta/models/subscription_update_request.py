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

class SubscriptionUpdateRequest(BaseModel):
    """
    You can modify the subscription to change the plan used by your customers.
    """
    plan_id: Optional[StrictStr] = None
    card_id: Optional[StrictStr] = None
    trial_end: Optional[StrictInt] = None
    __properties = ["plan_id", "card_id", "trial_end"]

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
    def from_json(cls, json_str: str) -> SubscriptionUpdateRequest:
        """Create an instance of SubscriptionUpdateRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SubscriptionUpdateRequest:
        """Create an instance of SubscriptionUpdateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SubscriptionUpdateRequest.parse_obj(obj)

        _obj = SubscriptionUpdateRequest.parse_obj({
            "plan_id": obj.get("plan_id"),
            "card_id": obj.get("card_id"),
            "trial_end": obj.get("trial_end")
        })
        return _obj

