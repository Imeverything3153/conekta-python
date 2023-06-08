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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from conekta.models.customer_fiscal_entities_request_address import CustomerFiscalEntitiesRequestAddress

class CreateCustomerFiscalEntitiesResponse(BaseModel):
    """
    CreateCustomerFiscalEntitiesResponse
    """
    address: CustomerFiscalEntitiesRequestAddress = Field(...)
    tax_id: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    phone: Optional[StrictStr] = None
    metadata: Optional[Dict[str, Dict[str, Any]]] = None
    company_name: Optional[StrictStr] = None
    id: StrictStr = Field(...)
    object: StrictStr = Field(...)
    created_at: StrictInt = Field(...)
    parent_id: Optional[StrictStr] = None
    default: Optional[StrictBool] = None
    __properties = ["address", "tax_id", "email", "phone", "metadata", "company_name", "id", "object", "created_at", "parent_id", "default"]

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
    def from_json(cls, json_str: str) -> CreateCustomerFiscalEntitiesResponse:
        """Create an instance of CreateCustomerFiscalEntitiesResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of address
        if self.address:
            _dict['address'] = self.address.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateCustomerFiscalEntitiesResponse:
        """Create an instance of CreateCustomerFiscalEntitiesResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateCustomerFiscalEntitiesResponse.parse_obj(obj)

        _obj = CreateCustomerFiscalEntitiesResponse.parse_obj({
            "address": CustomerFiscalEntitiesRequestAddress.from_dict(obj.get("address")) if obj.get("address") is not None else None,
            "tax_id": obj.get("tax_id"),
            "email": obj.get("email"),
            "phone": obj.get("phone"),
            "metadata": obj.get("metadata"),
            "company_name": obj.get("company_name"),
            "id": obj.get("id"),
            "object": obj.get("object"),
            "created_at": obj.get("created_at"),
            "parent_id": obj.get("parent_id"),
            "default": obj.get("default")
        })
        return _obj

