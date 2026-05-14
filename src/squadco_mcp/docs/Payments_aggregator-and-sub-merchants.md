# Source: https://docs.squadco.com/Payments/aggregator-and-sub-merchants/

[Skip to main content](https://docs.squadco.com/Payments/aggregator-and-sub-merchants/#__docusaurus_skipToContent_fallback)
[![My Site Logo](https://docs.squadco.com/img/squad_logo.svg)](https://docs.squadco.com/)
Search`K`
[Support](https://squadco.com/support/)[Create Account](https://dashboard.squadco.com/sign-up)[Sign In](https://dashboard.squadco.com/login)
  * [Home](https://docs.squadco.com/)
  * [Payments](https://docs.squadco.com/Payments/aggregator-and-sub-merchants/)
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
  * [Webhook & Redirect URL](https://docs.squadco.com/Payments/aggregator-and-sub-merchants/)
  * [Virtual Accounts](https://docs.squadco.com/Payments/aggregator-and-sub-merchants/)
  * [Transfer API](https://docs.squadco.com/Payments/aggregator-and-sub-merchants/)
  * [Others](https://docs.squadco.com/Payments/aggregator-and-sub-merchants/)
  * [Value Added Services (VAS)](https://docs.squadco.com/Payments/aggregator-and-sub-merchants/)


  * [](https://docs.squadco.com/)
  * Payments
  * Aggregator and Sub-merchants


On this page
# Aggregator and Sub-merchants
##### This API allows you to be profiled as an aggregator and also create sub-merchants dynamically under your account.[​](https://docs.squadco.com/Payments/aggregator-and-sub-merchants/#this-api-allows-you-to-be-profiled-as-an-aggregator-and-also-create-sub-merchants-dynamically-under-your-account "Direct link to This API allows you to be profiled as an aggregator and also create sub-merchants dynamically under your account.")
##### With this, you are able to initiate transactions from a central point for all businesses or sub merchants under you using the same API keys.[​](https://docs.squadco.com/Payments/aggregator-and-sub-merchants/#with-this-you-are-able-to-initiate-transactions-from-a-central-point-for-all-businesses-or-sub-merchants-under-you-using-the-same-api-keys "Direct link to With this, you are able to initiate transactions from a central point for all businesses or sub merchants under you using the same API keys.")
**Environment base URL:**
**Test:** <https://sandbox-api-d.squadco.com>
**Production:** <https://api-d.squadco.com>
**Authorization** keys are to be passed via Headers as a Bearer token.
**Example:** Authorization: Bearer sandbox_sk_94f2b798466408ef4d19e848ee1a4d1a3e93f104046f.
### Create Sub-merchants.[​](https://docs.squadco.com/Payments/aggregator-and-sub-merchants/#create-sub-merchants "Direct link to Create Sub-merchants.")
This API is used to create a sub-merchant, the sub-merchant will have its own ID and will automatically have its own view on the dashboard.
POST
https://sandbox-api-d.squadco.com/merchant/create-sub-users
#### Parameters
##### Body
display_name*
String
Name of sub-merchant
account_name*
String
Sub-merchant's settlement bank account name
account_number*
String
Sub-merchant's settlement account number
bank_code*
String
Sub-merchant's settlement bank code. e.g 058
bank*
String
Name of sub-merchant's settlement bank e.g GTBank
#### Responses
200:OK
Success

```
{  
      "status": 200,  
      "success": true,  
      "message": "Success",  
      "data": {  
          "account_id": "AGGERYG8WF34"  
      }  
}  

```

400:Bad Request
Error in request payload

```
{  
      "status": 400,  
      "success": false,  
      "message": ""account_number" is required",  
      "data": {}  
}  

```

401:Unauthorized
No Authorization

```
{  
      "success": false,  
      "message": "",  
      "data": {}  
}  

```

403:Forbidden
Wrong/Invalid API Keys

```
{  
      "success": false,  
      "message": "Merchant authentication failed",  
      "data": {}  
}  

```

[](https://github.com/HabariPay/habaripay.github.io/tree/main/docs/Payments/aggregator-and-sub-merchants.mdx)
[Previous Squad Woo Commerce Plugin](https://docs.squadco.com/Payments/squad-woo-squad-plugin)[Next POS Remote Request](https://docs.squadco.com/Payments/pos-payment)
  * [Create Sub-merchants.](https://docs.squadco.com/Payments/aggregator-and-sub-merchants/#create-sub-merchants)


