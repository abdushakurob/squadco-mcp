# Source: https://docs.squadco.com/Payments/squad-payment-modal/

[Skip to main content](https://docs.squadco.com/Payments/squad-payment-modal/#__docusaurus_skipToContent_fallback)
[![My Site Logo](https://docs.squadco.com/img/squad_logo.svg)](https://docs.squadco.com/)
Search`K`
[Support](https://squadco.com/support/)[Create Account](https://dashboard.squadco.com/sign-up)[Sign In](https://dashboard.squadco.com/login)
  * [Home](https://docs.squadco.com/)
  * [Payments](https://docs.squadco.com/Payments/squad-payment-modal/)
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
  * [Webhook & Redirect URL](https://docs.squadco.com/Payments/squad-payment-modal/)
  * [Virtual Accounts](https://docs.squadco.com/Payments/squad-payment-modal/)
  * [Transfer API](https://docs.squadco.com/Payments/squad-payment-modal/)
  * [Others](https://docs.squadco.com/Payments/squad-payment-modal/)
  * [Value Added Services (VAS)](https://docs.squadco.com/Payments/squad-payment-modal/)


  * [](https://docs.squadco.com/)
  * Payments
  * Squad Payment Modal


On this page
# Squad Payment Modal
### Payment Modal[​](https://docs.squadco.com/Payments/squad-payment-modal/#payment-modal "Direct link to Payment Modal")
Squad Payment Modal provides an easy and convenient payment flow. It is the simplest way to securely collect payments from your customers without them leaving your website. The customer will be shown all the payment methods you have selected.
Integration is quick and seamless —simply copy the code from the embed section and paste it into your page, providing the easiest way to start accepting payments.
### Parameters[​](https://docs.squadco.com/Payments/squad-payment-modal/#parameters "Direct link to Parameters")
To initialize a transaction, you need to pass details such as email, first name, last name, amount, transaction reference, etc. Email, amount, and currency are **required**. You can also pass any other additional information in the _metadata_ object field. The following is a complete list of parameters that you can pass:  
| PARAMETERS  | REQUIRED?  | DESCRIPTION  |  
| --- | --- | --- |  
| key  | Yes  | Your Squad public key. Use the test key found in your [Sandbox account](https://sandbox.squadco.com/login) in test mode, and use the live key found in your [Squad dashboard](https://dashboard.squadco.com/login) in live mode.  |  
| email  | Yes  | Customer's email address.  |  
| amount  | Yes  | The amount you are debiting customer (expressed in the lowest currency value - **kobo** & **cent**).  |  
| transaction_ref  | No  | Unique case-sensitive transaction reference. If you do not pass this parameter, Squad will generate a unique reference for you.  |  
| currency_code  | Yes  | The currency you want the amount to be charged in. Allowed value is **NGN** or **USD**.  |  
| payment_channels  | No  | An array of payment channels to control what channels you want to make available for the user to make a payment with. Available channels include; [**'card'** , **'bank'** , **'ussd'** , **'transfer'**]  |  
| customer_name  | No  | Name of Customer  |  
| callback_url  | No  | Sample: <https://squadco.com>  |  
| metadata  | No  | Object that contains any additional information that you want to record with the transaction. The _custom fields in the object_ will be returned via webhook and the payment verification endpoint.  |  
| pass_charge  | No  | It takes two possible values: True or False. It is set to False by default. When set to True, the charges on the transaction is computed and passed on to the customer(payer). But when set to False, the charge is passed to the merchant and will be deducted from the amount to be settled to the merchant.  |  
The customer information can either be retrieved from a form, or from your database if you already have it stored. (Example below)
### Code Glossary[​](https://docs.squadco.com/Payments/squad-payment-modal/#code-glossary "Direct link to Code Glossary")
  * HTML
  * JavaScript



```
<!DOCTYPE html>  
<html lang="en">  
<HEAD>  
<TITLE>SQUAD</TITLE>  
<!-- bootstrap -->  
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">  
  
</HEAD>  
<BODY>  
  <form style="padding-left: 30px;" class="text-center">  
      <div class="text-left" style="color:red; font-family: Verdana; font-size: 30px;">SAMPLE CHECKOUT</div>  
      <h6>Note: Amount should be between $1 to $10,000 (USD), NGN100 to NGN5,000,000 and KSH100 to KSH5,000,000</h6>  
      <div class="row text-center">  
        <div class="col-lg-4">  
            <label for="email">Email Address</label>  
            <input type="email" id="email-address" class="form-control" required /><br>  
        </div>  
        <div class="col-lg-4">  
            <label for="amount">Amount</label>  
            <input type="tel" id="amount" class="form-control" required /><br>  
        </div>  
      </div>  
      <div class="row">  
        <div class="col-lg-4">  
            <label for="first-name">First Name</label>  
            <input type="text" id="first-name" class="form-control" /><br>  
        </div>  
        <div class="col-lg-4">  
            <label for="last-name">Last Name</label>  
            <input type="text" id="last-name" class="form-control" /><br>  
        </div>  
      </div>  
      <div class="col-lg-4">  
        <div class="form-submit">  
          <button type="button" onclick="SquadPay()" class="btn btn-danger">Check Out</button><br><br>  
        </div>  
      </div>  
    </div>  
  </form>  
</BODY>  
</HTML>  

```


```
<script src="https://checkout.squadco.com/widget/squad.min.js"></script>;  
  
function SquadPay() {  
  const squadInstance = new squad({  
    onClose: () => console.log("Widget closed"),  
    onLoad: () => console.log("Widget loaded successfully"),  
    onSuccess: () => console.log(`Linked successfully`),  
    key: "test_pk_sample-public-key-1",  
    //Change key (test_pk_sample-public-key-1) to the key on your Squad Dashboard  
    email: document.getElementById("email-address").value,  
    amount: document.getElementById("amount").value * 100,  
    //Enter amount in Naira or Dollar (Base value Kobo/cent already multiplied by 100)  
    currency_code: "NGN",  
  });  
  squadInstance.setup();  
  squadInstance.open();  
}  

```

### Initiate transaction[​](https://docs.squadco.com/Payments/squad-payment-modal/#initiate-transaction "Direct link to Initiate transaction")
When the customer clicks the **submit** button, use the provided JavaScript function to initiate a transaction by passing the required parameters (such as email, amount, and any additional fields).

```
function SquadPay() {  
  const squadInstance = new squad({  
    onClose: () => console.log("Widget closed"),  
    onLoad: () => console.log("Widget loaded successfully"),  
    onSuccess: () => console.log(`Linked successfully`),  
    key: "test_pk_sample-public-key-1",  
    //Change key (test_pk_sample-public-key-1) to the key on your Squad Dashboard  
    email: document.getElementById("email-address").value,  
    amount: document.getElementById("amount").value * 100,  
    //Enter amount in Naira or Dollar (Base value Kobo/cent already multiplied by 100)  
    currency_code: "NGN",  
  });  
  squadInstance.setup();  
  squadInstance.open();  
}  

```

A checkout modal will pop-up with different payment options for the customer to choose and input their payment information to complete the transaction.
### Checkout Demo[​](https://docs.squadco.com/Payments/squad-payment-modal/#checkout-demo "Direct link to Checkout Demo")
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

### Key Information[​](https://docs.squadco.com/Payments/squad-payment-modal/#key-information "Direct link to Key Information")
  1. The key field takes your Squad key.
  2. By default, the amount field is already set in the lowest currency unit (kobo, cent). That is, to pay **NGN100** , you have to enter **10000** in the amount field. To convert amount to the base currency (Naira, Dollar), multiply the amount parameter by 100 in your code, amount: document.getElementById("amount").value * 100, This will allow you enter the amount in Naira or Dollar as the case may be.


### Payment channels[​](https://docs.squadco.com/Payments/squad-payment-modal/#payment-channels "Direct link to Payment channels")
After initialization, there are a couple of payment channels available to the customer to complete the transaction.
#### USSD[​](https://docs.squadco.com/Payments/squad-payment-modal/#ussd "Direct link to USSD")
The USSD channel allows your Nigerian customers to pay you by dialing the USSD code on their mobile devices. Nigerian banks provide USSD services for customers to use for transactions, and we have integrated with some of these banks to allow your customers to complete payments.
  

![](https://res.cloudinary.com/delflsgq4/image/upload/v1/squad-docs/ussdModal?_a=DAJFJtWIZAA0)
  

After dialing the USSD code displayed, the system will prompt the user to input the USSD PIN to authenticate the transaction and then confirm it. All that is needed to initiate USSD payment is the customer's email and the amount to be charged. When the user makes a payment, the response will be sent to your webhook.
Therefore, to make it work as expected, webhooks must be configured on your [Squad dashboard](https://dashboard.squadco.com/login).
##### Banks Supported[​](https://docs.squadco.com/Payments/squad-payment-modal/#banks-supported "Direct link to Banks Supported")
Here is a list of all the Banks USSD _shortcodes_ we currently support:  
| Bank  | USSD Shortcode  |  
| --- | --- |  
| Access (Diamond) Bank  | 426  |  
| Access Bank  | 901  |  
| EcoBank  | 326  |  
| First City Monument Bank (FCMB)  | 329  |  
| Fidelity Bank  | 770  |  
| First Bank  | 894  |  
| Guaranty Trust  | 737  |  
| Heritage Bank  | 745  |  
| Keystone Bank  | 7111  |  
| Rubies (Highstreet) MFB  | 779  |  
| Stanbic IBTC Bank  | 909  |  
| Sterling Bank  | 822  |  
| United Bank for Africa (UBA)  | 919  |  
| Union Bank  | 826  |  
| Unity Bank  | 7799  |  
| VFD Bank  | 5037  |  
| Wema Bank  | 945  |  
| Zenith Bank  | 966  |  
#### Bank Transfer[​](https://docs.squadco.com/Payments/squad-payment-modal/#bank-transfer "Direct link to Bank Transfer")
Squad provides a payment method that makes it possible for customers to pay you through a direct bank account transfer. The customer provides their name, phone number, and email address. Then a preset account number is displayed along with the preregistered bank name.
  

![](https://res.cloudinary.com/delflsgq4/image/upload/v1/squad-docs/transferModal?_a=DAJFJtWIZAA0)
  

#### Card[​](https://docs.squadco.com/Payments/squad-payment-modal/#card "Direct link to Card")
With Squad, customers can pay with Card provided their card details are correct and updated. The customer provides their card number, card expiry date, and CVV.
### How To Test[​](https://docs.squadco.com/Payments/squad-payment-modal/#how-to-test "Direct link to How To Test")
  1. Create a free Squad [sandbox account](https://sandbox.squadco.com/login) and get your test keys from the dashboard.
  2. Copy the code sample from the **Code Glossary** of this documentation unto a text editor of your choice.
  3. Save the document as .html file. For example index.html
  4. With an internet-enabled device, view the .html file (index.html) using any web server of your choice either local (WAMP, XAMPP, etc) or online.


### Go live[​](https://docs.squadco.com/Payments/squad-payment-modal/#go-live "Direct link to Go live")
To go live with the payment modal, simply replace the test public key with the live public key found in your [Squad dashboard](https://dashboard.squadco.com/login). Your platform must be hosted online for the live environment to function correctly.
[](https://github.com/HabariPay/habaripay.github.io/tree/main/docs/Payments/squad-payment-modal.mdx)
[Previous Verify Transaction](https://docs.squadco.com/Payments/verify-transaction)[Next Test Cards](https://docs.squadco.com/Payments/test-cards)
  * [Payment Modal](https://docs.squadco.com/Payments/squad-payment-modal/#payment-modal)
  * [Parameters](https://docs.squadco.com/Payments/squad-payment-modal/#parameters)
  * [Code Glossary](https://docs.squadco.com/Payments/squad-payment-modal/#code-glossary)
  * [Initiate transaction](https://docs.squadco.com/Payments/squad-payment-modal/#initiate-transaction)
  * [Checkout Demo](https://docs.squadco.com/Payments/squad-payment-modal/#checkout-demo)
  * [Key Information](https://docs.squadco.com/Payments/squad-payment-modal/#key-information)
  * [Payment channels](https://docs.squadco.com/Payments/squad-payment-modal/#payment-channels)
  * [How To Test](https://docs.squadco.com/Payments/squad-payment-modal/#how-to-test)
  * [Go live](https://docs.squadco.com/Payments/squad-payment-modal/#go-live)


