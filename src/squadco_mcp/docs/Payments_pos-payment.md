# Source: https://docs.squadco.com/Payments/pos-payment/

[Skip to main content](https://docs.squadco.com/Payments/pos-payment/#__docusaurus_skipToContent_fallback)
[![My Site Logo](https://docs.squadco.com/img/squad_logo.svg)](https://docs.squadco.com/)
Search`K`
[Support](https://squadco.com/support/)[Create Account](https://dashboard.squadco.com/sign-up)[Sign In](https://dashboard.squadco.com/login)
  * [Home](https://docs.squadco.com/)
  * [Payments](https://docs.squadco.com/Payments/pos-payment/)
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
  * [Webhook & Redirect URL](https://docs.squadco.com/Payments/pos-payment/)
  * [Virtual Accounts](https://docs.squadco.com/Payments/pos-payment/)
  * [Transfer API](https://docs.squadco.com/Payments/pos-payment/)
  * [Others](https://docs.squadco.com/Payments/pos-payment/)
  * [Value Added Services (VAS)](https://docs.squadco.com/Payments/pos-payment/)


  * [](https://docs.squadco.com/)
  * Payments
  * POS Remote Request


On this page
# POS Remote Request
##### The POS Remote Request suite of APIs allows you to remotely invoke a payment on a POS terminal and requery for the status of the transaction.[​](https://docs.squadco.com/Payments/pos-payment/#the-pos-remote-request-suite-of-apis-allows-you-to-remotely-invoke-a-payment-on-a-pos-terminal-and-requery-for-the-status-of-the-transaction "Direct link to The POS Remote Request suite of APIs allows you to remotely invoke a payment on a POS terminal and requery for the status of the transaction.")
**Environment base URL:**
**Base URL:** <https://api-d.squadco.com/softpos/>
**Authorization** keys are to be passed via Headers as a Bearer token.
**Example:** Authorization: Bearer sandbox_sk_94f2b798466408ef4d19e848ee1a4d1a3e93f104046f.
### Create Payment Request[​](https://docs.squadco.com/Payments/pos-payment/#create-payment-request "Direct link to Create Payment Request")
This endpoint enables you to send a payment request to a POS terminal. The terminal receives the request and processes the card payment.
POST
https://api-d.squadco.com/softpos/pos/remote-request
This endpoint allows you send a payment to a POS terminal.
#### Parameters
##### Header
Authorization*
String
API keys (Secret Key) that authorize your transactions and gotten from your squad dashboard
##### Body
terminal_id*
String
The ID of the POS terminal to invoke
amount*
Number
Amount to charge (in kobo). Must be greater than 0
account_type*
String
Account type: default, savings, current, or credit
#### Sample POS Remote Request[​](https://docs.squadco.com/Payments/pos-payment/#sample-pos-remote-request "Direct link to Sample POS Remote Request")

```
{  
  "terminal_id": "2035AB01",  
  "amount": 350000,  
  "account_type": "default"  
}  

```

#### Responses
200:OK
Successful

```
{  
  "status": 200,  
  "success": true,  
  "message": "Payment request created",  
  "data": {  
    "request_ref": "prq_01HV8M3K5R7XM6QEGG1YAEVF"  
  }  
}  
  

```

400:Validation Error
Validation Error

```
{  
    "status": "400",  
    "message": "Validation error (missing fields, invalid amount)",  
    "data": {}  
  }  

```

401:Invalid Token
Invalid Token

```
{  
    "status": "401",  
    "message": "Invalid or missing token",  
    "data": {}  
  }  

```

### Requery Payment Status[​](https://docs.squadco.com/Payments/pos-payment/#requery-payment-status "Direct link to Requery Payment Status")
This endpoint allows you to requery the terminal using the request reference to confirm if payment is completed or not.
GET
https://api-d.squadco.com/softpos/pos/remote-request/{request_ref}
This endpoint allows you requery the status of a request
#### Parameters
##### Header
Authorization*
String
API keys (Secret Key) that authorize your transactions and gotten from your squad dashboard
##### Body
request_ref*
String
The reference returned from the create endpoint
#### Sample Request[​](https://docs.squadco.com/Payments/pos-payment/#sample-request "Direct link to Sample Request")

```
GET https://api-d.squadco.com/softpos/pos/remote-request/prq_01HV8M3K5R7XM6QEGG1YAEVF  

```

#### Responses
200 Success
Success

```
{  
  "status": 200,  
  "success": true,  
  "message": "Success",  
  "data": {  
    "status": "success",  
    "id": 12345,  
    "merchant_request_ref": "prq_01HV8M3K5R7XM6QEGG1YAEVF",  
    "merchant_id": "MER_001",  
    "terminal_id": "2035AB01",  
    "amount": 350000,  
    "currency": "NGN",  
    "payment_method": "card",  
    "transaction_type": "Purchase",  
    "payment_info": {  
      "card_pan": "506100******1234",  
      "card_exp": "2512",  
      "card_type": "visa",  
      "cardholder_name": "JOHN DOE"  
    },  
    "transaction_reference": "TXN_REF_001",  
    "virtual_account_number": null,  
    "rrn": "123456789012",  
    "stan": "019283",  
    "aid": "A0000000041010",  
    "response_code": "00",  
    "response_message": "Approved",  
    "processor": null,  
    "meta": "{}",  
    "pc_code": "PC001",  
    "created_at": "2026-02-20T09:15:48.901Z"  
  }  
}  
  

```

200 Pending
Success

```
{  
  "status": 200,  
  "success": true,  
  "message": "Success",  
  "data": {  
    "status": "pending"  
  }  
}  

```

200 Failed
Success

```
{  
  "status": 200,  
  "success": true,  
  "message": "Success",  
  "data": {  
    "status": "failed",  
    "id": 12345,  
    "merchant_request_ref": "prq_01HV8M3K5R7XM6QEGG1YAEVF",  
    "merchant_id": "MER_001",  
    "terminal_id": "2035AB01",  
    "amount": 350000,  
    "currency": "NGN",  
    "payment_method": "card",  
    "transaction_type": "Purchase",  
    "payment_info": {  
      "card_pan": "506100******1234",  
      "card_exp": "2512",  
      "card_type": "visa",  
      "cardholder_name": "JOHN DOE"  
    },  
    "transaction_reference": "TXN_REF_002",  
    "virtual_account_number": null,  
    "rrn": "123456789013",  
    "stan": "019284",  
    "aid": "A0000000041010",  
    "response_code": "51",  
    "response_message": "Insufficient funds",  
    "processor": null,  
    "meta": "{}",  
    "pc_code": "PC001",  
    "created_at": "2026-02-20T09:15:48.901Z"  
  }  
}  

```

404 Expired/Not Found
false

```
{  
  "status": 404,  
  "success": false,  
  "message": "Request not found or expired",  
  "data": {}  
}  
  

```

401:Invalid Token
Invalid Token

```
{  
    "status": "401",  
    "message": "Invalid or missing token",  
    "data": {}  
  }  

```

**Response — Expired / Not Found (404)** Returned when the request_ref does not exist or has expired. Payment requests are stored with a 5-minute Time To Live (TTL). Once the TTL expires, the record is automatically deleted, as such the system returns a 404 response. Which can mean:
i.The request_ref was never valid
ii.The request expired because the POS terminal did not complete the payment within 5 minutes
The request_ref expires after 5 minutes.
If the terminal does not process the payment within that window, requery will return 404.
Call the requery endpoint every 2-3 seconds until you get a final status (success or failed) or a 404.
When status is pending, only status is returned. When success or failed, the full transaction fields are flattened into the response.
### POS Webhook[​](https://docs.squadco.com/Payments/pos-payment/#pos-webhook "Direct link to POS Webhook")
POS Merchants can now recive webhook notifications sent directly from their terminals to their systems.
  1. Login to Squad Dashboard
  2. Go to API and Webhook under Merchant Settings
  3. Scroll Down and input endpoint to recieve the notification in the Webhook URL tab
  4. Click Save Changes


Once done, any successful payment made to the terminal will be automatcally fired to the webhook url.
#### Sample webhook for webhook notifications (From POS to merchant system)[​](https://docs.squadco.com/Payments/pos-payment/#sample-webhook-for-webhook-notifications-from-pos-to-merchant-system "Direct link to Sample webhook for webhook notifications \(From POS to merchant system\)")

```
{  
  "amount": 1000,  
  "merchant_id": "AABBCCDDEEFFGGHHJJKK",  
  "payment_info": {  
    "card_pan": "539983****5128",  
    "card_type": "MasterCard",  
    "cardholder_name": "MARTINS OLARINDE"  
  },  
  "status": "success",  
  "payment_method": "card",  
  "transaction_type": "Purchase",  
  "response_code": "00",  
  "transaction_reference": "SQDEMO080830159201",  
  "terminal_id": "2058ZUTK",  
  "response_message": "Transaction Successful",  
  "rrn": "080830159201",  
  "stan": "159201",  
  "currency": "NGN",  
  "aid": "4F07A0000000041010",  
  "merchant_request_ref": null,  
  "updated_at": "2026-05-05T13:47:22.458Z",  
  "created_at": "2026-05-05T13:47:22.458Z",  
  "virtual_account_number": null,  
  "receipt_no": "0025145374",  
  "settlement_type": "normal",  
  "instant_settlement_account_no": null,  
  "mcc": {  
    "mcc_code": "5411",  
    "percentage_charge": 0.5,  
    "capped_at_kobo": 100000  
  }  
}  

```

[](https://github.com/HabariPay/habaripay.github.io/tree/main/docs/Payments/pos-payment.mdx)
[Previous Aggregator and Sub-merchants](https://docs.squadco.com/Payments/aggregator-and-sub-merchants)[Next Webhook & Redirect URL](https://docs.squadco.com/webhook-direct-url/webhook-and-direct-url)
  * [Create Payment Request](https://docs.squadco.com/Payments/pos-payment/#create-payment-request)
  * [Requery Payment Status](https://docs.squadco.com/Payments/pos-payment/#requery-payment-status)
  * [POS Webhook](https://docs.squadco.com/Payments/pos-payment/#pos-webhook)


