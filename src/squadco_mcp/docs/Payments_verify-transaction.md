# Source: https://docs.squadco.com/Payments/verify-transaction/

[Skip to main content](https://docs.squadco.com/Payments/verify-transaction/#__docusaurus_skipToContent_fallback)
[![My Site Logo](https://docs.squadco.com/img/squad_logo.svg)](https://docs.squadco.com/)
Search`K`
[Support](https://squadco.com/support/)[Create Account](https://dashboard.squadco.com/sign-up)[Sign In](https://dashboard.squadco.com/login)
  * [Home](https://docs.squadco.com/)
  * [Payments](https://docs.squadco.com/Payments/verify-transaction/)
    * [Payments](https://docs.squadco.com/Payments/overview)
    * [Initiate Payment](https://docs.squadco.com/Payments/Initiate-payment)
    * [Verify Transaction](https://docs.squadco.com/Payments/verify-transaction)
    * [Squad Payment Modal](https://docs.squadco.com/Payments/squad-payment-modal)
    * [Test Cards](https://docs.squadco.com/Payments/test-cards)
    * [Direct API Integration](https://docs.squadco.com/Payments/direct-api-integration)
    * [Direct Debit](https://docs.squadco.com/Payments/direct-debit)
    * [Squad Woo Commerce Plugin](https://docs.squadco.com/Payments/squad-woo-squad-plugin)
    * [Aggregator and Sub-merchants](https://docs.squadco.com/Payments/aggregator-and-sub-merchants)
    * [POS Remote Request](https://docs.squadco.com/Payments/pos-payment)
  * [Webhook & Redirect URL](https://docs.squadco.com/Payments/verify-transaction/)
  * [Virtual Accounts](https://docs.squadco.com/Payments/verify-transaction/)
  * [Transfer API](https://docs.squadco.com/Payments/verify-transaction/)
  * [Others](https://docs.squadco.com/Payments/verify-transaction/)
  * [Value Added Services (VAS)](https://docs.squadco.com/Payments/verify-transaction/)


  * [](https://docs.squadco.com/)
  * Payments
  * Verify Transaction


On this page
# Verify Transaction
This is an endpoint that allows you to query the status of a particular transaction using the unique transaction reference attached to the transaction.
**Environment base URL:**
**Test:** <https://sandbox-api-d.squadco.com>
**Production:** <https://api-d.squadco.com>
**Authorization** keys are to be passed via Headers as a Bearer token.
**Example:** Authorization: Bearer sandbox_sk_94f2b798466408ef4d19e848ee1a4d1a3e93f104046f.
### Response Data Object[​](https://docs.squadco.com/Payments/verify-transaction/#response-data-object "Direct link to Response Data Object")
The data object returned in the response is null when the status code is 400 and populated when the status code is 200.
The data object contains a parameter known as the transaction_status which differentiates the transaction type.
Transaction status can either be Success, Failed, Abandoned or Pending
GET
https://sandbox-api-d.squadco.com/transaction/verify/{{transaction_ref}}
### This verifies a transaction
To verify the validity of a transaction, kindly query the endpoint above by replacing {{transaction_ref}} with the unique transaction_ref of the transaction you want to verify
#### Parameters
##### Query
transaction_ref*
String
Unique transaction reference that identifies each transaction
#### Responses
200:OK
Valid Transaction Reference

```
{  
            "status": 200,  
            "success": true,  
            "message": "Success",  
            "data": {  
                "transaction_amount": 5000,  
                "transaction_ref": "SQCHIZ3634573076082",  
                "email": "ayo@gmail.com",  
                "transaction_status": "Success",  
                "transaction_currency_id": "NGN",  
                "created_at": "0001-01-01T00:00:00",  
                "transaction_type": "VirtualAccount",  
                "merchant_name": "CHIZOBA ANTHONY",  
                "merchant_business_name": null,  
                "gateway_transaction_ref": "SQCHIZ3634573076082",  
                "recurring": null,  
                "merchant_email": "okoyeanthonychizoba@gmail.com",  
                "plan_code": null  
            }  
}  

```

400:Bad Request
Invalid Transaction Reference

```
{  
            "status": 400,  
            "success": false,  
            "message": "Invalid transaction reference",  
            "data": {}  
}  

```

401:Unauthorized
Unauthorized Request

```
{  
            "success": false,  
            "message": "",  
            "data": {}  
}  

```

403:Forbidden
Invalid API Key

```
{  
            "success": false,  
            "message": "API key is invalid. Key must start with sandbox_sk_",  
            "data": {}  
}  

```

# Verify POS Transaction
To verify the validity of a POS transaction, kindly query the endpoint above, passing the transaction_reference as the value in the path variable
GET
https://api-d.squadco.com/softpos/transaction/verify/:transaction_reference
### This verifies a POS transaction
To verify the validity of a POS transaction, kindly query the endpoint above, passing the transaction_reference as the value in the path variable
#### Parameters
#### Responses
[](https://github.com/HabariPay/habaripay.github.io/tree/main/docs/Payments/verify-transaction.mdx)
[Previous Initiate Payment](https://docs.squadco.com/Payments/Initiate-payment)[Next Squad Payment Modal](https://docs.squadco.com/Payments/squad-payment-modal)
  * [Response Data Object](https://docs.squadco.com/Payments/verify-transaction/#response-data-object)


