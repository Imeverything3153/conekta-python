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
from pydantic import BaseModel, Field, StrictInt, StrictStr
from conekta.models.charge_request_payment_method import ChargeRequestPaymentMethod

class ChargeRequest(BaseModel):
    """
    The charges to be made
    """
    amount: Optional[StrictInt] = None
    monthly_installments: Optional[StrictInt] = Field(None, description="How many months without interest to apply, it can be 3, 6, 9, 12 or 18")
    payment_method: ChargeRequestPaymentMethod = Field(...)
    reference_id: Optional[StrictStr] = Field(None, description="Custom reference to add to the charge")
    __properties = ["amount", "monthly_installments", "payment_method", "reference_id"]

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
    def from_json(cls, json_str: str) -> ChargeRequest:
        """Create an instance of ChargeRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of payment_method
        if self.payment_method:
            _dict['payment_method'] = self.payment_method.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ChargeRequest:
        """Create an instance of ChargeRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ChargeRequest.parse_obj(obj)

        _obj = ChargeRequest.parse_obj({
            "amount": obj.get("amount"),
            "monthly_installments": obj.get("monthly_installments"),
            "payment_method": ChargeRequestPaymentMethod.from_dict(obj.get("payment_method")) if obj.get("payment_method") is not None else None,
            "reference_id": obj.get("reference_id")
        })
        return _obj

