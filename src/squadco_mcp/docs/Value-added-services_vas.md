# Source: https://docs.squadco.com/Value-added-services/vas/

[Skip to main content](https://docs.squadco.com/Value-added-services/vas/#__docusaurus_skipToContent_fallback)
[![My Site Logo](https://docs.squadco.com/img/squad_logo.svg)](https://docs.squadco.com/)
Search`K`
[Support](https://squadco.com/support/)[Create Account](https://dashboard.squadco.com/sign-up)[Sign In](https://dashboard.squadco.com/login)
  * [Home](https://docs.squadco.com/)
  * [Payments](https://docs.squadco.com/Value-added-services/vas/)
  * [Webhook & Redirect URL](https://docs.squadco.com/Value-added-services/vas/)
  * [Virtual Accounts](https://docs.squadco.com/Value-added-services/vas/)
  * [Transfer API](https://docs.squadco.com/Value-added-services/vas/)
  * [Others](https://docs.squadco.com/Value-added-services/vas/)
  * [Value Added Services (VAS)](https://docs.squadco.com/Value-added-services/vas/)
    * [Airtime and Data](https://docs.squadco.com/Value-added-services/vas)
    * [SMS](https://docs.squadco.com/Value-added-services/vas/)
    * [Utilities](https://docs.squadco.com/Value-added-services/vas/)


  * [](https://docs.squadco.com/)
  * Value Added Services (VAS)
  * Airtime and Data


On this page
# Airtime and Data
##### These are API suites that allow you to vend airtime and data. Please note that the equivalent value of all data and airtime vended will be deducted from your SQUAD account.[​](https://docs.squadco.com/Value-added-services/vas/#these-are-api-suites-that-allow-you-to-vend-airtime-and-data-please-note-that-the-equivalent-value-of-all-data-and-airtime-vended-will-be-deducted-from-your-squad-account "Direct link to These are API suites that allow you to vend airtime and data. Please note that the equivalent value of all data and airtime vended will be deducted from your SQUAD account.")
### API KEYS (Test Environment)[​](https://docs.squadco.com/Value-added-services/vas/#api-keys-test-environment "Direct link to API KEYS \(Test Environment\)")
  1. Create an account on our [sandbox environment](https://sandbox.squadco.com)
  2. Retrieve keys from the "API and WEBHOOKS" tab in the merchant settings page for authorisation.


**Environment base URL:**
**Test:** <https://sandbox-api-d.squadco.com>
**Production:** <https://api-d.squadco.com>
**Authorization** keys are to be passed via Headers as a Bearer token.
**Example:** Authorization: Bearer sandbox_sk_94f2b798466408ef4d19e848ee1a4d1a3e93f104046f
### Vend Airtime[​](https://docs.squadco.com/Value-added-services/vas/#vend-airtime "Direct link to Vend Airtime")
This API allows you to vend airtime. The minimum amount that can be vended is 50 naira.
POST
https://sandbox-api-d.squadco.com/vending/purchase/airtime
### This API vends Airtime
#### Parameters
##### Body
phone_number*
String
11 digit phone number. Format: : '08139011943'
amount*
Integer
Amount is in Naira.
#### Responses
200:OK
Success

```
{   
            "status": 200,   
            "success": true,   
            "message": "Success",   
            "data": {   
                "reference": "app_08139011943_5000_1690387362399",   
                "amount": "5000.00",   
                "merchant_amount": "4900.00",   
                "phone_number": "08139011943",   
                "merchant_id": "T6AGJQEY",   
                "wallet_batch_id": "20230726160242715_490000_T6AGJQEY_AIRTIME_NGN",   
                "transaction_id": "app_08139011943_5000_1690387362399",   
                "type": "airtime",   
                "action": "debit",   
                "status": "pending",   
                "meta": "{"vending_status":"pending","status_code":"301","message":"pending confirmation","phonenumber":"08139011943","transaction_id":"app_08139011943_5000_1690387362399","network":"MTN"}",   
                "createdAt": "2023-07-26T16:02:43.341Z"   
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

#### Sample Request[​](https://docs.squadco.com/Value-added-services/vas/#sample-request "Direct link to Sample Request")

```
{  
    "phone_number": "08139011943",  
    "amount": 5000  
}  

```

### Vend Data Bundles[​](https://docs.squadco.com/Value-added-services/vas/#vend-data-bundles "Direct link to Vend Data Bundles")
POST
https://sandbox-api-d.squadco.com/vending/purchase/data
### This is the data bundle vending endpoint.
#### Parameters
##### Body
phone_number*
String
11 digit phone number. Format: : '08139011943'
plan_code*
String
The plan code is gotten from the Get Plan Code endpoint and usually in the format: '1001'
#### Responses
200:OK
Success

```
{   
            "status": 200,   
            "success": true,   
            "message": "Success",   
            "data": {   
                "reference": "app_7062918558_100_1001_1679914203047",   
                "amount": "100.00",   
                "merchant_amount": "98.00",   
                "phone_number": "+2347062918558",   
                "merchant_id": "AABBCCDDEEFFGGHHJJKK",   
                "wallet_batch_id": "BC8BE65JWG44ZW7AN9KG",   
                "transaction_id": "edf867fa-8ad6-4eac-bd87-6e5f8ec9b945",   
                "type": "data",   
                "action": "debit",   
                "status": "success",   
                "meta": "{"vending_status":"success","status_code":"200","message":"successfully submitted for processing","phonenumber":"07062918558","transaction_id":"edf867fa-8ad6-4eac-bd87-6e5f8ec9b945","network":"MTN"}",   
                "createdAt": "2023-03-27T10:50:04.073Z"   
            }   
}  

```

401:Unathorized
No Authorization keys

```
{  
            "success": false,  
            "message": "",  
            "data": {}  
}  

```

403:Forbidden
Invalid/Wrong Keys

```
{  
            "success": false,  
            "message": "Merchant authentication failed",  
            "data": {}  
}  

```

#### Sample Request[​](https://docs.squadco.com/Value-added-services/vas/#sample-request-1 "Direct link to Sample Request")

```
{  
    "phone_number": "07062918558",  
    "amount": 100,  
    "plan_code": "1001"  
}  

```

### Get Data Bundles[​](https://docs.squadco.com/Value-added-services/vas/#get-data-bundles "Direct link to Get Data Bundles")
This API returns all available data bundle plans for all telcos
GET
https://sandbox-api-d.squadco.com/vending/data-bundles?network=MTN
### This API returns all available data bundle plans for all telcos
#### Parameters
##### Query
network*
String
Teleco ID: MTN, GLO, AIRTEL, 9MOBILE
#### Responses
200:OK
Success

```
{   
            "status": 200,   
            "success": true,   
            "message": "Success",   
            "data": [   
                {   
                    "plan_name": "MTN data_plan",   
                    "bundle_value": "100MB ",   
                    "bundle_validity": " Daily Plan",   
                    "bundle_description": " Daily Plan",   
                    "bundle_price": "100",   
                    "plan_code": "1001",   
                    "network": "MTN"   
                },   
                {   
                    "plan_name": "MTN data_plan",   
                    "bundle_value": "200MB",   
                    "bundle_validity": " 2-day Plan",   
                    "bundle_description": " 2-day Plan",   
                    "bundle_price": "200",   
                    "plan_code": "1002",   
                    "network": "MTN"   
                },   
                {   
                    "plan_name": "MTN data_plan",   
                    "bundle_value": "350MB",   
                    "bundle_validity": " Weekly Plan",   
                    "bundle_description": " Weekly Plan",   
                    "bundle_price": "300",   
                    "plan_code": "1003",   
                    "network": "MTN"   
                },   
                {   
                    "plan_name": "MTN data_plan",   
                    "bundle_value": "750MB",   
                    "bundle_validity": " 2-Week plan",   
                    "bundle_description": " 2-Week plan",   
                    "bundle_price": "500",   
                    "plan_code": "1004",   
                    "network": "MTN"   
                },   
                        {   
                    "plan_name": "MTN data_plan",   
                    "bundle_value": "1500GB",   
                    "bundle_validity": "365 days",   
                    "bundle_description": "365 days",   
                    "bundle_price": "450000",   
                    "plan_code": "1111",   
                    "network": "MTN"   
                }   
            ]   
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
Invalid/Wrong Keys

```
{  
            "success": false,  
            "message": "Merchant authentication failed",  
            "data": {}  
}  

```

### Retrieve Airtime and Data Transactions[​](https://docs.squadco.com/Value-added-services/vas/#retrieve-airtime-and-data-transactions "Direct link to Retrieve Airtime and Data Transactions")
This API provides details on airtime and data transactions conducted by a merchant, allowing for the use of multiple filters.
GET
https://api-d.squadco.com/vending/transactions?page=1&perPage=4&action=debit
### This API returns airtime and data transactions done by a merchant.
#### Parameters
##### Query
page*
Integer
The page of the transaction you want to view
perPage*
Integer
Number of transaction you want to view per page
action*
string
The type of transaction you want to see: 'debit'
reference*
string
Reference of the transaction you want to see
#### Responses
200:OK
Response description

```
{   
            "status": 200,   
            "success": true,   
            "message": "Success",   
            "data": {   
                "count": 5,   
                "rows": [   
                    {   
                        "reference": "app_08139011943_5000_1690387362399",   
                        "amount": "5000.00",   
                        "merchant_amount": "4900.00",   
                        "phone_number": "08139011943",   
                        "merchant_id": "T6AGJQEY",   
                        "wallet_batch_id": "20230726160242715_490000_T6AGJQEY_AIRTIME_NGN",   
                        "transaction_id": "app_08139011943_5000_1690387362399",   
                        "type": "airtime",   
                        "action": "debit",   
                        "status": "pending",   
                        "meta": "{"vending_status":"pending","status_code":"301","message":"pending confirmation","phonenumber":"08139011943","transaction_id":"app_08139011943_5000_1690387362399","network":"MTN"}",   
                        "createdAt": "2023-07-26T16:02:43.341Z"   
                    },   
                    {   
                        "reference": "app_08132448598_500_1001_1690387247434",   
                        "amount": "500.00",   
                        "merchant_amount": "490.00",   
                        "phone_number": "08132448598",   
                        "merchant_id": "T6AGJQEY",   
                        "wallet_batch_id": "20230726160047736_49000_T6AGJQEY_DATA__NGN",   
                        "transaction_id": null,   
                        "type": "data",   
                        "action": "debit",   
                        "status": "failed",   
                        "meta": null,   
                        "createdAt": "2023-07-26T16:00:48.212Z"   
                    },   
                    {   
                        "reference": "app_08139011943_5000_1001_1690387152681",   
                        "amount": "5000.00",   
                        "merchant_amount": "4900.00",   
                        "phone_number": "08139011943",   
                        "merchant_id": "T6AGJQEY",   
                        "wallet_batch_id": "20230726155914250_490000_T6AGJQEY_DATA__NGN",   
                        "transaction_id": null,   
                        "type": "data",   
                        "action": "debit",   
                        "status": "failed",   
                        "meta": null,   
                        "createdAt": "2023-07-26T15:59:15.602Z"   
                    },   
                    {   
                        "reference": "app_08139011943_5000_1690363943917",   
                        "amount": "5000.00",   
                        "merchant_amount": "4900.00",   
                        "phone_number": "08139011943",   
                        "merchant_id": "T6AGJQEY",   
                        "wallet_batch_id": "20230726093224159_490000_T6AGJQEY_AIRTIME_NGN",   
                        "transaction_id": "app_08139011943_5000_1690363943917",   
                        "type": "airtime",   
                        "action": "debit",   
                        "status": "pending",   
                        "meta": "{"vending_status":"pending","status_code":"301","message":"pending confirmation","phonenumber":"08139011943","transaction_id":"app_08139011943_5000_1690363943917","network":"MTN"}",   
                        "createdAt": "2023-07-26T09:32:24.638Z"   
                    }   
                ]   
            }   
}  

```

401:Unathorized
Response description

```
{  
            "success": false,  
            "message": "",  
            "data": {}  
}  

```

403:Forbidden
Response description

```
{  
            "success": false,  
            "message": "Merchant authentication failed",  
            "data": {}  
}  

```

### Going Live[​](https://docs.squadco.com/Value-added-services/vas/#going-live "Direct link to Going Live")
To go live, follow these steps:
  1. Change the base URL for your endpoints from **<https://sandbox-api-d.squadco.com>** to **<https://api-d.squadco.com>**.
  2. Sign up for our [Live Environment](https://dashboard.squadco.com/sign-up).
  3. Complete your Know Your Customer (KYC) process.
  4. Share your Merchant ID with the Technical Account Manager for profiling.
  5. Use the credentials provided on the live dashboard for authentication.


[](https://github.com/HabariPay/habaripay.github.io/tree/main/docs/Value-added-services/vas.mdx)
[Previous Refund API](https://docs.squadco.com/Others/refund-api)[Next Bucket](https://docs.squadco.com/Value-added-services/SMS/bucket)
  * [API KEYS (Test Environment)](https://docs.squadco.com/Value-added-services/vas/#api-keys-test-environment)
  * [Vend Airtime](https://docs.squadco.com/Value-added-services/vas/#vend-airtime)
  * [Vend Data Bundles](https://docs.squadco.com/Value-added-services/vas/#vend-data-bundles)
  * [Get Data Bundles](https://docs.squadco.com/Value-added-services/vas/#get-data-bundles)
  * [Retrieve Airtime and Data Transactions](https://docs.squadco.com/Value-added-services/vas/#retrieve-airtime-and-data-transactions)
  * [Going Live](https://docs.squadco.com/Value-added-services/vas/#going-live)


