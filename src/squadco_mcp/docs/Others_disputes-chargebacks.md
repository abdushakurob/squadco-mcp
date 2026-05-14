# Source: https://docs.squadco.com/Others/disputes-chargebacks/

[Skip to main content](https://docs.squadco.com/Others/disputes-chargebacks/#__docusaurus_skipToContent_fallback)
[![My Site Logo](https://docs.squadco.com/img/squad_logo.svg)](https://docs.squadco.com/)
Search`K`
[Support](https://squadco.com/support/)[Create Account](https://dashboard.squadco.com/sign-up)[Sign In](https://dashboard.squadco.com/login)
  * [Home](https://docs.squadco.com/)
  * [Payments](https://docs.squadco.com/Others/disputes-chargebacks/)
  * [Webhook & Redirect URL](https://docs.squadco.com/Others/disputes-chargebacks/)
  * [Virtual Accounts](https://docs.squadco.com/Others/disputes-chargebacks/)
  * [Transfer API](https://docs.squadco.com/Others/disputes-chargebacks/)
  * [Others](https://docs.squadco.com/Others/disputes-chargebacks/)
    * [Disputes & Chargebacks](https://docs.squadco.com/Others/disputes-chargebacks)
    * [Refund API](https://docs.squadco.com/Others/refund-api)
  * [Value Added Services (VAS)](https://docs.squadco.com/Others/disputes-chargebacks/)


  * [](https://docs.squadco.com/)
  * Others
  * Disputes & Chargebacks


On this page
# Disputes & Chargebacks
##### This contains a list of APIs that allow you get all disputes raised on your transaction, reject the claim with an evidence or accept the claim and accept a charge back to be performed.[​](https://docs.squadco.com/Others/disputes-chargebacks/#this-contains-a-list-of-apis-that-allow-you-get-all-disputes-raised-on-your-transaction-reject-the-claim-with-an-evidence-or-accept-the-claim-and-accept-a-charge-back-to-be-performed "Direct link to This contains a list of APIs that allow you get all disputes raised on your transaction, reject the claim with an evidence or accept the claim and accept a charge back to be performed.")
You have the option to either accept or reject a chargeback
### Accepting a chargeback:[​](https://docs.squadco.com/Others/disputes-chargebacks/#accepting-a-chargeback "Direct link to Accepting a chargeback:")
This means you received the customer’s payment but did not provide the service or product the customer requested for some reasons. When you accept a chargeback, you allow for the funds to be deducted from your payouts and reversed to the customer’s bank account.
### Rejecting a chargeback:[​](https://docs.squadco.com/Others/disputes-chargebacks/#rejecting-a-chargeback "Direct link to Rejecting a chargeback:")
This means you received the customer’s payment and have provided the service or delivered the product to the customer. To justify your claim you are required to provide an evidence to show that value has been given for payment made by the customer. If the evidence is not sufficient, we will automatically accept the chargeback.
**Environment base URL:**
**Test:** <https://sandbox-api-d.squadco.com>
**Production:** <https://api-d.squadco.com>
**Authorization** keys are to be passed via Headers as a Bearer token.
**Example:** Authorization: Bearer sandbox_sk_94f2b798466408ef4d19e848ee1a4d1a3e93f104046f
## GET ALL DISPUTES[​](https://docs.squadco.com/Others/disputes-chargebacks/#get-all-disputes "Direct link to GET ALL DISPUTES")
This API is used to get all disputes on your transactions raised by your customers.
GET
https://sandbox-api-d.squadco.com/dispute
### All you need to do is make a get request with your private/secret key
#### Responses
200:OK
Success

```
{ // Response   
}   
              

```

401:Unathorized
No API Key

```
{ // Response   
}  
              

```

### Get Upload URL[​](https://docs.squadco.com/Others/disputes-chargebacks/#get-upload-url "Direct link to Get Upload URL")
This API is used to get a unique URL to upload an evidence(file) which is a proof or reason to reject a dispute. This is only necessary when we want to reject a dispute.
GET
https://sandbox-api-d.squadco.com/dispute/upload-url/:ticket_id/:file_name
### All you need to do is make a get request with your private/secret key
#### Parameters
##### Path
ticket_id*
String
file_name*
String
### Resolve Disputes[​](https://docs.squadco.com/Others/disputes-chargebacks/#resolve-disputes "Direct link to Resolve Disputes")
This API is used to resolve a dispute by either accepting or rejecting it.
GET
https://sandbox-api-d.squadco.com/dispute/:ticked_id/resolve
### This API is used to resolve a dispute by either accepting or rejecting it. 
#### Parameters
##### Path
ticket_id*
String
A unique ID that identifies the dispute you want to reject or accept
##### Body
action*
String
This is the action you want to be taken on the raised dispute. The value of this action can be either 'rejected' or 'accepted'
file_name*
String
The name of the file uploaded
### GO LIVE - Production[​](https://docs.squadco.com/Others/disputes-chargebacks/#go-live---production "Direct link to GO LIVE - Production")
To Use this API on production:
  1. Kindly change the base URL of the endpoint from <https://sandbox-api-d.squadco.com> to <https://api-d.squadco.com>
  2. Get production keys from your [live account](https://squadco.com) and replace the test authorization keys.


[](https://github.com/HabariPay/habaripay.github.io/tree/main/docs/Others/disputes-chargebacks.mdx)
[Previous Ledger Balance](https://docs.squadco.com/Transfer-API/ledger-balance)[Next Refund API](https://docs.squadco.com/Others/refund-api)
  * [Accepting a chargeback:](https://docs.squadco.com/Others/disputes-chargebacks/#accepting-a-chargeback)
  * [Rejecting a chargeback:](https://docs.squadco.com/Others/disputes-chargebacks/#rejecting-a-chargeback)
  * [GET ALL DISPUTES](https://docs.squadco.com/Others/disputes-chargebacks/#get-all-disputes)
    * [Get Upload URL](https://docs.squadco.com/Others/disputes-chargebacks/#get-upload-url)
    * [Resolve Disputes](https://docs.squadco.com/Others/disputes-chargebacks/#resolve-disputes)
    * [GO LIVE - Production](https://docs.squadco.com/Others/disputes-chargebacks/#go-live---production)


