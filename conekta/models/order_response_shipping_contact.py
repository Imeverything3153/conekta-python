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
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from conekta.models.customer_shipping_contacts_response_address import CustomerShippingContactsResponseAddress

class OrderResponseShippingContact(BaseModel):
    """
    OrderResponseShippingContact
    """
    created_at: Optional[StrictInt] = None
    id: Optional[StrictStr] = None
    object: Optional[StrictStr] = None
    phone: Optional[StrictStr] = None
    receiver: Optional[StrictStr] = None
    between_streets: Optional[StrictStr] = None
    address: Optional[CustomerShippingContactsResponseAddress] = None
    parent_id: Optional[StrictStr] = None
    default: Optional[StrictBool] = None
    deleted: Optional[StrictBool] = None
    __properties = ["created_at", "id", "object", "phone", "receiver", "between_streets", "address", "parent_id", "default", "deleted"]

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
    def from_json(cls, json_str: str) -> OrderResponseShippingContact:
        """Create an instance of OrderResponseShippingContact from a JSON string"""
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
        # set to None if between_streets (nullable) is None
        # and __fields_set__ contains the field
        if self.between_streets is None and "between_streets" in self.__fields_set__:
            _dict['between_streets'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OrderResponseShippingContact:
        """Create an instance of OrderResponseShippingContact from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OrderResponseShippingContact.parse_obj(obj)

        _obj = OrderResponseShippingContact.parse_obj({
            "created_at": obj.get("created_at"),
            "id": obj.get("id"),
            "object": obj.get("object"),
            "phone": obj.get("phone"),
            "receiver": obj.get("receiver"),
            "between_streets": obj.get("between_streets"),
            "address": CustomerShippingContactsResponseAddress.from_dict(obj.get("address")) if obj.get("address") is not None else None,
            "parent_id": obj.get("parent_id"),
            "default": obj.get("default"),
            "deleted": obj.get("deleted")
        })
        return _obj

