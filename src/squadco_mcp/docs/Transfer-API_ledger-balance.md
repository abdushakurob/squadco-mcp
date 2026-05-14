# Source: https://docs.squadco.com/Transfer-API/ledger-balance/

[Skip to main content](https://docs.squadco.com/Transfer-API/ledger-balance/#__docusaurus_skipToContent_fallback)
[![My Site Logo](https://docs.squadco.com/img/squad_logo.svg)](https://docs.squadco.com/)
Search`K`
[Support](https://squadco.com/support/)[Create Account](https://dashboard.squadco.com/sign-up)[Sign In](https://dashboard.squadco.com/login)
  * [Home](https://docs.squadco.com/)
  * [Payments](https://docs.squadco.com/Transfer-API/ledger-balance/)
  * [Webhook & Redirect URL](https://docs.squadco.com/Transfer-API/ledger-balance/)
  * [Virtual Accounts](https://docs.squadco.com/Transfer-API/ledger-balance/)
  * [Transfer API](https://docs.squadco.com/Transfer-API/ledger-balance/)
    * [Transfer API](https://docs.squadco.com/Transfer-API/transfer-apis)
    * [Ledger Balance](https://docs.squadco.com/Transfer-API/ledger-balance)
  * [Others](https://docs.squadco.com/Transfer-API/ledger-balance/)
  * [Value Added Services (VAS)](https://docs.squadco.com/Transfer-API/ledger-balance/)


  * [](https://docs.squadco.com/)
  * Transfer API
  * Ledger Balance


On this page
# Ledger Balance
##### This endpoint allows you get your Squad Account Balance.[​](https://docs.squadco.com/Transfer-API/ledger-balance/#this-endpoint-allows-you-get-your-squad-account-balance "Direct link to This endpoint allows you get your Squad Account Balance.")
**Environment base URL:**
**Test:** <https://sandbox-api-d.squadco.com>
**Production:** <https://api-d.squadco.com>
**Authorization** keys are to be passed via Headers as a Bearer token.
**Example:** Authorization: Bearer sandbox_sk_94f2b798466408ef4d19e848ee1a4d1a3e93f104046f
**Please be informed that the ledger balance is in KOBO. (Please note that you can't get ledger balance for Dollar transactions).**
GET
https://sandbox-api-d.squadco.com/merchant/balance
### This endpoint allows you get your Squad Ledger Balance. Amount is in KOBO
#### Parameters
##### Query
currency_id*
String
It only takes the value 'NGN'. (Please note that you can't get ledger balance for Dollar transactions)
#### Responses
200:OK
Success

```
{  
            "status": 200,  
            "success": true,  
            "message": "Success",  
            "data": {  
                "balance": "2367013",  
                "currency_id": "NGN",  
                "merchant_id": "SBN1EBZEQ8"  
            }  
}  

```

401:Unathorized
No Authorization

```
{  
            "success": false,  
            "message": "",  
            "data": {}  
}  

```

403:Forbidden
Invalid/Wrong API Keys

```
{  
            "success": false,  
            "message": "Merchant authentication failed",  
            "data": {}  
}  

```

[](https://github.com/HabariPay/habaripay.github.io/tree/main/docs/Transfer-API/ledger-balance.mdx)
[Previous Transfer API](https://docs.squadco.com/Transfer-API/transfer-apis)[Next Disputes & Chargebacks](https://docs.squadco.com/Others/disputes-chargebacks)
