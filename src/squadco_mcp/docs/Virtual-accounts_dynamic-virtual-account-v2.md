# Source: https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2/

[Skip to main content](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2/#__docusaurus_skipToContent_fallback)
[![My Site Logo](https://docs.squadco.com/img/squad_logo.svg)](https://docs.squadco.com/)
Search`K`
[Support](https://squadco.com/support/)[Create Account](https://dashboard.squadco.com/sign-up)[Sign In](https://dashboard.squadco.com/login)
  * [Home](https://docs.squadco.com/)
  * [Payments](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2/)
  * [Webhook & Redirect URL](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2/)
  * [Virtual Accounts](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2/)
    * [Virtual Accounts](https://docs.squadco.com/Virtual-accounts/virtual-account)
    * [API Specifications](https://docs.squadco.com/Virtual-accounts/api-specifications)
    * [Encryption & Decryption](https://docs.squadco.com/Virtual-accounts/encryption-decryption)
    * [Dynamic Virtual Account Overview](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2)
  * [Transfer API](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2/)
  * [Others](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2/)
  * [Value Added Services (VAS)](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2/)


  * [](https://docs.squadco.com/)
  * Virtual Accounts
  * Dynamic Virtual Account Overview


On this page
# Dynamic Virtual Account Overview
This module provides APIs to generate a pool of Virtual Accounts that can be assigned on a transaction-by-transaction basis. You can set parameters such as expiry time, transaction reference, and the amount to be collected.
Please be aware that all newly created accounts will now show the merchant's business name instead of the previous standard, "SQUAD CHECKOUT." The new format will be "SQUAD_MERCHANT BUSINESS NAME." Existing accounts will remain unaffected by this change.
Once you create the pool of accounts, the system will automatically assign accounts from your pool on a transaction basis. It includes various webhook notifications for events such as mismatches, expirations, and successful transactions. There is also a re-query endpoint to check all transactions that have been queued for refunds and those that have already been refunded.
**Important:** To create dynamic virtual accounts for your pool, your KYC account must be a GTB account number mapped to the provided BVN.
### Process Flow[​](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2/#process-flow "Direct link to Process Flow")
  1. All accounts must be profiled before you can use this service, as it is restricted to selected businesses. Please send an email to help@squadco.com or growth@habaripay.com to request permission to use this service.
  2. Each merchant is assigned a separate pool of accounts and is expected to create accounts based on their use case and anticipated transaction volume.
  3. To initiate a transaction, the merchant should call the Generate Dynamic Virtual Account endpoint. An account from your specific pool will be assigned for the transaction, and it will be linked to the amount and duration you have specified.
  4. Webhook notifications will be triggered for three events: SUCCESS, EXPIRED, and MISMATCH.
  5. There is a re-query feature that provides all payment attempts for a single transaction reference, returning an array that includes the status of each attempt (SUCCESS, EXPIRED, or MISMATCH where applicable).


### API KEYS (Test Environment)[​](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2/#api-keys-test-environment "Direct link to API KEYS \(Test Environment\)")
  1. Create an account in our [sandbox environment](https://sandbox.squadco.com).
  2. Share your Merchant ID with the Technical Account Managers for profiling.
  3. Retrieve authorization keys from the "API and WEBHOOKS" tab in the "Merchant Settings" page.


### Create Dynamic VA Accounts[​](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2/#create-dynamic-va-accounts "Direct link to Create Dynamic VA Accounts")
This feature allows you to create and assign dynamic virtual accounts to your pool. Note that only one account is generated per request.
POST
https://sandbox-api-d.squadco.com/virtual-account/create-dynamic-virtual-account
### This allows you create and assign dynamic virtual accounts to your pool
#### Parameters
##### Body
first_name*
String
Optional custom first name for the virtual account
last_name*
String
Optional custom last name for the virtual account
beneficiary_account*
Integer
Optional GTBank account number for instant settlement
#### Responses
200:OK
Success

```
{  
              "status": 200,  
              "success": true,  
              "message": "Success",  
              "data": {}  
  }  

```

400:Bad Request
Bad Request

```
{  
            "status": 400,  
            "success": false,  
            "message": "You are not allowed to pass first_name and last_name",  
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
Invalid/Wrong Authorization

```
{  
              "success": false,  
              "message": "Merchant authentication failed",  
              "data": {}  
  }  

```

  

### Instant Settlement[​](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2/#instant-settlement "Direct link to Instant Settlement")
For instant settlement to GTBank corporate account, please include the beneficiary_account key in the request body with a GTBank account number. Only GTBank accounts are acceptable.
#### Sample request[​](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2/#sample-request "Direct link to Sample request")

```
{  
"beneficiary_account": "0147799000"  
}  

```

### Custom DVA name[​](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2/#custom-dva-name "Direct link to Custom DVA name")
When you request a customized business name for your virtual accounts, please include the "first_name" and "last_name" fields along with their corresponding values in the request body. Note that only authorized merchants can access this feature. Additionally, ensure that all account names within a pool are identical, as the system will randomly select accounts from this pool.
#### Sample request[​](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2/#sample-request-1 "Direct link to Sample request")

```
{  
 "first_name": "Habaripay",  
 "last_name": "Limited"  
 }  

```

### Initiate Dynamic Virtual Account Transaction[​](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2/#initiate-dynamic-virtual-account-transaction "Direct link to Initiate Dynamic Virtual Account Transaction")
This API allows you to retrieve a Dynamic Virtual Account from the pool of accounts to be assigned for collection. This is used to initiate a transaction.
POST
https://sandbox-api-d.squadco.com/virtual-account/initiate-dynamic-virtual-account
### This API allows you fetch a Dynamic Virtual Account to be assigned to a customer
This API allows you to retrieve a Dynamic Virtual Account from the pool of accounts to be assigned for collection. This is used to initiate a transaction.
#### Parameters
##### Body
amount*
Integer
Amount is in Kobo
duration*
Integer
Time allowed before an account/transaction is expired. Duration is in seconds. i.e duration:60 = 1 minute
email*
string
a valid email address for notification to customer
transaction_ref*
string
Unique transaction Reference that identifies the transaction on your system
#### Responses
200:OK
Success

```
{  
              "status": 200,  
              "success": true,  
              "message": "Success",  
              "data": {  
                  "is_blocked": false,  
                  "account_name": "SQUAD CHECKOUT",  
                  "account_number": "4879261135",  
                  "expected_amount": "100.00",  
                  "expires_at": "2023-08-08T08:23:27.791Z",  
                  "transaction_reference": "dva123",  
                  "bank": "GTBank",  
                  "currency": "NGN"  
              }  
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

#### Sample Request[​](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2/#sample-request-2 "Direct link to Sample Request")

```
{  
    "amount":100,  
    "transaction_ref":"Aq1111BddCDqdddqdqqEw2",  
    "duration":600,  
    "email":"hittommyi02@gmail.com"  
}  

```

### Re-query Transaction[​](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2/#re-query-transaction "Direct link to Re-query Transaction")
This API facilitates the ability to re-query a transaction in order to ascertain its status. It presents a comprehensive array of all transaction attempts, encompassing those that resulted in MISMATCH, those that EXPIRED, and those that were SUCCESSFULLY completed. It is important to note that all EXPIRED and MISMATCH transactions will be subject to a refund by our system.
GET
https://sandbox-api-d.squadco.com/virtual-account/get-dynamic-virtual-account-transactions/:transaction_reference
### This API allows you re-query a transaction to check it's status.
This API allows you to re-query a transaction to check its status. It provides an array of all transaction attempts, including those that resulted in a mismatch, those that expired, and the successful transactions. Ultimately, all expired and mismatched transactions will be refunded.
#### Parameters
##### Path
transaction_reference*
String
Merchant's transaction reference passed when initiating / generating the dynamic virtual account.
#### Responses
200:OK
Success

```
{  
              "status": 200,  
              "success": true,  
              "message": "Success",  
              "data": {  
                  "count": 3,  
                  "rows": [  
                      {  
                          "transaction_status": "EXPIRED",  
                          "transaction_reference": "Aq1111BddCDqdddqdqqEw4",  
                          "created_at": "2023-08-08T07:02:59.672Z",  
                          "refund": false  
                      },  
                      {  
                          "transaction_status": "SUCCESS",  
                          "transaction_reference": "Aq1111BddCDqdddqdqqEw4",  
                          "created_at": "2023-08-08T07:02:54.052Z",  
                          "refund": null  
                      },  
                      {  
                          "transaction_status": "MISMATCH",  
                          "transaction_reference": "Aq1111BddCDqdddqdqqEw4",  
                          "created_at": "2023-08-08T07:02:29.392Z",  
                          "refund": false  
                      }  
                  ]  
              }  
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

### Edit Amount/Duration[​](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2/#edit-amountduration "Direct link to Edit Amount/Duration")
This API is used to modify the amount and duration of a dynamic transaction that has already been initiated. It takes the transaction reference, the amount, and the duration.
PATCH
https://sandbox-api-d.squadco.com/virtual-account/update-dynamic-virtual-account-time-and-amount
### This API allows you to edit the amount/duration of a dynamic transaction
#### Parameters
##### Body
transaction_reference*
String
The transaction ref of the already initiated transaction.
amount*
Integer
Amount is in Kobo
duration*
Integer
Amount of time before transaction expires. Duration is in seconds.
#### Responses
200:OK
Success

```
{  
              "status": 200,  
              "success": true,  
              "message": "Success",  
              "data": {  
                  "account_number": "0852491446",  
                  "currency": "NGN",  
                  "amount": 5000,  
                  "expires_at": "2023-08-30T17:01:46.973Z",  
                  "transaction_reference": "ify21"  
              }  
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

404:Not Found
Invalid Transaction Ref

```
{  
              "status": 404,  
              "success": false,  
              "message": "Transaction not found",  
              "data": {}  
  }  

```

#### Sample Request[​](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2/#sample-request-3 "Direct link to Sample Request")

```
{  
    "transaction_reference": "ify21",  
    "amount": 5000  
}  

```

### Simulate Payment Endpoint[​](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2/#simulate-payment-endpoint "Direct link to Simulate Payment Endpoint")
This API is designed for the purpose of submitting test transactions. It is important to note that this API should only be utilized within the sandbox environment.
POST
https://sandbox-api-d.squadco.com/virtual-account/simulate/payment
### This is to be used only on the sandbox environment to do test transactions. 
#### Parameters
##### Body
virtual_account_number*
String
10-digit Dynamic Account gotten after initiating a virtual transfer. 
amount*
String
Amount is in naira. This is the expected amount to be transferred into the dynamic virtual account.
dva*
boolean
true
#### Responses
200:OK
Success

```
{  
              "status": 200,  
              "success": true,  
              "message": "Success",  
              "data": "Payment successful"  
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

## DVA Refunds[​](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2/#dva-refunds "Direct link to DVA Refunds")
As previously mentioned in this documentation, customers are required to pay the exact amount specified for each initiated Dynamic Virtual Account (DVA) within the designated time frame. If a customer fails to do so (resulting in a mismatched or expired transaction), the default procedure is for the customer to receive an automatic refund.
However, in cases where merchants prefer to have the mismatched or expired funds settled directly to them and assume the responsibility of refunding their customers, this can now be arranged. Expired or mismatched DVA transactions will be processed to one of the following options:
  1. Merchant's Dashboard
  2. Merchant's GTBank Settlement Account
  3. Sub-Merchant's Wallet


### Process Flow[​](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2/#process-flow-1 "Direct link to Process Flow")
  1. To initiate this process, a merchant must submit a written request via email for any of the profiling options. The email should include:


  * Merchant ID
  * The preferred settlement location for the mismatched or expired transactions (Merchant Dashboard, GTBank Settlement Account, or Sub-Merchant Wallet)


  1. The email should be sent to the Key Account Manager, with growth@squadco.com copied on the correspondence.
  2. If the request is approved, the merchant will be internally profiled and notified accordingly.


## Webhooks[​](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2/#webhooks "Direct link to Webhooks")
To set up your webhook, please visit your squad dashboard and navigate to the merchant settings page. There, you will find a field labeled 'Webhook URL' under the API & Webhook tab. Only accounts with a valid webhook URL will receive notifications.
Webhook notifications are sent for three different events/statuses:
  1. **Success** : This occurs when the first transfer/transaction meets the expected/specified amount and is completed within the designated time frame.
  2. **Mismatch** : This happens when a transfer occurs within the specified duration, but the transferred amount does not match the expected amount.
  3. **Expired** : This status is triggered when a transaction occurs after the set duration, or after a successful transaction has already been recorded, regardless of whether the transferred amount is equal to the expected amount.


#### Sample Webhook Notification (Success)[​](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2/#sample-webhook-notification-success "Direct link to Sample Webhook Notification \(Success\)")

```
{  
  "transaction_status": "SUCCESS",  
  "merchant_reference": "test55",  
  "merchant_amount": "100.00",  
  "amount_received": "100.00",  
  "transaction_reference": "REF20250321S51557521_M01282553_0855445055",  
  "email": "williamudousoro@gmail.com",  
  "merchant_id": "P7SJ3KMH",  
  "sub_merchant_id": null,  
  "transaction_type": "dynamic_virtual_account",  
  "date": "2025-03-21T08:52:42.729Z",  
  "sender_name": "WILLIAM  JOSEPH UDOUSORO"  
}  

```

#### Sample Webhook Notification (Expired)[​](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2/#sample-webhook-notification-expired "Direct link to Sample Webhook Notification \(Expired\)")

```
{  
  "transaction_status": "EXPIRED",  
  "merchant_reference": "test55",  
  "merchant_amount": "100.00",  
  "amount_received": "100.00",  
  "transaction_reference": "REF20250321S51557521_M01282553_0855445055",  
  "email": "williamudousoro@gmail.com",  
  "merchant_id": "P7SJ3KMH",  
  "sub_merchant_id": null,  
  "transaction_type": "dynamic_virtual_account",  
  "date": "2025-03-22T08:52:42.729Z",  
  "sender_name": "WILLIAM  JOSEPH UDOUSORO"  
}  

```

#### Sample Webhook Notification (Mismatch)[​](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2/#sample-webhook-notification-mismatch "Direct link to Sample Webhook Notification \(Mismatch\)")

```
{  
  "transaction_status": "MISMATCH",  
  "merchant_reference": "test55",  
  "merchant_amount": "100.00",  
  "amount_received": "102.00",  
  "transaction_reference": "REF20250321S51557521_M01282553_0855445055",  
  "email": "williamudousoro@gmail.com",  
  "merchant_id": "P7SJ3KMH",  
  "sub_merchant_id": null,  
  "transaction_type": "dynamic_virtual_account",  
  "date": "2025-03-21T08:52:42.729Z",  
  "sender_name": "WILLIAM  JOSEPH UDOUSORO"  
}  

```

## Hash Signature Validation[​](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2/#hash-signature-validation "Direct link to Hash Signature Validation")
Every webhook request includes a hash signature in the request header. As a security measure, you are required to create a hash and compare it to the hash sent in the header. This hash is a SHA-512 hash generated from specific parameters in the payload, using your squad's secret/private key.
The signature in the header is identified by the key: **x-squad-encrypted-body**.
#### Webhook Payload to be hashed[​](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2/#webhook-payload-to-be-hashed "Direct link to Webhook Payload to be hashed")
Below are the parameters that need to be hashed from the webhook payload:

```
{  
 transaction_reference: "REF202308010384993",  
 amount_received: "3000",  
 merchant_reference: "test_1",  
}  

```

### Sample Implementation[​](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2/#sample-implementation "Direct link to Sample Implementation")
  * C#



```
  using System;  
  using System.Collections.Generic;  
  using System.Security.Cryptography;  
  using System.Text;  
  using System.Text.Json;  
  
  public class Program  
  {  
      public static void Main()  
      {  
          string secretKey = "sandbox_sk_1sfsdfa9c3b324241e19dfd25ac0c797193fd7cca";  
  
    
          string receivedSignature = "16be3425345ccbd37b98b5e3983da18a1becf1d78e87cf3dc59b6f685fe2bfa07d9a5dc3830599c078e3199aa3a67dc39197b98b1fe386b493ab1ac970bdfd0d5";  
  
            
          var verificationData = new  
          {  
              transaction_reference = "REF20250730S40083324_M1023327831_0900939602",  
              amount_received = "200.00",  
              merchant_reference = "sample101ssdxcvxxcs"  
          };  
  
          
          bool isValid = VerifyHashHelper(verificationData, receivedSignature, secretKey);  
  
          Console.WriteLine("\n--- RESULT ---");  
          Console.WriteLine("Signature Match: " + isValid);  
      }  
  
      private static bool VerifyHashHelper(object value, string authHeader, string secretKey)  
      {  
          if (string.IsNullOrEmpty(secretKey))  
              throw new InvalidOperationException("Secret key is not configured");  
  
          byte[] keyBytes = Encoding.UTF8.GetBytes(secretKey);  
  
            
          var dict = new Dictionary<string, string>  
          {  
              { "transaction_reference", ((dynamic)value).transaction_reference },  
              { "amount_received", ((dynamic)value).amount_received },  
              { "merchant_reference", ((dynamic)value).merchant_reference }  
          };  
  
          var jsonOptions = new JsonSerializerOptions  
          {  
              WriteIndented = false,  
  #if NET6_0_OR_GREATER  
              DefaultIgnoreCondition = System.Text.Json.Serialization.JsonIgnoreCondition.WhenWritingNull  
  #else  
              IgnoreNullValues = true  
  #endif  
          };  
  
          string jsonValue = JsonSerializer.Serialize(dict, jsonOptions);  
  
          Console.WriteLine("JSON used for hashing:");  
          Console.WriteLine(jsonValue);  
  
          byte[] dataBytes = Encoding.UTF8.GetBytes(jsonValue);  
  
          using (var hmac = new HMACSHA512(keyBytes))  
          {  
              byte[] hash = hmac.ComputeHash(dataBytes);  
              string result = BitConverter.ToString(hash).Replace("-", "").ToLower();  
  
              Console.WriteLine("\nGenerated Signature:");  
              Console.WriteLine(result);  
  
              return result.Equals(authHeader, StringComparison.OrdinalIgnoreCase);  
          }  
      }  
  }  

```

#### Webhook Error Log[​](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2/#webhook-error-log "Direct link to Webhook Error Log")
This contains all missed webhook notifications that we didn't get a 200 response for. The aim of this is to mitigate against missed webhooks. [Click to open API specifications](https://docs.squadco.com/Virtual-accounts/api-specifications#webhook-error-log)
#### Sample Error Log Response for DVA[​](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2/#sample-error-log-response-for-dva "Direct link to Sample Error Log Response for DVA")

```
{  
    "status": 200,  
    "success": true,  
    "message": "Success",  
    "data": {  
        "count": 2,  
        "rows": [  
            {  
                "id": "2dc56eb3-d997-4e68-adf9-53b603c16a43",  
                "payload": {  
                    "date": "2023-08-09T15:09:54.958Z",  
                    "email": "igwehifeanyi02@gmail.com",  
                    "merchant_id": "SBN1EBZEQ8",  
                    "amount_received": "100.00",  
                    "merchant_amount": "100.00",  
                    "transaction_type": "dynamic_virtual_account",  
                    "merchant_reference": "C2",  
                    "transaction_status": "SUCCESS",  
                    "transaction_reference": "REF7VDV8JV25/1691593794798"  
                },  
                "transaction_ref": "REF7VDV8JV25/1691593794798"  
            },  
            {  
                "id": "b7983af4-ad3e-40ef-91d4-55af04bb2173",  
                "payload": {  
                    "date": "2023-08-09T15:04:41.017Z",  
                    "email": "igwehifeanyi02@gmail.com",  
                    "merchant_id": "SBN1EBZEQ8",  
                    "amount_received": "100.00",  
                    "merchant_amount": "100.00",  
                    "transaction_type": "dynamic_virtual_account",  
                    "merchant_reference": "Cw2",  
                    "transaction_status": "SUCCESS",  
                    "transaction_reference": "REFANGDGNQ1N/1691593480709"  
                },  
                "transaction_ref": "REFANGDGNQ1N/1691593480709"  
            }  
        ]  
    }  
}  

```

[](https://github.com/HabariPay/habaripay.github.io/tree/main/docs/Virtual-accounts/dynamic-virtual-account-v2.mdx)
[Previous Encryption & Decryption](https://docs.squadco.com/Virtual-accounts/encryption-decryption)[Next Transfer API](https://docs.squadco.com/Transfer-API/transfer-apis)
  * [Process Flow](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2/#process-flow)
  * [API KEYS (Test Environment)](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2/#api-keys-test-environment)
  * [Create Dynamic VA Accounts](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2/#create-dynamic-va-accounts)
  * [Instant Settlement](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2/#instant-settlement)
  * [Custom DVA name](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2/#custom-dva-name)
  * [Initiate Dynamic Virtual Account Transaction](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2/#initiate-dynamic-virtual-account-transaction)
  * [Re-query Transaction](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2/#re-query-transaction)
  * [Edit Amount/Duration](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2/#edit-amountduration)
  * [Simulate Payment Endpoint](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2/#simulate-payment-endpoint)
  * [DVA Refunds](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2/#dva-refunds)
    * [Process Flow](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2/#process-flow-1)
  * [Webhooks](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2/#webhooks)
  * [Hash Signature Validation](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2/#hash-signature-validation)
    * [Sample Implementation](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2/#sample-implementation)


