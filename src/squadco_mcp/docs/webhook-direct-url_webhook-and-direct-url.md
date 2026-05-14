# Source: https://docs.squadco.com/webhook-direct-url/webhook-and-direct-url

[Skip to main content](https://docs.squadco.com/webhook-direct-url/webhook-and-direct-url/#__docusaurus_skipToContent_fallback)
[![My Site Logo](https://docs.squadco.com/img/squad_logo.svg)](https://docs.squadco.com/)
Search`K`
[Support](https://squadco.com/support/)[Create Account](https://dashboard.squadco.com/sign-up)[Sign In](https://dashboard.squadco.com/login)
  * [Home](https://docs.squadco.com/)
  * [Payments](https://docs.squadco.com/webhook-direct-url/webhook-and-direct-url/)
  * [Webhook & Redirect URL](https://docs.squadco.com/webhook-direct-url/webhook-and-direct-url/)
    * [Webhook & Redirect URL](https://docs.squadco.com/webhook-direct-url/webhook-and-direct-url)
    * [Signature validation](https://docs.squadco.com/webhook-direct-url/signature-validation)
    * [Secure File Transfer Protocol (SFTP) Notification](https://docs.squadco.com/webhook-direct-url/sftp)
  * [Virtual Accounts](https://docs.squadco.com/webhook-direct-url/webhook-and-direct-url/)
  * [Transfer API](https://docs.squadco.com/webhook-direct-url/webhook-and-direct-url/)
  * [Others](https://docs.squadco.com/webhook-direct-url/webhook-and-direct-url/)
  * [Value Added Services (VAS)](https://docs.squadco.com/webhook-direct-url/webhook-and-direct-url/)


  * [](https://docs.squadco.com/)
  * Webhook & Redirect URL
  * Webhook & Redirect URL


On this page
# Webhook & Redirect URL
Webhooks are used so that anytime an event occurs on your account, your application can be notified with instant, real-time notifications by Squad.
Squad webhooks are HTTP calls that are triggered by specific events. It is necessary only for behind-the-scenes transactions.
This can be set up on your Squad Dashboard by specifying a URL we would send POST requests to whenever a successful transaction occurs.
To process notifications, you need to:
Paste your redirect and **Callback/Webhook URL** in the space provided on your dashboard by following the steps below:
  * Login to your Squad dashboard.
  * Go to Profile > API & Webhook.
  * In the Webhook URL field, enter your Notification URL.
  * In the redirect URL field, enter your redirect URL- and on completion of payment, the customer will be redirected to the URL with the transaction reference passed as a query param.
  * Enter a redirect URL for your customers to be redirected after they complete payment.


NB:The Redirect URL is optional.
**KINDLY ENSURE YOU HAVE A TRANSACTION REFERENCE CHECKER WHEN IMPLEMENTING WEBHOOKS TO AVOID GIVING DOUBLE VALUE ON TRANSACTIONS.**
Sending IP: 18.133.63.109
### Webhook Validation[​](https://docs.squadco.com/webhook-direct-url/webhook-and-direct-url/#webhook-validation "Direct link to Webhook Validation")
To configure webhook notifications: go to **_dashboard > profile > Api & Webhooks._**
POST
https://api.gitbook.com/v1/users
### The Webhook is a post request that is triggered whenever a transaction is successful
#### Parameters
##### Header
x-squad-encrypted-body*
Hash
This is the encrypted payload which serves as a test of truth for all transactions. This should be compared against the body sent via the webhook by encrypting the body of data and comparing the value with this value
Content-type*
JSON
application/json
  

Sample POST request to be sent via webhook upon successful transaction
### Sample Webhook for Card Transactions[​](https://docs.squadco.com/webhook-direct-url/webhook-and-direct-url/#sample-webhook-for-card-transactions "Direct link to Sample Webhook for Card Transactions")

```
{  
  "Event": "charge_successful",  
  "TransactionRef": "SQTEST6389164239897900003",  
  "Body": {  
    "amount": 10000,  
    "transaction_ref": "SQTEST6389164239897900003",  
    "gateway_ref": "SQTEST6389164239897900003_1_18_1",  
    "transaction_status": "Success",  
    "email": "williamudousoro@gmail.com",  
    "merchant_id": "SBBWRX1Z3S",  
    "currency": "NGN",  
    "transaction_type": "Card",  
    "merchant_amount": 10000,  
    "created_at": "2025-08-24T15:26:38.994",  
    "meta": {  
      "location": "gtbank test test"  
    },  
    "payment_information": {  
      "payment_type": "card",  
      "pan": "424242******4242|0825",  
      "card_type": "verve"  
    },  
    "is_recurring": false  
  }  
}  

```

### Sample Webhook for Transfers[​](https://docs.squadco.com/webhook-direct-url/webhook-and-direct-url/#sample-webhook-for-transfers "Direct link to Sample Webhook for Transfers")

```
{  
  "Event": "charge_successful",  
  "TransactionRef": "SQTECH6389179925109400004",  
  "Body": {  
    "amount": 10000,  
    "transaction_ref": "SQTECH6389179925109400004",  
    "gateway_ref": "SQTECH6389179925109400004_5_5_1",  
    "transaction_status": "Success",  
    "email": "williamudousoro@gmail.com",  
    "merchant_id": "P7SJ3KMH",  
    "currency": "NGN",  
    "transaction_type": "Transfer",  
    "merchant_amount": 10000,  
    "created_at": "2025-08-26T12:00:51.1",  
    "meta": {  
      "location": "gtbank bank test"  
    },  
    "is_recurring": false  
  }  
}  
  

```

### Sample Webhook for Bank[​](https://docs.squadco.com/webhook-direct-url/webhook-and-direct-url/#sample-webhook-for-bank "Direct link to Sample Webhook for Bank")

```
{  
  "Event": "charge_successful",  
  "TransactionRef": "SQTECH6389179913199300001",  
  "Body": {  
    "amount": 10000,  
    "transaction_ref": "SQTECH6389179913199300001",  
    "gateway_ref": "SQTECH6389179913199300001_2_2_1",  
    "transaction_status": "Success",  
    "email": "williamudousoro@gmail.com",  
    "merchant_id": "P7SJ3KMH",  
    "currency": "NGN",  
    "transaction_type": "Bank",  
    "merchant_amount": 10000,  
    "created_at": "2025-08-26T11:58:52.013",  
    "meta": {  
      "location": "Bank option extra data"  
    },  
    "is_recurring": false  
  }  
}  
  

```

### SAMPLE WEBHOOK FOR USSD PAYMENT OPTION[​](https://docs.squadco.com/webhook-direct-url/webhook-and-direct-url/#sample-webhook-for-ussd-payment-option "Direct link to SAMPLE WEBHOOK FOR USSD PAYMENT OPTION")

```
{  
      "Event": "charge_successful",  
      "TransactionRef": "SQCHIZ6035872641857",  
      "Body": {  
        "amount": 20000,  
        "transaction_ref": "SQCHIZ6035872641857",  
        "gateway_ref": "SQCHIZ6035872641857_3_1",  
        "transaction_status": "Success",  
        "email": "maaa@h.com",  
        "currency": "NGN",  
        "transaction_type": "Ussd",  
        "merchant_amount": 19800,  
        "created_at": "2023-01-25T13:41:16.223",  
        "customer_mobile": "0803***7205",  
        "meta": {  
          "plan": "premium"  
        },  
        "is_recurring": false  
      }  
}  

```

### Sample Webhook for Merchant USSD (USSD CODE ON THE DASHBOARD)[​](https://docs.squadco.com/webhook-direct-url/webhook-and-direct-url/#sample-webhook-for-merchant-ussd-ussd-code-on-the-dashboard "Direct link to Sample Webhook for Merchant USSD \(USSD CODE ON THE DASHBOARD\)")

```
{  
      "Event": "charge_successful",  
      "TransactionRef": "SQCHIZ410708",  
      "Body": {  
        "amount": 10000,  
        "transaction_ref": "SQCHIZ410708",  
        "gateway_ref": "f7c810f4-b53e-4970-a3f6",  
        "transaction_status": "Success",  
        "email": "0803***0000",  
        "merchant_id": "********",  
        "currency": "NGN",  
        "transaction_type": "MerchantUssd",  
        "merchant_amount": 10000,  
        "created_at": "2022-11-30T16:21:52.8850061+00:00",  
        "customer_mobile": "0803***0000",  
        "meta": {},  
        "payment_information": {  
          "payment_type": "merchantussd",  
          "customer_ref": "123456"  
        },  
        "is_recurring": false  
      }  
}  

```

  

**Please Note that the encrypted body (x-squad-encrypted-body) is usually sent via the header**
[](https://github.com/HabariPay/habaripay.github.io/tree/main/docs/webhook-direct-url/webhook-and-direct-url.mdx)
[Previous POS Remote Request](https://docs.squadco.com/Payments/pos-payment)[Next Signature validation](https://docs.squadco.com/webhook-direct-url/signature-validation)
  * [Webhook Validation](https://docs.squadco.com/webhook-direct-url/webhook-and-direct-url/#webhook-validation)
  * [Sample Webhook for Card Transactions](https://docs.squadco.com/webhook-direct-url/webhook-and-direct-url/#sample-webhook-for-card-transactions)
  * [Sample Webhook for Transfers](https://docs.squadco.com/webhook-direct-url/webhook-and-direct-url/#sample-webhook-for-transfers)
  * [Sample Webhook for Bank](https://docs.squadco.com/webhook-direct-url/webhook-and-direct-url/#sample-webhook-for-bank)
  * [SAMPLE WEBHOOK FOR USSD PAYMENT OPTION](https://docs.squadco.com/webhook-direct-url/webhook-and-direct-url/#sample-webhook-for-ussd-payment-option)
  * [Sample Webhook for Merchant USSD (USSD CODE ON THE DASHBOARD)](https://docs.squadco.com/webhook-direct-url/webhook-and-direct-url/#sample-webhook-for-merchant-ussd-ussd-code-on-the-dashboard)


