# Source: https://docs.squadco.com/Payments/direct-api-integration/

[Skip to main content](https://docs.squadco.com/Payments/direct-api-integration/#__docusaurus_skipToContent_fallback)
[![My Site Logo](https://docs.squadco.com/img/squad_logo.svg)](https://docs.squadco.com/)
Search`K`
[Support](https://squadco.com/support/)[Create Account](https://dashboard.squadco.com/sign-up)[Sign In](https://dashboard.squadco.com/login)
  * [Home](https://docs.squadco.com/)
  * [Payments](https://docs.squadco.com/Payments/direct-api-integration/)
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
  * [Webhook & Redirect URL](https://docs.squadco.com/Payments/direct-api-integration/)
  * [Virtual Accounts](https://docs.squadco.com/Payments/direct-api-integration/)
  * [Transfer API](https://docs.squadco.com/Payments/direct-api-integration/)
  * [Others](https://docs.squadco.com/Payments/direct-api-integration/)
  * [Value Added Services (VAS)](https://docs.squadco.com/Payments/direct-api-integration/)


  * [](https://docs.squadco.com/)
  * Payments
  * Direct API Integration


On this page
# Direct API Integration
##### This suite of APIs allows you to directly initiate CARD, BANK and USSD transactions without using the Squad Modal.[​](https://docs.squadco.com/Payments/direct-api-integration/#this-suite-of-apis-allows-you-to-directly-initiate-card-bank-and-ussd-transactions-without-using-the-squad-modal "Direct link to This suite of APIs allows you to directly initiate CARD, BANK and USSD transactions without using the Squad Modal.")
**Environment base URL:**
**Test:** <https://sandbox-api-d.squadco.com>
**Production:** <https://api-d.squadco.com>
**Authorization** keys are to be passed via Headers as a Bearer token.
**Example:** Authorization: Bearer sandbox_sk_94f2b798466408ef4d19e848ee1a4d1a3e93f104046f.
**The transaction reference used to initiate transactions must be unique.**
### Direct CARD[​](https://docs.squadco.com/Payments/direct-api-integration/#direct-card "Direct link to Direct CARD")
This suite of API's allows merchants to directly collect customer card details and charge the cards following the expected steps. Only PCI-DSS-certified and profiled merchants will be able to make use of the service
Due to the nature of payment systems around cards, several possible scenarios may play out, which are broadly classified as:
Payments requiring only PIN for completion
Payments requiring only OTP for completion
Payments requiring a combination of both PIN and OTP for completion
Payments requiring a challenge (3DS) for completion
**The Expected next step to take will be based on the transaction_status in the response body after the Step 1 (Charge Card)**
Test Cards for Different Scenarios
4242424242424242 >> Direct OTP validation (Use Amount < ₦7,500)
5200000000001096 >> 3DS authentication
5555555555554444 >> PIN + OTP (Two-step validation: PIN verification → OTP validation)
### Step #1: Charge Card[​](https://docs.squadco.com/Payments/direct-api-integration/#step-1-charge-card "Direct link to Step #1: Charge Card")
This endpoint allows you to pass collected card details and other required fields
POST
https://sandbox-api-squadco.com/transaction/initiate/process-payment
This endpoint allows you collect card details
#### Parameters
##### Header
Authorization*
String
API keys (Secret Key) that authorize your transactions and gotten from your squad dashboard
##### Body
transaction_reference*
String
An alphanumeric string that uniquely identifies a transaction (where none is presented, the system generates one for you)
amount*
Integer
The amount in kobo you are debiting a customer (expressed in the lowest currency value - kobo). 10000 = 100NGN 
currency*
String
The currency you want the amount to be charged in. Allowed value is NGN
pass_charge*
Boolean
Allows charges to be passed to customer when set as True, else merchant bears charges
webhook_url*
String
Specifies where successful notification is sent on payment completion (superseded by webhook_url set on dashboard)
card*
Object
Collects card details comprising of card number, cvv, expiry_month & expiry_year
payment_method*
String
pass 'card' as value
customer*
Object
Collects name and email of customer making payment, email receives receipt of successfull payment
redirect_url*
String
Specifies site to be redirected to after successfull payment
### Sample Request[​](https://docs.squadco.com/Payments/direct-api-integration/#sample-request "Direct link to Sample Request")

```
{  
    // "transaction_reference": "hell333o123",  
    "amount": 1000000,  
    "pass_charge": true,  
    "currency": "NGN",  
    "webhook_url": "https://webhook.site/50733ce1-f957-4900-9f4a-3eddf0a1f270",  
    "card": {  
        "number": "5555555555554444",  
        "cvv": "121",  
        "expiry_month": "12",  
        "expiry_year": "50"  
    },  
    "payment_method": "card",  
    "customer": {  
        "name": "Tams Bills",  
        "email": "50733ce1-f957-4900-9f4a-3eddf0a1f270@emailhook.site"  
    },  
    "redirect_url": "https://www.squadco.com/"  
}  

```

#### Responses
200:ValidatePin
Successful

```
{  
    "status": 200,  
    "success": true,  
    "message": "Success",  
    "data": {  
        "amount": 1001000,  
        "transaction_ref": "SQDEMO6388697447108000002",  
        "currency": "NGN",  
        "transaction_type": "Card",  
        "gateway_ref": "SQDEMO6388697447108000002_1_1_1",  
        "merchant_amount": 1000000,  
        "message": "Charge Attempted",  
        "transaction_status": "ValidatePin"  
    }  
}  

```

200:ValidateOTP
Successful

```
{  
        "status": 200,  
    "success": true,  
    "message": "Success",  
    "data": {  
        "amount": 50000,  
        "transaction_ref": "SUPR123",  
        "currency": "NGN",  
        "transaction_type": "Card",  
        "gateway_ref": "SUPR123_1_18_1",  
        "merchant_amount": 49500,  
        "transaction_status": "ValidateOTP"  
    }  
}  

```

200:3DS
Successful

```
{  
    "status": 200,  
    "success": true,  
    "message": "Success",  
    "data": {  
        "amount": 1010000,  
        "transaction_ref": "test1001",  
        "currency": "NGN",  
        "transaction_type": "Card",  
        "gateway_ref": "test1001_1_5_4",  
        "merchant_amount": 1000000,  
        "message": "COMPLETED",  
        "auth_url": "https://sandbox-pay.squadco.com/3ds/U0JTNUI4VlUzNl82Mzg4NzA0NDQyNDM4MTQzMTc=",  
        "transaction_status": "ThreeDSecure"  
    }  
}  

```

403:Forbidden
Forbidden

```
{  
    "success": false,  
    "message": "API key is empty or invalid. Key must start with sandbox_sk_",  
    "data": {}  
}  

```

401:Unauthorized
Unauthorized

```
{  
    "success": false,  
    "message": "",  
    "data": {}  
}  

```

### Step #2: Authorize Payment[​](https://docs.squadco.com/Payments/direct-api-integration/#step-2-authorize-payment "Direct link to Step #2: Authorize Payment")
This endpoint allows you to authorize a payment based on the transaction_status from the charge card process
POST
https://sandbox-api-squadco.com/transaction/payment/authorize
This endpoint allows you authorize payments
#### Parameters
##### Header
Authorization*
String
API keys (Secret Key) that authorize your transactions and gotten from your squad dashboard
##### Body
transaction_reference*
String
An alphanumeric string that uniquely identifies a transaction (Returned in the response of the charge card API)
authorization*
Object
Contains pin or otp used to authorize payment
  

For ValidatePin, use PIN: 1234
For ValidateOTP, use OTP: 123456
#### 3DS (ThreeDSecure)[​](https://docs.squadco.com/Payments/direct-api-integration/#3ds-threedsecure "Direct link to 3DS \(ThreeDSecure\)")
Where transaction_status is "ThreeDSecure", the challenge is to be completed by following the URL specified in the auth_url field. When executed, a challenge page is initiated and once the challenge is completed, a payment successful page is displayed and then redirected to redirect_url provided.
### Sample Request for ValidatePin[​](https://docs.squadco.com/Payments/direct-api-integration/#sample-request-for-validatepin "Direct link to Sample Request for ValidatePin")

```
   {  
    "transaction_reference": "SQDEMO6388591221547800002",  
    "authorization": {  
        "pin": "1234"  
    }  
}  

```

### Sample Request for ValidateOTP[​](https://docs.squadco.com/Payments/direct-api-integration/#sample-request-for-validateotp "Direct link to Sample Request for ValidateOTP")

```
{  
    "transaction_reference": "SQDEMO6388591221547800002",  
    "authorization": {  
        "otp": "123456"  
    }  
}  

```

#### Responses
200:ValidatePin + OTP
Successful

```
{  
    "status": 200,  
    "success": true,  
    "message": "Success",  
    "data": {  
        "amount": 1001000,  
        "transaction_ref": "SQDEMO6388697447108000002",  
        "currency": "NGN",  
        "transaction_type": "Card",  
        "gateway_ref": "SQDEMO6388697447108000002_1_1_1",  
        "merchant_amount": 1000000,  
        "message": "Validate pin attempted",  
        "transaction_status": "ValidateOTP"  
    }  
}  

```

200:ValidateOTP
Successful

```
{  
    "status": 200,  
    "success": true,  
    "message": "Success",  
    "data": {  
        "amount": 1001000,  
        "transaction_ref": "SQDEMO6388697447108000002",  
        "transaction_type": "Card",  
        "gateway_ref": "SQDEMO6388697447108000002_1_1_1",  
        "merchant_amount": 1000000,  
        "message": "Validate OTP Successful.",  
        "transaction_status": "Success"  
    }  
}  

```

403:Forbidden
Forbidden

```
{  
    "success": false,  
    "message": "API key is empty or invalid. Key must start with sandbox_sk_",  
    "data": {}  
}  

```

401:Unauthorized
Unauthorized

```
{  
    "success": false,  
    "message": "",  
    "data": {}  
}  

```

## Direct GTBank account debit[​](https://docs.squadco.com/Payments/direct-api-integration/#direct-gtbank-account-debit "Direct link to Direct GTBank account debit")
This endpoint allows you to initiate the direct debit of a GTBank account by passing the account number. After initiating the request using this endpoint you are then to call the validate endpoint to complete the transaction.
POST
https://sandbox-api-squadco.com/transaction/initiate/process-payment
This endpoint initiate the direct debit of a GTBank account by passing the account number or the phone number linked to the account
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
The amount in kobo you are debiting customer (expressed in the lowest currency value - kobo). 10000 = 100NGN 
currency*
String
The currency you want the amount to be charged in. Allowed value is NGN
name*
String
Name of Customer carrying out the transaction.
transaction_ref*
String
This states the method by which the transaction is initiated. At the moment, this can only take the value 'inline'.
bank_code*
String
Unique NIP code that identifies a bank.
payment_method*
String
method of payment (should use BANK)
transaction_ref*
String
An alphanumeric string that uniquely identifies a transaction (where none is presented, the sytem generates one for you)
webhook_url*
String
Allows you define where webhook notification is sent (where none is presented, the default webhook for merchant is notified)
account_or_phone*
String
The GTBank account number or phone number linked to the account to be debitted
pass_charge*
Boolean
It takes two possible values: True or False. It is set to False by default. When set to True, the charges on the transaction is computed and passed on to the customer(payer). But when set to False, the charge is passed to the merchant and will be deducted from the amount to be settled to the merchant.
### Sample Request[​](https://docs.squadco.com/Payments/direct-api-integration/#sample-request-1 "Direct link to Sample Request")

```
{  
  "transaction_reference": "test001",  
  "amount": 51800,  
  "pass_charge": false,  
  "currency": "NGN",  
  "webhook_url": "www.sampleurl.com",  
  "bank": {  
    "bank_code": "058",  
    "account_or_phoneno": "08146663666"  
  },  
  "payment_method": "bank",  
  "customer": {  
     "name": "William Udousoro",  
   "email": "squadtest@gmail.com"  
  }  
}  

```

#### Responses
200:OK
Successful

```
{  
    "status": 200,  
    "success": true,  
    "message": "Success",  
    "data": {  
        "amount": 51800,  
        "transaction_ref": "SQDEMO6386363720055500003",  
        "transaction_type": "Bank",  
        "gateway_ref": "SQDEMO6386363720055500003_2_2_1",  
        "merchant_amount": 46178.4,  
        "message": "Please enter the 6-digit code from your GTBank token / e-Token or dial *737*7# with your registered GTBank phone number.",  
        "auth_model": "ValidateTOKEN"  
    }  
}  

```

401:Unauthorized
Invalid/No Authorization Key

```
{  
    "success": false,  
    "message": "",  
    "data": {}  
}  

```

400:Bad Request
Bad Request

```
{  
    "status": 400,  
    "success": false,  
    "message": ""account_or_phoneno" is required",  
    "data": {}  
}  

```

### Validate Payment for Direct Bank API Payment[​](https://docs.squadco.com/Payments/direct-api-integration/#validate-payment-for-direct-bank-api-payment "Direct link to Validate Payment for Direct Bank API Payment")
Once an account debit is initiated using the Direct Bank API, the transaction must be authenticated. This is done using this endpoint to receive details from the user.
For the auth_model, the value can be either "ValidateTOKEN" or "ValidateOTP." If "ValidateTOKEN" is received, the payee must input the OTP from _737_ 7#, a hardware token, or an e-token to complete the transaction. If "ValidateOTP" is returned, an OTP will be sent to the phone number linked to the customer account number, which the payee will then input to finalize the transaction.
POST
https://sandbox-api-squadco.com/transaction/validate-payment
This endpoint is used to validate account debit request.
#### Parameters
##### Header
Authorization*
String
API keys (Secret Key) that authorize your transactions and gotten from your squad dashboard
##### Body
transaction_reference*
String
Transaction Refrence from the initiated payment
otp_token*
String
Unique OTP or Token sent to customer, required for transaction completion
authorization*
String
Contains otp_token
### Sample Request[​](https://docs.squadco.com/Payments/direct-api-integration/#sample-request-2 "Direct link to Sample Request")

```
{  
  "transaction_reference": "SQDEMO6386363261862600002",  
  "authorization": {  
    "otp_token": "123456"  
  }  
}  

```

#### Responses
ValidateTOKEN

```
{  
    "status": 200,  
    "success": true,  
    "message": "Success",  
    "data": {  
        "amount": 56800,  
        "transaction_ref": "SQDEMO6386313153377900002",  
        "transaction_type": "Bank",  
        "gateway_ref": "SQDEMO6386313153377900002_2_2_1",  
        "merchant_amount": 51118.4,  
        "auth_model": "ValidateTOKEN",  
        "message": "Charge attempted"  
    }  
}  

```

ValidateOTP

```
{  
    "status": 200,  
    "success": true,  
    "message": "Success",  
    "data": {  
        "amount": 56800,  
        "transaction_ref": "SQDEMO6386313153377900002",  
        "transaction_type": "Bank",  
        "gateway_ref": "SQDEMO6386313153377900002_2_2_1",  
        "merchant_amount": 51118.4,  
        "auth_model": "ValidateOTP",  
        "message": "Charge attempted"  
    }  
}  

```

403:Forbidden
Forbidden

```
{  
    "success": false,  
    "message": "API key is empty or invalid. Key must start with sandbox_sk_",  
    "data": {}  
}  

```

401:Unauthorized
Unauthorized

```
{  
    "success": false,  
    "message": "",  
    "data": {}  
}  

```

### Initiate USSD payment[​](https://docs.squadco.com/Payments/direct-api-integration/#initiate-ussd-payment "Direct link to Initiate USSD payment")
This API allows you to directly process USSD transactions, with the same param details as direct bank payment.
POST
https://sandbox-api-squadco.com/transaction/initiate/process-payment
This endpoint initiates a USSD transaction
#### Parameters
##### Body
transaction_reference*
String
Transaction Refrence from the initiated payment
otp_token*
String
Unique OTP or Token sent to customer, required for transaction completion
authorization*
String
Contains otp_token
#### USSD SUPPORTED BANKS AND BANK CODES[​](https://docs.squadco.com/Payments/direct-api-integration/#ussd-supported-banks-and-bank-codes "Direct link to USSD SUPPORTED BANKS AND BANK CODES")  
| Bank Name  | Bank Code  |  
| --- | --- |  
| Access (Diamond)  | 063  |  
| Access  | 044  |  
| Ecobank  | 050  |  
| FCMB  | 214  |  
| Fidelity Bank  | 070  |  
| First Bank  | 011  |  
| Guaranty Trust Bank  | 058  |  
| Heritage Bank  | 030  |  
| Keystone Bank  | 082  |  
| Rubies (Highstreet) MFB  | 125  |  
| Stanbic Bank  | 221  |  
| Sterling Bank  | 232  |  
| UBA  | 033  |  
| Union Bank  | 032  |  
| Unity Bank  | 215  |  
| VFD Bank  | 566  |  
| Wema Bank  | 035  |  
| Zenith Bank  | 057  |  
| Globus Bank  | 00103  |  
| Premium Trust Bank  | 105  |  
| LOTUS Bank  | 303  |  
| Optimum Trust Bank  | 107  |  
| Kuda MFB  | 50211  |  
| The bank code provided is what should be populated in the bank_code parameter.  |   |  
### Sample Request[​](https://docs.squadco.com/Payments/direct-api-integration/#sample-request-3 "Direct link to Sample Request")

```
{  
  "transaction_reference": "testussd",  
  "amount": 56800,  
  "pass_charge": false,  
  "currency": "NGN",  
  "webhook_url": "www.sampleurl.com",  
  "ussd": {  
    "bank_code": "058"  
  },  
  "payment_method": "ussd",  
  "customer": {  
    "name": "Test User",  
    "email": "TestUser@gmail.com"  
  }  
}  

```

#### Responses
200:OK
Successful

```
{  
    "status": 200,  
    "success": true,  
    "message": "Success",  
    "data": {  
        "amount": 56800,  
        "transaction_ref": "SQDEMO6386363261862600002",  
        "transaction_type": "Ussd",  
        "gateway_ref": "SQDEMO6386363261862600002_3_3_1",  
        "merchant_amount": 51118.4,  
        "message": "USSD Payment Reference Generated",  
        "auth_model": "USSDCodeGenerated",  
        "ussd_details": {  
            "ussd_reference": "*737*000*1914",  
            "expiresAt": "2024-10-04T11:01:59.8888866"  
        }  
    }  
}  

```

403:Forbidden
Forbidden

```
{  
    "success": false,  
    "message": "API key is empty or invalid. Key must start with sandbox_sk_",  
    "data": {}  
}  

```

401:Unauthorized
Unauthorized

```
{  
    "success": false,  
    "message": "",  
    "data": {}  
}  

```

### Go Live[​](https://docs.squadco.com/Payments/direct-api-integration/#go-live "Direct link to Go Live")
To go live, simply:
  1. Change the base URL of your endpoints from sandbox-api-d.squadco.com to api-d.squadco.com
  2. [Sign up on our Live Environment](https://dashboard.squadco.com/login)
  3. Complete your KYC
  4. Use the secret key provided on the dashboard to replace the test keys gotten from the sandbox environment to authenticate your live transactions.


[](https://github.com/HabariPay/habaripay.github.io/tree/main/docs/Payments/direct-api-integration.mdx)
[Previous Test Cards](https://docs.squadco.com/Payments/test-cards)[Next Direct Debit](https://docs.squadco.com/Payments/direct-debit)
  * [Direct CARD](https://docs.squadco.com/Payments/direct-api-integration/#direct-card)
  * [Step #1: Charge Card](https://docs.squadco.com/Payments/direct-api-integration/#step-1-charge-card)
  * [Sample Request](https://docs.squadco.com/Payments/direct-api-integration/#sample-request)
  * [Step #2: Authorize Payment](https://docs.squadco.com/Payments/direct-api-integration/#step-2-authorize-payment)
  * [Sample Request for ValidatePin](https://docs.squadco.com/Payments/direct-api-integration/#sample-request-for-validatepin)
  * [Sample Request for ValidateOTP](https://docs.squadco.com/Payments/direct-api-integration/#sample-request-for-validateotp)
  * [Direct GTBank account debit](https://docs.squadco.com/Payments/direct-api-integration/#direct-gtbank-account-debit)
    * [Sample Request](https://docs.squadco.com/Payments/direct-api-integration/#sample-request-1)
    * [Validate Payment for Direct Bank API Payment](https://docs.squadco.com/Payments/direct-api-integration/#validate-payment-for-direct-bank-api-payment)
    * [Sample Request](https://docs.squadco.com/Payments/direct-api-integration/#sample-request-2)
    * [Initiate USSD payment](https://docs.squadco.com/Payments/direct-api-integration/#initiate-ussd-payment)
    * [Sample Request](https://docs.squadco.com/Payments/direct-api-integration/#sample-request-3)
    * [Go Live](https://docs.squadco.com/Payments/direct-api-integration/#go-live)


