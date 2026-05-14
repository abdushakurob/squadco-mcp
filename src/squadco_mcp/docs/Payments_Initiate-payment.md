# Source: https://docs.squadco.com/Payments/Initiate-payment/

[Skip to main content](https://docs.squadco.com/Payments/Initiate-payment/#__docusaurus_skipToContent_fallback)
[![My Site Logo](https://docs.squadco.com/img/squad_logo.svg)](https://docs.squadco.com/)
Search`K`
[Support](https://squadco.com/support/)[Create Account](https://dashboard.squadco.com/sign-up)[Sign In](https://dashboard.squadco.com/login)
  * [Home](https://docs.squadco.com/)
  * [Payments](https://docs.squadco.com/Payments/Initiate-payment/)
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
  * [Webhook & Redirect URL](https://docs.squadco.com/Payments/Initiate-payment/)
  * [Virtual Accounts](https://docs.squadco.com/Payments/Initiate-payment/)
  * [Transfer API](https://docs.squadco.com/Payments/Initiate-payment/)
  * [Others](https://docs.squadco.com/Payments/Initiate-payment/)
  * [Value Added Services (VAS)](https://docs.squadco.com/Payments/Initiate-payment/)


  * [](https://docs.squadco.com/)
  * Payments
  * Initiate Payment


On this page
# Initiate Payment
##### This API lets you initiate transactions by making server calls that return a checkout URL. When visited, this URL will display our payment modal.[​](https://docs.squadco.com/Payments/Initiate-payment/#this-api-lets-you-initiate-transactions-by-making-server-calls-that-return-a-checkout-url-when-visited-this-url-will-display-our-payment-modal "Direct link to This API lets you initiate transactions by making server calls that return a checkout URL. When visited, this URL will display our payment modal.")
**Environment base URL:**
**Test:** <https://sandbox-api-d.squadco.com>
**Production:** <https://api-d.squadco.com>
**Authorization** keys are to be passed via Headers as a Bearer token.
**Example:** Authorization: Bearer sandbox_sk_94f2b798466408ef4d19e848ee1a4d1a3e93f104046f.
**The transaction reference used to initiate transactions must be unique.**
POST
sandbox-api.squadco.com/transaction/Initiate
cURL
#### Enter Payment details
Help us send transactions receipts to the customers
Charge Amount (₦)
Customer Email Address
Merchant key
Send Request

```
  
  curl --location 'https://sandbox-api.squadco.com/transaction/initiate'   
  --header 'Authorization: 47M3DMZD'  
  --header 'Content-Type: application/json'  
  --data-raw '{  
    "amount":_ ,  
    "email":_ ,  
    "key":_ ,  
      "currency":"NGN",  
      "initiate_type": "inline",  
      "CallBack_URL" : "https://www.linkedin.com/",  
  }  
  

```

POST
https://sandbox-api-d.squadco.com/transaction/initiate
This endpoint returns a checkout URL that when visited calls up the modal with the various payment channel.
#### Parameters
##### Header
Authorization*
String
API keys (Secret Key) that authorize your transactions and gotten from your squad dashboard
##### Body
email*
String
Customer's email address.
amount*
String
The amount you are debiting customer (expressed in the lowest currency value - kobo& cent). 10000 = 100NGN for Naira Transactions
initiate_type*
String
This states the method by which the transaction is initiated. At the moment, this can only take the value 'inline'.
currency*
String
The currency you want the amount to be charged in. Allowed value is either NGN or USD.
transaction_ref*
String
The merchant defined reference, unique for each transaction (where none is passed, a system-generated reference will be created)
customer_name*
String
Name of Customer carrying out the transaction
callback_url*
String
A web address where customers are redirected after payment completion (This differs from the URL where webhook notifications are sent).
payment_channels*
Array
An array of payment channels to control what channels you want to make available for the user to make a payment with. Available channels include; ['card', 'bank' , 'ussd','transfer']
metadata*
Object
Object that contains any additional information that you want to record with the transaction. The custom fields in the object will be returned via webhook and the payment verification endpoint.
pass_charge*
Boolean
It takes two possible values: True or False. It is set to False by default. When set to True, the charges on the transaction is computed and passed on to the customer(payer). But when set to False, the charge is passed to the merchant and will be deducted from the amount to be settled to the merchant.
sub_merchant_id*
String
This is the ID of a meerchant that was created by an aggregator which allows the aggregator initiate a transaction on behalf of the submerchant. This parameter is an optional field that is passed only by a registered aggregator
#### Responses
200:OK
Successful

```
{  
    "status": 200,  
    "message": "success",  
    "data": {  
        "auth_url": null,  
        "access_token": null,  
        "merchant_info": {  
            "merchant_response": null,  
            "merchant_name": null,  
            "merchant_logo": null,  
            "merchant_id": "SBN1EBZEQ8"  
        },  
        "currency": "NGN",  
        "recurring": {  
            "frequency": null,  
            "duration": null,  
            "type": 0,  
            "plan_code": null,  
            "customer_name": null  
        },  
        "is_recurring": false,  
        "plan_code": null,  
        "callback_url": "http://squadco.com",  
        "transaction_ref": "4678388588350909090AH",  
        "transaction_memo": null,  
        "transaction_amount": 43000,  
        "authorized_channels": [  
            "card",  
            "ussd",  
            "bank"  
        ],  
        "checkout_url": "https://sandbox-pay.squadco.com/4678388588350909090AH"  
    }  
}  

```

401:Unauthorized
Invalid/No Authorization Key

```
{  
            "status": 401,  
            "message": "Initiate transaction Unauthorized",  
            "data": null  
}  

```

400:Bad Request
Bad Request

```
{  
    "status": 400,  
    "success": false,  
    "message": "email" is required",  
    "data": {}  
}  

```

### Sample Request[​](https://docs.squadco.com/Payments/Initiate-payment/#sample-request "Direct link to Sample Request")

```
{  
    "amount":43000,  
    "email":"henimastic@gmail.com",  
    "currency":"NGN",  
    "initiate_type": "inline",  
    "transaction_ref":"4678388588350909090AH",  
    "callback_url":"http://squadco.com"  
}  

```

### Simulate Test Payment (Transfer)[​](https://docs.squadco.com/Payments/Initiate-payment/#simulate-test-payment-transfer "Direct link to Simulate Test Payment \(Transfer\)")
In the test environment, when the transfer option is selected on the payment modal, a dynamic virtual account is created. To complete the transaction, a simulated payment is required. This API allows you to simulate a payment into the dynamic virtual account.
POST
https://sandbox-api-d.squadco.com/virtual-account/simulate/payment
This endpoint allows you simualte payment into an account
#### Parameters
##### Header
Authorization*
String
API keys (Secret Key) that authorize your transactions and gotten from your squad dashboard
##### Body
virtual_account_number*
Integer
Generated Dynamic Virtual Account from the Transfer modal
amount*
Integer
The amount to be paid
#### Responses
200:OK
Successful

```
{  
      
    "status": 200,  
    "success": true,  
    "message": "Success",  
    "data": "Payment successful"  
}  

```

400:Bad Request
Bad Request

```
{  
    "status": "400",  
    "success": false,  
    "message": ""amount" is required",  
    "data": {}  
  }  

```

### Sample Request Simulate Payment[​](https://docs.squadco.com/Payments/Initiate-payment/#sample-request-simulate-payment "Direct link to Sample Request Simulate Payment")

```
{  
    "virtual_account_number": "9279755518",  
    "amount": "20000"  
}  

```

### Recurring Payment (Charge Authorization on Card)[​](https://docs.squadco.com/Payments/Initiate-payment/#recurring-payment-charge-authorization-on-card "Direct link to Recurring Payment \(Charge Authorization on Card\)")
This allows you charge a card without collecting the card information each time.
For recurring Payments test on Sandbox, ensure to use the test card: 5200000000000007
### Card Tokenization[​](https://docs.squadco.com/Payments/Initiate-payment/#card-tokenization "Direct link to Card Tokenization")
Our system utilizes card tokenization, a security technique that replaces the customer's sensitive details with a unique, randomly generated token. This token can be safely stored and used for future transactions, eliminating the need to request the customer's card details again.
To tokenize a card, just add a flag to the initiate payload when calling the initiate endpoint and the card will automatically be tokenized. The unique token code will automatically be added to the webhook notification that will be received after payment.

```
"is_recurring":true  

```

### Sample Request for Card Tokenization[​](https://docs.squadco.com/Payments/Initiate-payment/#sample-request-for-card-tokenization "Direct link to Sample Request for Card Tokenization")

```
{  
    "amount":43000,  
    "email":"henimastic@gmail.com",  
    "currency":"NGN",  
    "initiate_type": "inline",  
    "transaction_ref":"bchs4678388588350909090AH",  
    "callback_url":"http://squadco.com",  
    "is_recurring":true  
}  

```

### Sample Webhook Response For Tokenized Card[​](https://docs.squadco.com/Payments/Initiate-payment/#sample-webhook-response-for-tokenized-card "Direct link to Sample Webhook Response For Tokenized Card")

```
{  
  "Event": "charge_successful",  
  "TransactionRef": "SQTECH6389058547434300003",  
  "Body": {  
    "amount": 11000,  
    "transaction_ref": "SQTECH6389058547434300003",  
    "gateway_ref": "SQTECH6389058547434300003_1_6_1",  
    "transaction_status": "Success",  
    "email": "william@gmail.com",  
    "merchant_id": "SBSJ3KMH",  
    "currency": "NGN",  
    "transaction_type": "Card",  
    "merchant_amount": 868,  
    "created_at": "2025-08-12T10:51:14.368",  
    "meta": {  
      "details": "level1",  
      "location": "Lagos"  
    },  
    "payment_information": {  
      "payment_type": "card",  
      "pan": "509983******3911|1027",  
      "card_type": "mastercard",  
      "token_id": "AUTH_lBlGESHDLMX_60049043"  
    },  
    "is_recurring": true  
  }  
}  

```

### Charge Card[​](https://docs.squadco.com/Payments/Initiate-payment/#charge-card "Direct link to Charge Card")
This allows you charge a card using the token_id (The token_id is sent as part of the webhook on the first call).
POST
https://sandbox-api-d.squadco.com/transaction/charge_card
This debits a credit card using the token_id
#### Parameters
##### Body
amount*
Integer
Amount to charge from card in the lowest currency value. kobo for NGN transactions or cent for USD transactions
token_id*
String
A unique tokenization code for each card transaction and it is returned via the webhook for first charge on the card.
transaction_ref*
String
Unique case-sensitive transaction reference. If you do not pass this parameter, Squad will generate a unique reference for you.
#### Responses
200:OK
Successful

```
{  
            "status": 200,  
            "success": true,  
            "message": "Success",  
            "data": {  
                "transaction_amount": 0,  
                "transaction_ref": null,  
                "email": null,  
                "transaction_status": null,  
                "transaction_currency_id": null,  
                "created_at": "0001-01-01T00:00:00",  
                "transaction_type": null,  
                "merchant_name": null,  
                "merchant_business_name": null,  
                "gateway_transaction_ref": null,  
                "recurring": null,  
                "merchant_email": null,  
                "plan_code": null  
            }  
}  

```

400:Bad Request
Bad Request

```
{  
            "status": 400,  
            "success": false,  
            "message": "amount cannot be < 0",  
            "data": {}  
}  

```

### Sample Request[​](https://docs.squadco.com/Payments/Initiate-payment/#sample-request-1 "Direct link to Sample Request")

```
{  
    "amount":10000,  
    "token_id":"tJlYMKcwPd",  
}  

```

### Cancel Charge Card[​](https://docs.squadco.com/Payments/Initiate-payment/#cancel-charge-card "Direct link to Cancel Charge Card")
This endpoint allows you to cancel a card which was previously tokenised.
PATCH
https://sandbox-api-d.squadco.com/transaction/cancel/recurring
This endpoint cancels active tokens
#### Parameters
##### Body
auth_code*
String
Token ID sent via webhook at first tokenized call.
#### Responses
200:OK
Successful

```
{  
          "status": 200,  
          "success": true,  
          "message": "Success",  
          "data": {  
              "auth_code": [  
                  "AUTH_lBlGXSHDLMX_63749043"  
        ]  
    }  
            }  
}  

```

400:Bad Request
Bad Request

```
{  
            "status": 400,  
            "success": false,  
            "message": "Recurring Payment was not cancelled",  
            "data": {}  
}  

```

### Sample Request[​](https://docs.squadco.com/Payments/Initiate-payment/#sample-request-2 "Direct link to Sample Request")

```
{  
  "auth_code": [  
    "AUTH_SlYtufQzy_452037"  
  ]  
}  

```

### Query All Transactions[​](https://docs.squadco.com/Payments/Initiate-payment/#query-all-transactions "Direct link to Query All Transactions")
This endpoint allows you to query all transactions and filter using multiple parameters like transaction ref, start and end dates, amount, etc
The date parameters are compulsory and should be a maximum of one month gap. Requests without date parameters will fail with error 400: Bad request.
GET
https://sandbox-api-d.squadco.com/transaction
#### Parameters
##### Query
currency*
string
transacting currency
start_date*
date
start date of transaction
end_date*
date
end date of transaction
page*
integer
number of transactions to be displayed in a page
perpage*
integer
number of transactions to be displayed in a page
reference*
string
transaction ref of a transaction
#### Responses
200:OK
Success

```
"status": 200,  
    "success": true,  
    "message": "Success",  
    "data": [  
        {  
            "id": 589,  
            "transaction_amount": 500000,  
            "transaction_ref": "SQDEMO6384411820295800001",  
            "email": "demo@merchant.com",  
            "merchant_id": "AABBCCDDEEFFGGHHJJKK",  
            "merchant_amount": 495000,  
            "merchant_name": "Demo Habari Shop",  
            "merchant_business_name": "Ogbologba and Sons Limited",  
            "merchant_email": "demo@merchant.com",  
            "customer_email": "demo@merchant.com",  
            "customer_name": "Test QA",  
            "meta_data": "{"ip_address":"154.113.177.121","Customer_name":"Test QA","user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36","referring_site":"https://pay.squadinc.co/","payment_link_id":"GH9Y19","payment_link_type":"otp","source":"Desktop","device_id":null,"order_id":null,"auth_code":null,"fingerprintData":null,"callback_url":null,"initiate_type":null,"browser_screen_height":695,"browser_screen_width":1536,"referrer_url":"https://pay.squadinc.co/","extra":"{}"}",  
            "meta": {  
                "ip_address": [],  
                "Customer_name": [],  
                "user_agent": [],  
                "referring_site": [],  
                "payment_link_id": [],  
                "payment_link_type": [],  
                "source": [],  
                "device_id": [],  
                "order_id": [],  
                "auth_code": [],  
                "fingerprintData": [],  
                "callback_url": [],  
                "initiate_type": [],  
                "browser_screen_height": [],  
                "browser_screen_width": [],  
                "referrer_url": [],  
                "extra": []  
            },  
            "transaction_status": "success",  
            "transaction_charges": 0,  
            "transaction_currency_id": "NGN",  
            "transaction_gateway_id": "",  
            "transaction_type": "Card",  
            "flat_charge": 0,  
            "is_suspicious": false,  
            "is_refund": false,  
            "created_at": "2024-02-21T13:16:43.012+00:00"  
}  

```

400:Bad request
Bad Request

```
{  
    "status": 400,  
    "success": false,  
    "message": "Bad Request",  
    "data": {}  
    }  

```

### Go Live[​](https://docs.squadco.com/Payments/Initiate-payment/#go-live "Direct link to Go Live")
To go live, simply:
  1. Change the base URL of your endpoints from sandbox-api-d.squadco.com to api-d.squadco.com
  2. [Sign up on our Live Environment](https://dashboard.squadco.com/login)
  3. Complete your KYC
  4. Use the secret key provided on the dashboard to replace the test keys gotten from the sandbox environment to authenticate your live transactions.


[](https://github.com/HabariPay/habaripay.github.io/tree/main/docs/Payments/Initiate-payment.mdx)
[Previous Payments](https://docs.squadco.com/Payments/overview)[Next Verify Transaction](https://docs.squadco.com/Payments/verify-transaction)
  * [Sample Request](https://docs.squadco.com/Payments/Initiate-payment/#sample-request)
  * [Simulate Test Payment (Transfer)](https://docs.squadco.com/Payments/Initiate-payment/#simulate-test-payment-transfer)
  * [Sample Request Simulate Payment](https://docs.squadco.com/Payments/Initiate-payment/#sample-request-simulate-payment)
  * [Recurring Payment (Charge Authorization on Card)](https://docs.squadco.com/Payments/Initiate-payment/#recurring-payment-charge-authorization-on-card)
  * [Card Tokenization](https://docs.squadco.com/Payments/Initiate-payment/#card-tokenization)
  * [Sample Request for Card Tokenization](https://docs.squadco.com/Payments/Initiate-payment/#sample-request-for-card-tokenization)
  * [Sample Webhook Response For Tokenized Card](https://docs.squadco.com/Payments/Initiate-payment/#sample-webhook-response-for-tokenized-card)
  * [Charge Card](https://docs.squadco.com/Payments/Initiate-payment/#charge-card)
  * [Sample Request](https://docs.squadco.com/Payments/Initiate-payment/#sample-request-1)
  * [Cancel Charge Card](https://docs.squadco.com/Payments/Initiate-payment/#cancel-charge-card)
  * [Sample Request](https://docs.squadco.com/Payments/Initiate-payment/#sample-request-2)
  * [Query All Transactions](https://docs.squadco.com/Payments/Initiate-payment/#query-all-transactions)
  * [Go Live](https://docs.squadco.com/Payments/Initiate-payment/#go-live)


