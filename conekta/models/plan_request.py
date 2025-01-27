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
from pydantic import BaseModel, Field, StrictInt, StrictStr, conint, constr, validator

class PlanRequest(BaseModel):
    """
    a plan
    """
    amount: conint(strict=True, ge=1) = Field(..., description="The amount in cents that will be charged on the interval specified.")
    currency: Optional[constr(strict=True, max_length=3)] = Field(None, description="ISO 4217 for currencies, for the Mexican peso it is MXN/USD")
    expiry_count: Optional[StrictInt] = Field(None, description="Number of repetitions of the frequency NUMBER OF CHARGES TO BE MADE, considering the interval and frequency, this evolves over time, but is subject to the expiration count.")
    frequency: conint(strict=True, ge=1) = Field(..., description="Frequency of the charge, which together with the interval, can be every 3 weeks, every 4 months, every 2 years, every 5 fortnights")
    id: Optional[StrictStr] = Field(None, description="internal reference id")
    interval: StrictStr = Field(..., description="The interval of time between each charge.")
    name: StrictStr = Field(..., description="The name of the plan.")
    trial_period_days: Optional[StrictInt] = Field(None, description="The number of days the customer will have a free trial.")
    __properties = ["amount", "currency", "expiry_count", "frequency", "id", "interval", "name", "trial_period_days"]

    @validator('interval')
    def interval_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('week', 'half_month', 'month', 'year'):
            raise ValueError("must be one of enum values ('week', 'half_month', 'month', 'year')")
        return value

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
    def from_json(cls, json_str: str) -> PlanRequest:
        """Create an instance of PlanRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PlanRequest:
        """Create an instance of PlanRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PlanRequest.parse_obj(obj)

        _obj = PlanRequest.parse_obj({
            "amount": obj.get("amount"),
            "currency": obj.get("currency"),
            "expiry_count": obj.get("expiry_count"),
            "frequency": obj.get("frequency"),
            "id": obj.get("id"),
            "interval": obj.get("interval"),
            "name": obj.get("name"),
            "trial_period_days": obj.get("trial_period_days")
        })
        return _obj

