# conekta
Conekta sdk

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2.1.0
- Package version: 6.0.0
- Build package: org.openapitools.codegen.languages.PythonNextgenClientCodegen
For more information, please visit [https://github.com/conekta/openapi/issues](https://github.com/conekta/openapi/issues)

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/conekta/conekta-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/conekta/conekta-python.git`)

Then import the package:
```python
import conekta
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import conekta
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import conekta
from conekta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.conekta.io
# See configuration.py for a list of all supported configuration parameters.
configuration = conekta.Configuration(
    host = "https://api.conekta.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = conekta.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)


# Enter a context with an instance of the API client
with conekta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = conekta.CustomersApi(api_client)
    customer = conekta.Customer(
        email='customer@customer.com',
        name='Customer Name',
        phone='5534343434'
    ) # Customer | requested field for create Customer
    accept_language = 'es' # str | Use for knowing which language to use (optional) (default to 'es')

    try:
        # Create Customer
        api_response = api_instance.create_customer(customer, accept_language=accept_language)
        print("The response of CustomersApi->create_customer:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CustomersApi->create_customer: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.conekta.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AntifraudApi* | [**create_rule_blacklist**](docs/AntifraudApi.md#create_rule_blacklist) | **POST** /antifraud/blacklists | Create blacklisted rule
*AntifraudApi* | [**create_rule_whitelist**](docs/AntifraudApi.md#create_rule_whitelist) | **POST** /antifraud/whitelists | Create whitelisted rule
*AntifraudApi* | [**delete_rule_blacklist**](docs/AntifraudApi.md#delete_rule_blacklist) | **DELETE** /antifraud/blacklists/{id} | Delete blacklisted rule
*AntifraudApi* | [**delete_rule_whitelist**](docs/AntifraudApi.md#delete_rule_whitelist) | **DELETE** /antifraud/whitelists/{id} | Delete whitelisted rule
*AntifraudApi* | [**get_rule_blacklist**](docs/AntifraudApi.md#get_rule_blacklist) | **GET** /antifraud/blacklists | Get list of blacklisted rules
*AntifraudApi* | [**get_rule_whitelist**](docs/AntifraudApi.md#get_rule_whitelist) | **GET** /antifraud/whitelists | Get a list of whitelisted rules
*ApiKeysApi* | [**create_api_key**](docs/ApiKeysApi.md#create_api_key) | **POST** /api_keys | Create Api Key
*ApiKeysApi* | [**delete_api_key**](docs/ApiKeysApi.md#delete_api_key) | **DELETE** /api_keys/{id} | Delete Api Key
*ApiKeysApi* | [**get_api_key**](docs/ApiKeysApi.md#get_api_key) | **GET** /api_keys/{id} | Get Api Key
*ApiKeysApi* | [**get_api_keys**](docs/ApiKeysApi.md#get_api_keys) | **GET** /api_keys | Get list of Api Keys
*ApiKeysApi* | [**update_api_key**](docs/ApiKeysApi.md#update_api_key) | **PUT** /api_keys/{id} | Update Api Key
*ChargesApi* | [**get_charges**](docs/ChargesApi.md#get_charges) | **GET** /charges | Get A List of Charges
*ChargesApi* | [**orders_create_charge**](docs/ChargesApi.md#orders_create_charge) | **POST** /orders/{id}/charges | Create charge
*CompaniesApi* | [**get_companies**](docs/CompaniesApi.md#get_companies) | **GET** /companies | Get List of Companies
*CompaniesApi* | [**get_company**](docs/CompaniesApi.md#get_company) | **GET** /companies/{id} | Get Company
*CustomersApi* | [**create_customer**](docs/CustomersApi.md#create_customer) | **POST** /customers | Create customer
*CustomersApi* | [**create_customer_fiscal_entities**](docs/CustomersApi.md#create_customer_fiscal_entities) | **POST** /customers/{id}/fiscal_entities | Create Fiscal Entity
*CustomersApi* | [**delete_customer_by_id**](docs/CustomersApi.md#delete_customer_by_id) | **DELETE** /customers/{id} | Delete Customer
*CustomersApi* | [**get_customer_by_id**](docs/CustomersApi.md#get_customer_by_id) | **GET** /customers/{id} | Get Customer
*CustomersApi* | [**get_customers**](docs/CustomersApi.md#get_customers) | **GET** /customers | Get a list of customers
*CustomersApi* | [**update_customer**](docs/CustomersApi.md#update_customer) | **PUT** /customers/{id} | Update customer
*CustomersApi* | [**update_customer_fiscal_entities**](docs/CustomersApi.md#update_customer_fiscal_entities) | **PUT** /customers/{id}/fiscal_entities/{fiscal_entities_id} | Update  Fiscal Entity
*DiscountsApi* | [**orders_create_discount_line**](docs/DiscountsApi.md#orders_create_discount_line) | **POST** /orders/{id}/discount_lines | Create Discount
*DiscountsApi* | [**orders_delete_discount_lines**](docs/DiscountsApi.md#orders_delete_discount_lines) | **DELETE** /orders/{id}/discount_lines/{discount_lines_id} | Delete Discount
*DiscountsApi* | [**orders_update_discount_lines**](docs/DiscountsApi.md#orders_update_discount_lines) | **PUT** /orders/{id}/discount_lines/{discount_lines_id} | Update Discount
*EventsApi* | [**get_event**](docs/EventsApi.md#get_event) | **GET** /events/{id} | Get Event
*EventsApi* | [**get_events**](docs/EventsApi.md#get_events) | **GET** /events | Get list of Events
*EventsApi* | [**resend_event**](docs/EventsApi.md#resend_event) | **POST** /events/{event_id}/webhook_logs/{webhook_log_id}/resend | Resend Event
*LogsApi* | [**get_log_by_id**](docs/LogsApi.md#get_log_by_id) | **GET** /logs/{id} | Get Log
*LogsApi* | [**get_logs**](docs/LogsApi.md#get_logs) | **GET** /logs | Get List Of Logs
*OrdersApi* | [**cancel_order**](docs/OrdersApi.md#cancel_order) | **POST** /orders/{id}/cancel | Cancel Order
*OrdersApi* | [**create_order**](docs/OrdersApi.md#create_order) | **POST** /orders | Create order
*OrdersApi* | [**get_order_by_id**](docs/OrdersApi.md#get_order_by_id) | **GET** /orders/{id} | Get Order
*OrdersApi* | [**get_orders**](docs/OrdersApi.md#get_orders) | **GET** /orders | Get a list of Orders
*OrdersApi* | [**order_cancel_refund**](docs/OrdersApi.md#order_cancel_refund) | **DELETE** /orders/{id}/refunds/{refund_id} | Cancel Refund
*OrdersApi* | [**order_refund**](docs/OrdersApi.md#order_refund) | **POST** /orders/{id}/refunds | Refund Order
*OrdersApi* | [**orders_create_capture**](docs/OrdersApi.md#orders_create_capture) | **POST** /orders/{id}/capture | Capture Order
*OrdersApi* | [**update_order**](docs/OrdersApi.md#update_order) | **PUT** /orders/{id} | Update Order
*PaymentLinkApi* | [**cancel_checkout**](docs/PaymentLinkApi.md#cancel_checkout) | **PUT** /checkouts/{id}/cancel | Cancel Payment Link
*PaymentLinkApi* | [**create_checkout**](docs/PaymentLinkApi.md#create_checkout) | **POST** /checkouts | Create Unique Payment Link
*PaymentLinkApi* | [**email_checkout**](docs/PaymentLinkApi.md#email_checkout) | **POST** /checkouts/{id}/email | Send an email
*PaymentLinkApi* | [**get_checkout**](docs/PaymentLinkApi.md#get_checkout) | **GET** /checkouts/{id} | Get a payment link by ID
*PaymentLinkApi* | [**get_checkouts**](docs/PaymentLinkApi.md#get_checkouts) | **GET** /checkouts | Get a list of payment links
*PaymentLinkApi* | [**sms_checkout**](docs/PaymentLinkApi.md#sms_checkout) | **POST** /checkouts/{id}/sms | Send an sms
*PaymentMethodsApi* | [**create_customer_payment_methods**](docs/PaymentMethodsApi.md#create_customer_payment_methods) | **POST** /customers/{id}/payment_sources | Create Payment Method
*PaymentMethodsApi* | [**delete_customer_payment_methods**](docs/PaymentMethodsApi.md#delete_customer_payment_methods) | **DELETE** /customers/{id}/payment_sources/{payment_method_id} | Delete Payment Method
*PaymentMethodsApi* | [**get_customer_payment_methods**](docs/PaymentMethodsApi.md#get_customer_payment_methods) | **GET** /customers/{id}/payment_sources | Get Payment Methods
*PaymentMethodsApi* | [**update_customer_payment_methods**](docs/PaymentMethodsApi.md#update_customer_payment_methods) | **PUT** /customers/{id}/payment_sources/{payment_method_id} | Update Payment Method
*PlansApi* | [**create_plan**](docs/PlansApi.md#create_plan) | **POST** /plans | Create Plan
*PlansApi* | [**delete_plan**](docs/PlansApi.md#delete_plan) | **DELETE** /plans/{id} | Delete Plan
*PlansApi* | [**get_plan**](docs/PlansApi.md#get_plan) | **GET** /plans/{id} | Get Plan
*PlansApi* | [**get_plans**](docs/PlansApi.md#get_plans) | **GET** /plans | Get A List of Plans
*PlansApi* | [**update_plan**](docs/PlansApi.md#update_plan) | **PUT** /plans/{id} | Update Plan
*ProductsApi* | [**orders_create_product**](docs/ProductsApi.md#orders_create_product) | **POST** /orders/{id}/line_items | Create Product
*ProductsApi* | [**orders_delete_product**](docs/ProductsApi.md#orders_delete_product) | **DELETE** /orders/{id}/line_items/{line_item_id} | Delete Product
*ProductsApi* | [**orders_update_product**](docs/ProductsApi.md#orders_update_product) | **PUT** /orders/{id}/line_items/{line_item_id} | Update Product
*ShippingContactsApi* | [**create_customer_shipping_contacts**](docs/ShippingContactsApi.md#create_customer_shipping_contacts) | **POST** /customers/{id}/shipping_contacts | Create a shipping contacts
*ShippingContactsApi* | [**delete_customer_shipping_contacts**](docs/ShippingContactsApi.md#delete_customer_shipping_contacts) | **DELETE** /customers/{id}/shipping_contacts/{shipping_contacts_id} | Delete shipping contacts
*ShippingContactsApi* | [**update_customer_shipping_contacts**](docs/ShippingContactsApi.md#update_customer_shipping_contacts) | **PUT** /customers/{id}/shipping_contacts/{shipping_contacts_id} | Update shipping contacts
*ShippingsApi* | [**orders_create_shipping**](docs/ShippingsApi.md#orders_create_shipping) | **POST** /orders/{id}/shipping_lines | Create Shipping
*ShippingsApi* | [**orders_delete_shipping**](docs/ShippingsApi.md#orders_delete_shipping) | **DELETE** /orders/{id}/shipping_lines/{shipping_id} | Delete Shipping
*ShippingsApi* | [**orders_update_shipping**](docs/ShippingsApi.md#orders_update_shipping) | **PUT** /orders/{id}/shipping_lines/{shipping_id} | Update Shipping
*SubscriptionsApi* | [**cancel_subscription**](docs/SubscriptionsApi.md#cancel_subscription) | **POST** /customers/{id}/subscription/cancel | Cancel Subscription
*SubscriptionsApi* | [**create_subscription**](docs/SubscriptionsApi.md#create_subscription) | **POST** /customers/{id}/subscription | Create Subscription
*SubscriptionsApi* | [**get_all_events_from_subscription**](docs/SubscriptionsApi.md#get_all_events_from_subscription) | **GET** /customers/{id}/subscription/events | Get Events By Subscription
*SubscriptionsApi* | [**get_subscription**](docs/SubscriptionsApi.md#get_subscription) | **GET** /customers/{id}/subscription | Get Subscription
*SubscriptionsApi* | [**pause_subscription**](docs/SubscriptionsApi.md#pause_subscription) | **POST** /customers/{id}/subscription/pause | Pause Subscription
*SubscriptionsApi* | [**resume_subscription**](docs/SubscriptionsApi.md#resume_subscription) | **POST** /customers/{id}/subscription/resume | Resume Subscription
*SubscriptionsApi* | [**update_subscription**](docs/SubscriptionsApi.md#update_subscription) | **PUT** /customers/{id}/subscription | Update Subscription
*TaxesApi* | [**orders_create_taxes**](docs/TaxesApi.md#orders_create_taxes) | **POST** /orders/{id}/tax_lines | Create Tax
*TaxesApi* | [**orders_delete_taxes**](docs/TaxesApi.md#orders_delete_taxes) | **DELETE** /orders/{id}/tax_lines/{tax_id} | Delete Tax
*TaxesApi* | [**orders_update_taxes**](docs/TaxesApi.md#orders_update_taxes) | **PUT** /orders/{id}/tax_lines/{tax_id} | Update Tax
*TokensApi* | [**create_token**](docs/TokensApi.md#create_token) | **POST** /tokens | Create Token
*TransactionsApi* | [**get_transaction**](docs/TransactionsApi.md#get_transaction) | **GET** /transactions/{id} | Get transaction
*TransactionsApi* | [**get_transactions**](docs/TransactionsApi.md#get_transactions) | **GET** /transactions | Get List transactions
*TransfersApi* | [**get_transfer**](docs/TransfersApi.md#get_transfer) | **GET** /transfers/{id} | Get Transfer
*TransfersApi* | [**get_transfers**](docs/TransfersApi.md#get_transfers) | **GET** /transfers | Get a list of transfers
*WebhookKeysApi* | [**create_webhook_key**](docs/WebhookKeysApi.md#create_webhook_key) | **POST** /webhook_keys | Create Webhook Key
*WebhookKeysApi* | [**delete_webhook_key**](docs/WebhookKeysApi.md#delete_webhook_key) | **DELETE** /webhook_keys/{id} | Delete Webhook key
*WebhookKeysApi* | [**get_webhook_key**](docs/WebhookKeysApi.md#get_webhook_key) | **GET** /webhook_keys/{id} | Get Webhook Key
*WebhookKeysApi* | [**get_webhook_keys**](docs/WebhookKeysApi.md#get_webhook_keys) | **GET** /webhook_keys | Get List of Webhook Keys
*WebhookKeysApi* | [**update_webhook_key**](docs/WebhookKeysApi.md#update_webhook_key) | **PUT** /webhook_keys/{id} | Update Webhook Key
*WebhooksApi* | [**create_webhook**](docs/WebhooksApi.md#create_webhook) | **POST** /webhooks | Create Webhook
*WebhooksApi* | [**delete_webhook**](docs/WebhooksApi.md#delete_webhook) | **DELETE** /webhooks/{id} | Delete Webhook
*WebhooksApi* | [**get_webhook**](docs/WebhooksApi.md#get_webhook) | **GET** /webhooks/{id} | Get Webhook
*WebhooksApi* | [**get_webhooks**](docs/WebhooksApi.md#get_webhooks) | **GET** /webhooks | Get List of Webhooks
*WebhooksApi* | [**test_webhook**](docs/WebhooksApi.md#test_webhook) | **POST** /webhooks/{id}/test | Test Webhook
*WebhooksApi* | [**update_webhook**](docs/WebhooksApi.md#update_webhook) | **PUT** /webhooks/{id} | Update Webhook


## Documentation For Models

 - [ApiKeyCreateResponse](docs/ApiKeyCreateResponse.md)
 - [ApiKeyCreateResponseAllOf](docs/ApiKeyCreateResponseAllOf.md)
 - [ApiKeyRequest](docs/ApiKeyRequest.md)
 - [ApiKeyResponse](docs/ApiKeyResponse.md)
 - [ApiKeyUpdateRequest](docs/ApiKeyUpdateRequest.md)
 - [BlacklistRuleResponse](docs/BlacklistRuleResponse.md)
 - [ChargeDataPaymentMethodBankTransferResponse](docs/ChargeDataPaymentMethodBankTransferResponse.md)
 - [ChargeDataPaymentMethodCardResponse](docs/ChargeDataPaymentMethodCardResponse.md)
 - [ChargeDataPaymentMethodCashResponse](docs/ChargeDataPaymentMethodCashResponse.md)
 - [ChargeOrderResponse](docs/ChargeOrderResponse.md)
 - [ChargeOrderResponsePaymentMethod](docs/ChargeOrderResponsePaymentMethod.md)
 - [ChargeRequest](docs/ChargeRequest.md)
 - [ChargeRequestPaymentMethod](docs/ChargeRequestPaymentMethod.md)
 - [ChargeResponse](docs/ChargeResponse.md)
 - [ChargeResponseChannel](docs/ChargeResponseChannel.md)
 - [ChargeResponsePaymentMethod](docs/ChargeResponsePaymentMethod.md)
 - [ChargeResponseRefunds](docs/ChargeResponseRefunds.md)
 - [ChargeResponseRefundsAllOf](docs/ChargeResponseRefundsAllOf.md)
 - [ChargeResponseRefundsData](docs/ChargeResponseRefundsData.md)
 - [ChargesDataResponse](docs/ChargesDataResponse.md)
 - [Checkout](docs/Checkout.md)
 - [CheckoutOrderTemplate](docs/CheckoutOrderTemplate.md)
 - [CheckoutOrderTemplateCustomerInfo](docs/CheckoutOrderTemplateCustomerInfo.md)
 - [CheckoutRequest](docs/CheckoutRequest.md)
 - [CheckoutResponse](docs/CheckoutResponse.md)
 - [CheckoutsResponse](docs/CheckoutsResponse.md)
 - [CheckoutsResponseAllOf](docs/CheckoutsResponseAllOf.md)
 - [CompanyFiscalInfoAddressResponse](docs/CompanyFiscalInfoAddressResponse.md)
 - [CompanyFiscalInfoResponse](docs/CompanyFiscalInfoResponse.md)
 - [CompanyPayoutDestinationResponse](docs/CompanyPayoutDestinationResponse.md)
 - [CompanyResponse](docs/CompanyResponse.md)
 - [CreateCustomerFiscalEntitiesResponse](docs/CreateCustomerFiscalEntitiesResponse.md)
 - [CreateCustomerFiscalEntitiesResponseAllOf](docs/CreateCustomerFiscalEntitiesResponseAllOf.md)
 - [CreateCustomerPaymentMethodsRequest](docs/CreateCustomerPaymentMethodsRequest.md)
 - [CreateCustomerPaymentMethodsResponse](docs/CreateCustomerPaymentMethodsResponse.md)
 - [CreateRiskRulesData](docs/CreateRiskRulesData.md)
 - [Customer](docs/Customer.md)
 - [CustomerAddress](docs/CustomerAddress.md)
 - [CustomerAntifraudInfo](docs/CustomerAntifraudInfo.md)
 - [CustomerAntifraudInfoResponse](docs/CustomerAntifraudInfoResponse.md)
 - [CustomerFiscalEntitiesDataResponse](docs/CustomerFiscalEntitiesDataResponse.md)
 - [CustomerFiscalEntitiesRequest](docs/CustomerFiscalEntitiesRequest.md)
 - [CustomerFiscalEntitiesRequestAddress](docs/CustomerFiscalEntitiesRequestAddress.md)
 - [CustomerFiscalEntitiesResponse](docs/CustomerFiscalEntitiesResponse.md)
 - [CustomerFiscalEntitiesResponseAllOf](docs/CustomerFiscalEntitiesResponseAllOf.md)
 - [CustomerInfo](docs/CustomerInfo.md)
 - [CustomerInfoJustCustomerId](docs/CustomerInfoJustCustomerId.md)
 - [CustomerInfoJustCustomerIdResponse](docs/CustomerInfoJustCustomerIdResponse.md)
 - [CustomerInfoResponse](docs/CustomerInfoResponse.md)
 - [CustomerPaymentMethodRequest](docs/CustomerPaymentMethodRequest.md)
 - [CustomerPaymentMethods](docs/CustomerPaymentMethods.md)
 - [CustomerPaymentMethodsData](docs/CustomerPaymentMethodsData.md)
 - [CustomerPaymentMethodsRequest](docs/CustomerPaymentMethodsRequest.md)
 - [CustomerPaymentMethodsResponse](docs/CustomerPaymentMethodsResponse.md)
 - [CustomerResponse](docs/CustomerResponse.md)
 - [CustomerResponseShippingContacts](docs/CustomerResponseShippingContacts.md)
 - [CustomerResponseShippingContactsAllOf](docs/CustomerResponseShippingContactsAllOf.md)
 - [CustomerShippingContacts](docs/CustomerShippingContacts.md)
 - [CustomerShippingContactsAddress](docs/CustomerShippingContactsAddress.md)
 - [CustomerShippingContactsDataResponse](docs/CustomerShippingContactsDataResponse.md)
 - [CustomerShippingContactsDataResponseAllOf](docs/CustomerShippingContactsDataResponseAllOf.md)
 - [CustomerShippingContactsResponse](docs/CustomerShippingContactsResponse.md)
 - [CustomerShippingContactsResponseAddress](docs/CustomerShippingContactsResponseAddress.md)
 - [CustomerUpdateFiscalEntitiesRequest](docs/CustomerUpdateFiscalEntitiesRequest.md)
 - [CustomerUpdateShippingContacts](docs/CustomerUpdateShippingContacts.md)
 - [CustomersResponse](docs/CustomersResponse.md)
 - [CustomersResponseAllOf](docs/CustomersResponseAllOf.md)
 - [DeleteApiKeysResponse](docs/DeleteApiKeysResponse.md)
 - [DeleteApiKeysResponseAllOf](docs/DeleteApiKeysResponseAllOf.md)
 - [DeletedBlacklistRuleResponse](docs/DeletedBlacklistRuleResponse.md)
 - [DeletedWhitelistRuleResponse](docs/DeletedWhitelistRuleResponse.md)
 - [Details](docs/Details.md)
 - [DetailsError](docs/DetailsError.md)
 - [DiscountLinesDataResponse](docs/DiscountLinesDataResponse.md)
 - [DiscountLinesResponse](docs/DiscountLinesResponse.md)
 - [DiscountLinesResponseAllOf](docs/DiscountLinesResponseAllOf.md)
 - [EmailCheckoutRequest](docs/EmailCheckoutRequest.md)
 - [Error](docs/Error.md)
 - [ErrorAllOf](docs/ErrorAllOf.md)
 - [EventResponse](docs/EventResponse.md)
 - [EventsResendResponse](docs/EventsResendResponse.md)
 - [GetApiKeysResponse](docs/GetApiKeysResponse.md)
 - [GetApiKeysResponseAllOf](docs/GetApiKeysResponseAllOf.md)
 - [GetChargesResponse](docs/GetChargesResponse.md)
 - [GetChargesResponseAllOf](docs/GetChargesResponseAllOf.md)
 - [GetCompaniesResponse](docs/GetCompaniesResponse.md)
 - [GetCompaniesResponseAllOf](docs/GetCompaniesResponseAllOf.md)
 - [GetCustomerPaymentMethodDataResponse](docs/GetCustomerPaymentMethodDataResponse.md)
 - [GetEventsResponse](docs/GetEventsResponse.md)
 - [GetEventsResponseAllOf](docs/GetEventsResponseAllOf.md)
 - [GetOrdersResponse](docs/GetOrdersResponse.md)
 - [GetPaymentMethodResponse](docs/GetPaymentMethodResponse.md)
 - [GetPaymentMethodResponseAllOf](docs/GetPaymentMethodResponseAllOf.md)
 - [GetPlansResponse](docs/GetPlansResponse.md)
 - [GetPlansResponseAllOf](docs/GetPlansResponseAllOf.md)
 - [GetTransactionsResponse](docs/GetTransactionsResponse.md)
 - [GetTransactionsResponseAllOf](docs/GetTransactionsResponseAllOf.md)
 - [GetTransfersResponse](docs/GetTransfersResponse.md)
 - [GetTransfersResponseAllOf](docs/GetTransfersResponseAllOf.md)
 - [GetWebhookKeysResponse](docs/GetWebhookKeysResponse.md)
 - [GetWebhookKeysResponseAllOf](docs/GetWebhookKeysResponseAllOf.md)
 - [GetWebhooksResponse](docs/GetWebhooksResponse.md)
 - [GetWebhooksResponseAllOf](docs/GetWebhooksResponseAllOf.md)
 - [LogResponse](docs/LogResponse.md)
 - [LogsResponse](docs/LogsResponse.md)
 - [LogsResponseData](docs/LogsResponseData.md)
 - [OrderCaptureRequest](docs/OrderCaptureRequest.md)
 - [OrderDiscountLinesRequest](docs/OrderDiscountLinesRequest.md)
 - [OrderRefundRequest](docs/OrderRefundRequest.md)
 - [OrderRequest](docs/OrderRequest.md)
 - [OrderRequestCustomerInfo](docs/OrderRequestCustomerInfo.md)
 - [OrderResponse](docs/OrderResponse.md)
 - [OrderResponseCharges](docs/OrderResponseCharges.md)
 - [OrderResponseChargesAllOf](docs/OrderResponseChargesAllOf.md)
 - [OrderResponseCheckout](docs/OrderResponseCheckout.md)
 - [OrderResponseCustomerInfo](docs/OrderResponseCustomerInfo.md)
 - [OrderResponseCustomerInfoAllOf](docs/OrderResponseCustomerInfoAllOf.md)
 - [OrderResponseDiscountLines](docs/OrderResponseDiscountLines.md)
 - [OrderResponseDiscountLinesAllOf](docs/OrderResponseDiscountLinesAllOf.md)
 - [OrderResponseFiscalEntity](docs/OrderResponseFiscalEntity.md)
 - [OrderResponseFiscalEntityAddress](docs/OrderResponseFiscalEntityAddress.md)
 - [OrderResponseFiscalEntityAddressAllOf](docs/OrderResponseFiscalEntityAddressAllOf.md)
 - [OrderResponseProducts](docs/OrderResponseProducts.md)
 - [OrderResponseProductsAllOf](docs/OrderResponseProductsAllOf.md)
 - [OrderResponseShippingContact](docs/OrderResponseShippingContact.md)
 - [OrderResponseShippingContactAllOf](docs/OrderResponseShippingContactAllOf.md)
 - [OrderTaxRequest](docs/OrderTaxRequest.md)
 - [OrderUpdateRequest](docs/OrderUpdateRequest.md)
 - [OrdersResponse](docs/OrdersResponse.md)
 - [Page](docs/Page.md)
 - [Pagination](docs/Pagination.md)
 - [PaymentMethod](docs/PaymentMethod.md)
 - [PaymentMethodBankTransfer](docs/PaymentMethodBankTransfer.md)
 - [PaymentMethodCard](docs/PaymentMethodCard.md)
 - [PaymentMethodCardRequest](docs/PaymentMethodCardRequest.md)
 - [PaymentMethodCardRequestAllOf](docs/PaymentMethodCardRequestAllOf.md)
 - [PaymentMethodCardResponse](docs/PaymentMethodCardResponse.md)
 - [PaymentMethodCardResponseAllOf](docs/PaymentMethodCardResponseAllOf.md)
 - [PaymentMethodCash](docs/PaymentMethodCash.md)
 - [PaymentMethodCashRequest](docs/PaymentMethodCashRequest.md)
 - [PaymentMethodCashRequestAllOf](docs/PaymentMethodCashRequestAllOf.md)
 - [PaymentMethodCashResponse](docs/PaymentMethodCashResponse.md)
 - [PaymentMethodCashResponseAllOf](docs/PaymentMethodCashResponseAllOf.md)
 - [PaymentMethodResponse](docs/PaymentMethodResponse.md)
 - [PaymentMethodSpeiRecurrent](docs/PaymentMethodSpeiRecurrent.md)
 - [PaymentMethodSpeiRecurrentAllOf](docs/PaymentMethodSpeiRecurrentAllOf.md)
 - [PaymentMethodSpeiRequest](docs/PaymentMethodSpeiRequest.md)
 - [PlanRequest](docs/PlanRequest.md)
 - [PlanResponse](docs/PlanResponse.md)
 - [PlanUpdateRequest](docs/PlanUpdateRequest.md)
 - [Product](docs/Product.md)
 - [ProductDataResponse](docs/ProductDataResponse.md)
 - [ProductDataResponseAllOf](docs/ProductDataResponseAllOf.md)
 - [ProductOrderResponse](docs/ProductOrderResponse.md)
 - [ProductOrderResponseAllOf](docs/ProductOrderResponseAllOf.md)
 - [RiskRules](docs/RiskRules.md)
 - [RiskRulesData](docs/RiskRulesData.md)
 - [RiskRulesList](docs/RiskRulesList.md)
 - [ShippingOrderResponse](docs/ShippingOrderResponse.md)
 - [ShippingRequest](docs/ShippingRequest.md)
 - [SmsCheckoutRequest](docs/SmsCheckoutRequest.md)
 - [SubscriptionEventsResponse](docs/SubscriptionEventsResponse.md)
 - [SubscriptionRequest](docs/SubscriptionRequest.md)
 - [SubscriptionResponse](docs/SubscriptionResponse.md)
 - [SubscriptionUpdateRequest](docs/SubscriptionUpdateRequest.md)
 - [Token](docs/Token.md)
 - [TokenCard](docs/TokenCard.md)
 - [TokenCheckout](docs/TokenCheckout.md)
 - [TokenResponse](docs/TokenResponse.md)
 - [TokenResponseCheckout](docs/TokenResponseCheckout.md)
 - [TransactionResponse](docs/TransactionResponse.md)
 - [TransferDestinationResponse](docs/TransferDestinationResponse.md)
 - [TransferMethodResponse](docs/TransferMethodResponse.md)
 - [TransferResponse](docs/TransferResponse.md)
 - [TransfersResponse](docs/TransfersResponse.md)
 - [UpdateCustomer](docs/UpdateCustomer.md)
 - [UpdateCustomerAntifraudInfo](docs/UpdateCustomerAntifraudInfo.md)
 - [UpdateCustomerFiscalEntitiesResponse](docs/UpdateCustomerFiscalEntitiesResponse.md)
 - [UpdateCustomerFiscalEntitiesResponseAllOf](docs/UpdateCustomerFiscalEntitiesResponseAllOf.md)
 - [UpdateCustomerPaymentMethodsResponse](docs/UpdateCustomerPaymentMethodsResponse.md)
 - [UpdateOrderDiscountLinesRequest](docs/UpdateOrderDiscountLinesRequest.md)
 - [UpdateOrderTaxRequest](docs/UpdateOrderTaxRequest.md)
 - [UpdateOrderTaxResponse](docs/UpdateOrderTaxResponse.md)
 - [UpdateOrderTaxResponseAllOf](docs/UpdateOrderTaxResponseAllOf.md)
 - [UpdatePaymentMethods](docs/UpdatePaymentMethods.md)
 - [UpdateProduct](docs/UpdateProduct.md)
 - [WebhookKeyCreateResponse](docs/WebhookKeyCreateResponse.md)
 - [WebhookKeyDeleteResponse](docs/WebhookKeyDeleteResponse.md)
 - [WebhookKeyRequest](docs/WebhookKeyRequest.md)
 - [WebhookKeyResponse](docs/WebhookKeyResponse.md)
 - [WebhookKeyUpdateRequest](docs/WebhookKeyUpdateRequest.md)
 - [WebhookLog](docs/WebhookLog.md)
 - [WebhookRequest](docs/WebhookRequest.md)
 - [WebhookResponse](docs/WebhookResponse.md)
 - [WebhookUpdateRequest](docs/WebhookUpdateRequest.md)
 - [WhitelistlistRuleResponse](docs/WhitelistlistRuleResponse.md)

<a id="documentation-for-authorization"></a>
## Documentation For Authorization


## bearerAuth

- **Type**: Bearer authentication


## Author

engineering@conekta.com

