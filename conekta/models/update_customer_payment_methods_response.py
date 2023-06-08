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
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from conekta.models.payment_method_card_response import PaymentMethodCardResponse
from conekta.models.payment_method_cash_response import PaymentMethodCashResponse
from conekta.models.payment_method_spei_recurrent import PaymentMethodSpeiRecurrent
from typing import Any, List
from pydantic import StrictStr, Field

UPDATECUSTOMERPAYMENTMETHODSRESPONSE_ONE_OF_SCHEMAS = ["PaymentMethodCardResponse", "PaymentMethodCashResponse", "PaymentMethodSpeiRecurrent"]

class UpdateCustomerPaymentMethodsResponse(BaseModel):
    """
    UpdateCustomerPaymentMethodsResponse
    """
    # data type: PaymentMethodCashResponse
    oneof_schema_1_validator: Optional[PaymentMethodCashResponse] = None
    # data type: PaymentMethodCardResponse
    oneof_schema_2_validator: Optional[PaymentMethodCardResponse] = None
    # data type: PaymentMethodSpeiRecurrent
    oneof_schema_3_validator: Optional[PaymentMethodSpeiRecurrent] = None
    actual_instance: Any
    one_of_schemas: List[str] = Field(UPDATECUSTOMERPAYMENTMETHODSRESPONSE_ONE_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    discriminator_value_class_map = {
    }

    def __init__(self, *args, **kwargs):
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = UpdateCustomerPaymentMethodsResponse.construct()
        error_messages = []
        match = 0
        # validate data type: PaymentMethodCashResponse
        if not isinstance(v, PaymentMethodCashResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PaymentMethodCashResponse`")
        else:
            match += 1
        # validate data type: PaymentMethodCardResponse
        if not isinstance(v, PaymentMethodCardResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PaymentMethodCardResponse`")
        else:
            match += 1
        # validate data type: PaymentMethodSpeiRecurrent
        if not isinstance(v, PaymentMethodSpeiRecurrent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PaymentMethodSpeiRecurrent`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in UpdateCustomerPaymentMethodsResponse with oneOf schemas: PaymentMethodCardResponse, PaymentMethodCashResponse, PaymentMethodSpeiRecurrent. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in UpdateCustomerPaymentMethodsResponse with oneOf schemas: PaymentMethodCardResponse, PaymentMethodCashResponse, PaymentMethodSpeiRecurrent. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> UpdateCustomerPaymentMethodsResponse:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> UpdateCustomerPaymentMethodsResponse:
        """Returns the object represented by the json string"""
        instance = UpdateCustomerPaymentMethodsResponse.construct()
        error_messages = []
        match = 0

        # use oneOf discriminator to lookup the data type
        _data_type = json.loads(json_str).get("type")
        if not _data_type:
            raise ValueError("Failed to lookup data type from the field `type` in the input.")

        # check if data type is `PaymentMethodCardResponse`
        if _data_type == "card":
            instance.actual_instance = PaymentMethodCardResponse.from_json(json_str)
            return instance

        # check if data type is `PaymentMethodCashResponse`
        if _data_type == "cash":
            instance.actual_instance = PaymentMethodCashResponse.from_json(json_str)
            return instance

        # check if data type is `PaymentMethodCashResponse`
        if _data_type == "oxxo_recurrent":
            instance.actual_instance = PaymentMethodCashResponse.from_json(json_str)
            return instance

        # check if data type is `PaymentMethodCardResponse`
        if _data_type == "payment_method_card_response":
            instance.actual_instance = PaymentMethodCardResponse.from_json(json_str)
            return instance

        # check if data type is `PaymentMethodCashResponse`
        if _data_type == "payment_method_cash_response":
            instance.actual_instance = PaymentMethodCashResponse.from_json(json_str)
            return instance

        # check if data type is `PaymentMethodSpeiRecurrent`
        if _data_type == "payment_method_spei_recurrent":
            instance.actual_instance = PaymentMethodSpeiRecurrent.from_json(json_str)
            return instance

        # check if data type is `PaymentMethodSpeiRecurrent`
        if _data_type == "spei_recurrent":
            instance.actual_instance = PaymentMethodSpeiRecurrent.from_json(json_str)
            return instance

        # deserialize data into PaymentMethodCashResponse
        try:
            instance.actual_instance = PaymentMethodCashResponse.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PaymentMethodCardResponse
        try:
            instance.actual_instance = PaymentMethodCardResponse.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PaymentMethodSpeiRecurrent
        try:
            instance.actual_instance = PaymentMethodSpeiRecurrent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into UpdateCustomerPaymentMethodsResponse with oneOf schemas: PaymentMethodCardResponse, PaymentMethodCashResponse, PaymentMethodSpeiRecurrent. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into UpdateCustomerPaymentMethodsResponse with oneOf schemas: PaymentMethodCardResponse, PaymentMethodCashResponse, PaymentMethodSpeiRecurrent. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        to_dict = getattr(self.actual_instance, "to_dict", None)
        if callable(to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())

