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


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from conekta.models.customer_antifraud_info import CustomerAntifraudInfo
from conekta.models.customer_fiscal_entities_request import CustomerFiscalEntitiesRequest
from conekta.models.customer_payment_methods_request import CustomerPaymentMethodsRequest
from conekta.models.customer_shipping_contacts import CustomerShippingContacts
from conekta.models.subscription_request import SubscriptionRequest

class Customer(BaseModel):
    """
    a customer
    """
    antifraud_info: Optional[CustomerAntifraudInfo] = None
    corporate: Optional[StrictBool] = Field(False, description="It is a value that allows identifying if the email is corporate or not.")
    custom_reference: Optional[StrictStr] = Field(None, description="It is an undefined value.")
    email: StrictStr = Field(..., description="An email address is a series of customizable characters followed by a universal Internet symbol, the at symbol (@), the name of a host server, and a web domain ending (.mx, .com, .org, . net, etc).")
    default_payment_source_id: Optional[StrictStr] = Field(None, description="It is a parameter that allows to identify in the response, the Conekta ID of a payment method (payment_id)")
    default_shipping_contact_id: Optional[StrictStr] = Field(None, description="It is a parameter that allows to identify in the response, the Conekta ID of the shipping address (shipping_contact)")
    fiscal_entities: Optional[conlist(CustomerFiscalEntitiesRequest)] = None
    metadata: Optional[Dict[str, Any]] = None
    name: StrictStr = Field(..., description="Client's name")
    payment_sources: Optional[conlist(CustomerPaymentMethodsRequest)] = Field(None, description="Contains details of the payment methods that the customer has active or has used in Conekta")
    phone: StrictStr = Field(..., description="Is the customer's phone number")
    plan_id: Optional[StrictStr] = Field(None, description="Contains the ID of a plan, which could together with name, email and phone create a client directly to a subscription")
    shipping_contacts: Optional[conlist(CustomerShippingContacts)] = Field(None, description="Contains the detail of the shipping addresses that the client has active or has used in Conekta")
    subscription: Optional[SubscriptionRequest] = None
    __properties = ["antifraud_info", "corporate", "custom_reference", "email", "default_payment_source_id", "default_shipping_contact_id", "fiscal_entities", "metadata", "name", "payment_sources", "phone", "plan_id", "shipping_contacts", "subscription"]

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
    def from_json(cls, json_str: str) -> Customer:
        """Create an instance of Customer from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of antifraud_info
        if self.antifraud_info:
            _dict['antifraud_info'] = self.antifraud_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in fiscal_entities (list)
        _items = []
        if self.fiscal_entities:
            for _item in self.fiscal_entities:
                if _item:
                    _items.append(_item.to_dict())
            _dict['fiscal_entities'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in payment_sources (list)
        _items = []
        if self.payment_sources:
            for _item in self.payment_sources:
                if _item:
                    _items.append(_item.to_dict())
            _dict['payment_sources'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in shipping_contacts (list)
        _items = []
        if self.shipping_contacts:
            for _item in self.shipping_contacts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['shipping_contacts'] = _items
        # override the default output from pydantic by calling `to_dict()` of subscription
        if self.subscription:
            _dict['subscription'] = self.subscription.to_dict()
        # set to None if antifraud_info (nullable) is None
        # and __fields_set__ contains the field
        if self.antifraud_info is None and "antifraud_info" in self.__fields_set__:
            _dict['antifraud_info'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Customer:
        """Create an instance of Customer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Customer.parse_obj(obj)

        _obj = Customer.parse_obj({
            "antifraud_info": CustomerAntifraudInfo.from_dict(obj.get("antifraud_info")) if obj.get("antifraud_info") is not None else None,
            "corporate": obj.get("corporate") if obj.get("corporate") is not None else False,
            "custom_reference": obj.get("custom_reference"),
            "email": obj.get("email"),
            "default_payment_source_id": obj.get("default_payment_source_id"),
            "default_shipping_contact_id": obj.get("default_shipping_contact_id"),
            "fiscal_entities": [CustomerFiscalEntitiesRequest.from_dict(_item) for _item in obj.get("fiscal_entities")] if obj.get("fiscal_entities") is not None else None,
            "metadata": obj.get("metadata"),
            "name": obj.get("name"),
            "payment_sources": [CustomerPaymentMethodsRequest.from_dict(_item) for _item in obj.get("payment_sources")] if obj.get("payment_sources") is not None else None,
            "phone": obj.get("phone"),
            "plan_id": obj.get("plan_id"),
            "shipping_contacts": [CustomerShippingContacts.from_dict(_item) for _item in obj.get("shipping_contacts")] if obj.get("shipping_contacts") is not None else None,
            "subscription": SubscriptionRequest.from_dict(obj.get("subscription")) if obj.get("subscription") is not None else None
        })
        return _obj

