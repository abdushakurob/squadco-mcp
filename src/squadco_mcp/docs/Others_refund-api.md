# Source: https://docs.squadco.com/Others/refund-api/

[Skip to main content](https://docs.squadco.com/Others/refund-api/#__docusaurus_skipToContent_fallback)
[![My Site Logo](https://docs.squadco.com/img/squad_logo.svg)](https://docs.squadco.com/)
Search`K`
[Support](https://squadco.com/support/)[Create Account](https://dashboard.squadco.com/sign-up)[Sign In](https://dashboard.squadco.com/login)
  * [Home](https://docs.squadco.com/)
  * [Payments](https://docs.squadco.com/Others/refund-api/)
  * [Webhook & Redirect URL](https://docs.squadco.com/Others/refund-api/)
  * [Virtual Accounts](https://docs.squadco.com/Others/refund-api/)
  * [Transfer API](https://docs.squadco.com/Others/refund-api/)
  * [Others](https://docs.squadco.com/Others/refund-api/)
    * [Disputes & Chargebacks](https://docs.squadco.com/Others/disputes-chargebacks)
    * [Refund API](https://docs.squadco.com/Others/refund-api)
  * [Value Added Services (VAS)](https://docs.squadco.com/Others/refund-api/)


  * [](https://docs.squadco.com/)
  * Others
  * Refund API


On this page
# Refund API
This API is used to initiate refund process on a successful transaction.
Any request made without the authorization key (secret key) will fail with a 401 (Unauthorized) response code.
The authorization key is sent via the request header as Bearer Token Authorization
**Example:** Authorization: Bearer sandbox_sk_94f2b798466408ef4d19e848ee1a4d1a3e93f104046f
POST
https://sandbox-api-d.squadco.com/transaction/refund
### This endpoint refunds an already completed transactions
#### Parameters
##### Body
gateway_transaction_ref*
String
Unique reference that uniquely identifies the medium of payment and can be obtained from the webhook notification sent to you.
transaction_ref*
String
unique reference that identifies a transaction. Can be obtained from the dashboard or the webhook notification sent to you
refund_type*
String
The value of this parameter is either 'Full' or 'Partial'
reason_for_refund*
String
Reason for initiating the refund
refund_amount*
String
Refund amount is in kobo or cent. This is only required for 'Partial' refunds
#### Responses
200:OK
Success

```
{  
            "status": 200,  
            "success": true,  
            "message": "Success",  
            "data": {  
                "gateway_refund_status": "pending",  
                "refund_status": 2,  
                "refund_reference": "REFUND-SQOKOY1708696818297_1_1"  
            }  
}  

```

401:Unathorized
No API Key

```
{  
            "success": false,  
            "message": "",  
            "data": {}  
}  

```

#### Sample Request[​](https://docs.squadco.com/Others/refund-api/#sample-request "Direct link to Sample Request")
#### Full Refund[​](https://docs.squadco.com/Others/refund-api/#full-refund "Direct link to Full Refund")

```
{  
    "gateway_transaction_ref": "wvszqsdrujscpuaofnea529117332_1_1",  
    "refund_type": "Full",  
    "reason_for_refund": "Any reason",  
    "transaction_ref": "vszqsdrujscpua"  
}  

```

#### Partial Refund[​](https://docs.squadco.com/Others/refund-api/#partial-refund "Direct link to Partial Refund")

```
{  
    "gateway_transaction_ref": "SQOKOY3167299494777_1_1",  
    "refund_type": "Partial",  
    "reason_for_refund": "Testing Testing",  
    "transaction_ref": "SQOKOY3167299494777",  
    "refund_amount":"20000"  
}  

```

### GO LIVE - Production[​](https://docs.squadco.com/Others/refund-api/#go-live---production "Direct link to GO LIVE - Production")
To Use this API on production:
  1. Kindly change the base URL of the endpoint from sandbox-api-d.squadco.com to api-d.squadco.com
  2. Get production keys from your production environment on dashboard.squadco.com and replace as authorization keys.


[](https://github.com/HabariPay/habaripay.github.io/tree/main/docs/Others/refund-api.mdx)
[Previous Disputes & Chargebacks](https://docs.squadco.com/Others/disputes-chargebacks)[Next Airtime and Data](https://docs.squadco.com/Value-added-services/vas)
  * [GO LIVE - Production](https://docs.squadco.com/Others/refund-api/#go-live---production)


