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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from conekta.models.customer_shipping_contacts_address import CustomerShippingContactsAddress

class CustomerShippingContactsDataResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    phone: Optional[StrictStr] = Field(None, description="Phone contact")
    receiver: Optional[StrictStr] = Field(None, description="Name of the person who will receive the order")
    between_streets: Optional[StrictStr] = Field(None, description="The street names between which the order will be delivered.")
    address: CustomerShippingContactsAddress = ...
    parent_id: Optional[StrictStr] = None
    default: Optional[StrictBool] = None
    deleted: Optional[StrictBool] = None
    id: StrictStr = ...
    object: StrictStr = ...
    created_at: StrictInt = ...
    __properties = ["phone", "receiver", "between_streets", "address", "parent_id", "default", "deleted", "id", "object", "created_at"]

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
    def from_json(cls, json_str: str) -> CustomerShippingContactsDataResponse:
        """Create an instance of CustomerShippingContactsDataResponse from a JSON string"""
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
        # set to None if default (nullable) is None
        if self.default is None:
            _dict['default'] = None

        # set to None if deleted (nullable) is None
        if self.deleted is None:
            _dict['deleted'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CustomerShippingContactsDataResponse:
        """Create an instance of CustomerShippingContactsDataResponse from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return CustomerShippingContactsDataResponse.parse_obj(obj)

        _obj = CustomerShippingContactsDataResponse.parse_obj({
            "phone": obj.get("phone"),
            "receiver": obj.get("receiver"),
            "between_streets": obj.get("between_streets"),
            "address": CustomerShippingContactsAddress.from_dict(obj.get("address")) if obj.get("address") is not None else None,
            "parent_id": obj.get("parent_id"),
            "default": obj.get("default"),
            "deleted": obj.get("deleted"),
            "id": obj.get("id"),
            "object": obj.get("object"),
            "created_at": obj.get("created_at")
        })
        return _obj
