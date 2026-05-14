# Source: https://docs.squadco.com/Value-added-services/SMS/bucket

[Skip to main content](https://docs.squadco.com/Value-added-services/SMS/bucket/#__docusaurus_skipToContent_fallback)
[![My Site Logo](https://docs.squadco.com/img/squad_logo.svg)](https://docs.squadco.com/)
Search`K`
[Support](https://squadco.com/support/)[Create Account](https://dashboard.squadco.com/sign-up)[Sign In](https://dashboard.squadco.com/login)
  * [Home](https://docs.squadco.com/)
  * [Payments](https://docs.squadco.com/Value-added-services/SMS/bucket/)
  * [Webhook & Redirect URL](https://docs.squadco.com/Value-added-services/SMS/bucket/)
  * [Virtual Accounts](https://docs.squadco.com/Value-added-services/SMS/bucket/)
  * [Transfer API](https://docs.squadco.com/Value-added-services/SMS/bucket/)
  * [Others](https://docs.squadco.com/Value-added-services/SMS/bucket/)
  * [Value Added Services (VAS)](https://docs.squadco.com/Value-added-services/SMS/bucket/)
    * [Airtime and Data](https://docs.squadco.com/Value-added-services/vas)
    * [SMS](https://docs.squadco.com/Value-added-services/SMS/bucket/)
      * [Bucket](https://docs.squadco.com/Value-added-services/SMS/bucket)
      * [SMS Template](https://docs.squadco.com/Value-added-services/SMS/template)
      * [Messages](https://docs.squadco.com/Value-added-services/SMS/message)
    * [Utilities](https://docs.squadco.com/Value-added-services/SMS/bucket/)


  * [](https://docs.squadco.com/)
  * Value Added Services (VAS)
  * SMS
  * Bucket


On this page
# Bucket
##### A bucket is a collection of phone numbers organized in Excel format.[​](https://docs.squadco.com/Value-added-services/SMS/bucket/#a-bucket-is-a-collection-of-phone-numbers-organized-in-excel-format "Direct link to A bucket is a collection of phone numbers organized in Excel format.")
### Create Bucket[​](https://docs.squadco.com/Value-added-services/SMS/bucket/#create-bucket "Direct link to Create Bucket")
This endpoint allows you to create a bucket containing a group of phone numbers for SMS communication.
POST
https://sandbox-api-d.squadco.com/sms/bucket
### This API creates SMS Bucket
#### Parameters
##### Body
name*
String
Name of Bucket
description*
String
Description of Bucket
file_name*
String
Name of the csv file to be uploaded
#### Sample Request[​](https://docs.squadco.com/Value-added-services/SMS/bucket/#sample-request "Direct link to Sample Request")

```
{  
  "name": "file1234",  
  "description": "baa baa black sheep",  
  "file_name": "teest.csv"  
}  

```

  

After a successful bucket creation request, a file path (signed_url) will be provided in the response. Please follow the link in a browser and upload a CSV file containing the list of phone numbers.
#### Responses
200:OK
Success

```
{   
    "status": 200,  
    "success": true,  
    "message": "Success",  
    "data": {  
        "uuid": "ec571a9a-0c78-4d98-9956-1e5ede72d344",  
        "status": "pending",  
        "name": "file1234",  
        "description": "baa baa black sheep",  
        "merchant_id": "AABBCCDDEEFFGGHHJJKK",  
        "updatedAt": "2025-05-22T09:34:58.800Z",  
        "createdAt": "2025-05-22T09:34:58.800Z",  
        "size": null,  
        "file_url": null,  
        "estimated_cost": null,  
        "headers": null,  
        "meta": null,  
        "signed_url": "https://s3.eu-west-2.amazonaws.com/squadinc.co-gateway-mobile-app-service-dev/bulk_sms/AABBCCDDEEFFGGHHJJKK/campaign/ec571a9a-0c78-4d98-9956-1e5ede72d344/teest.csv/1747906498860-523754.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAYPHEQVFJHOQDZNU6%2F20250522%2Feu-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250522T093458Z&X-Amz-Expires=300&X-Amz-Signature=1f1f0017519941522352b1e8496d41b7641d7a8dd800cc3948afaf8850f86e79&X-Amz-SignedHeaders=host%3Bx-amz-acl&x-amz-acl=public-read"  
      }  
}  

```

### Get All Created Bucket[​](https://docs.squadco.com/Value-added-services/SMS/bucket/#get-all-created-bucket "Direct link to Get All Created Bucket")
This endpoint allows you to retrieve created buckets
GET
https://sandbox-api-d.squadco.com/sms/bucket
### This API retrieves all Bucket
#### Responses
200:OK
Success

```
{   
    "status": 200,  
    "success": true,  
    "message": "Success",  
    "data": {  
        "count": 2,  
        "rows": [  
            {  
                "uuid": "ec571a9a-0c78-4d98-9956-1e5ede72d344",  
                "merchant_id": "AABBCCDDEEFFGGHHJJKK",  
                "name": "file1234",  
                "description": "baa baa black sheep",  
                "size": null,  
                "file_url": null,  
                "estimated_cost": null,  
                "headers": null,  
                "status": "pending",  
                "meta": null,  
                "createdAt": "2025-05-22T09:34:58.800Z",  
                "updatedAt": "2025-05-22T09:34:58.800Z"  
            },  
            {  
                "uuid": "0f704e13-7b52-4ceb-a3ee-a1a253d14d97",  
                "merchant_id": "AABBCCDDEEFFGGHHJJKK",  
                "name": "file123",  
                "description": "baa baa black sheep",  
                "size": null,  
                "file_url": null,  
                "estimated_cost": null,  
                "headers": null,  
                "status": "pending",  
                "meta": null,  
                "createdAt": "2025-05-21T16:03:17.357Z",  
                "updatedAt": "2025-05-21T16:03:17.357Z"  
            }  
        ]  
    }  
  
}  

```

### Delete Created Bucket[​](https://docs.squadco.com/Value-added-services/SMS/bucket/#delete-created-bucket "Direct link to Delete Created Bucket")
This endpoint allows you to delete a bucket
POST
https://sandbox-api-d.squadco.com/sms/bucket/{{:uuid}}
### This API deletes created Bucket
#### Responses
200:OK
Success

```
{   
        "status": 200,  
        "success": true,  
        "message": "Success",  
        "data": {  
            "uuid": "c51dca18-0458-415d-b0d7-0a03754fb8a0",  
            "merchant_id": "SBS5B8VU36",  
            "name": "file12341",  
            "description": "baa baa black sheep",  
            "size": null,  
            "file_url": null,  
            "estimated_cost": null,  
            "headers": null,  
            "status": "pending",  
            "meta": null,  
            "createdAt": "2025-05-24T09:24:42.549Z",  
            "updatedAt": "2025-05-24T09:24:42.549Z"  
        }  
}  

```

[](https://github.com/HabariPay/habaripay.github.io/tree/main/docs/Value-added-services/SMS/bucket.mdx)
[Previous Airtime and Data](https://docs.squadco.com/Value-added-services/vas)[Next SMS Template](https://docs.squadco.com/Value-added-services/SMS/template)
  * [Create Bucket](https://docs.squadco.com/Value-added-services/SMS/bucket/#create-bucket)
  * [Get All Created Bucket](https://docs.squadco.com/Value-added-services/SMS/bucket/#get-all-created-bucket)
  * [Delete Created Bucket](https://docs.squadco.com/Value-added-services/SMS/bucket/#delete-created-bucket)


