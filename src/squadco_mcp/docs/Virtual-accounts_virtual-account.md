# Source: https://docs.squadco.com/Virtual-accounts/virtual-account

[Skip to main content](https://docs.squadco.com/Virtual-accounts/virtual-account/#__docusaurus_skipToContent_fallback)
[![My Site Logo](https://docs.squadco.com/img/squad_logo.svg)](https://docs.squadco.com/)
Search`K`
[Support](https://squadco.com/support/)[Create Account](https://dashboard.squadco.com/sign-up)[Sign In](https://dashboard.squadco.com/login)
  * [Home](https://docs.squadco.com/)
  * [Payments](https://docs.squadco.com/Virtual-accounts/virtual-account/)
  * [Webhook & Redirect URL](https://docs.squadco.com/Virtual-accounts/virtual-account/)
  * [Virtual Accounts](https://docs.squadco.com/Virtual-accounts/virtual-account/)
    * [Virtual Accounts](https://docs.squadco.com/Virtual-accounts/virtual-account)
    * [API Specifications](https://docs.squadco.com/Virtual-accounts/api-specifications)
    * [Encryption & Decryption](https://docs.squadco.com/Virtual-accounts/encryption-decryption)
    * [Dynamic Virtual Account Overview](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2)
  * [Transfer API](https://docs.squadco.com/Virtual-accounts/virtual-account/)
  * [Others](https://docs.squadco.com/Virtual-accounts/virtual-account/)
  * [Value Added Services (VAS)](https://docs.squadco.com/Virtual-accounts/virtual-account/)


  * [](https://docs.squadco.com/)
  * Virtual Accounts
  * Virtual Accounts


On this page
# Virtual Accounts
##### The Squad Virtual Accounts API allows you to create customized fly-through accounts for receiving payments from your customers. The virtual accounts help businesses reserve their corporate bank account numbers.[​](https://docs.squadco.com/Virtual-accounts/virtual-account/#the-squad-virtual-accounts-api-allows-you-to-create-customized-fly-through-accounts-for-receiving-payments-from-your-customers-the-virtual-accounts-help-businesses-reserve-their-corporate-bank-account-numbers "Direct link to The Squad Virtual Accounts API allows you to create customized fly-through accounts for receiving payments from your customers. The virtual accounts help businesses reserve their corporate bank account numbers.")
You must create a Sandbox account to test all integrations before going live.
  1. Create an account on our [sandbox](https://sandbox.squadco.com/sign-up) environment
  2. Retrieve keys from the Merchant settings Page, under the API & Webhook tab.


**Authorization:** Any request made without the authorization key will fail with a 401 (Service Not Authorized) response code.
**Environment base URL:**
**Test:** <https://sandbox-api-d.squadco.com>
**Production:** <https://api-d.squadco.com>
**Authorization** keys are to be passed via Headers as a Bearer token.
**Example:** Authorization: Bearer sandbox_sk_94f2b798466408ef4d19e848ee1a4d1a3e93f104046f
### Explore[​](https://docs.squadco.com/Virtual-accounts/virtual-account/#explore "Direct link to Explore")
Virtual accounts serve as an additional payment channel for your business, allowing customers to pay directly to the account number assigned to them. Whenever money is sent to a dedicated virtual account, you will receive a notification through your webhook URL, and the amount will be instantly credited to your specified GTBank physical account.
These notifications will be sent to your webhook URL, enabling your servers to take the necessary actions related to the payment within your system.
To explore all the possibilities available with the Virtual Accounts API, please refer to our API documentation.
[](https://github.com/HabariPay/habaripay.github.io/tree/main/docs/Virtual-accounts/virtual-account.mdx)
[Previous Secure File Transfer Protocol (SFTP) Notification](https://docs.squadco.com/webhook-direct-url/sftp)[Next API Specifications](https://docs.squadco.com/Virtual-accounts/api-specifications)
  * [Explore](https://docs.squadco.com/Virtual-accounts/virtual-account/#explore)


