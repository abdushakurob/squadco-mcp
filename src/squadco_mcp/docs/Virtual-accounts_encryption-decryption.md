# Source: https://docs.squadco.com/Virtual-accounts/encryption-decryption

[Skip to main content](https://docs.squadco.com/Virtual-accounts/encryption-decryption/#__docusaurus_skipToContent_fallback)
[![My Site Logo](https://docs.squadco.com/img/squad_logo.svg)](https://docs.squadco.com/)
Search`K`
[Support](https://squadco.com/support/)[Create Account](https://dashboard.squadco.com/sign-up)[Sign In](https://dashboard.squadco.com/login)
  * [Home](https://docs.squadco.com/)
  * [Payments](https://docs.squadco.com/Virtual-accounts/encryption-decryption/)
  * [Webhook & Redirect URL](https://docs.squadco.com/Virtual-accounts/encryption-decryption/)
  * [Virtual Accounts](https://docs.squadco.com/Virtual-accounts/encryption-decryption/)
    * [Virtual Accounts](https://docs.squadco.com/Virtual-accounts/virtual-account)
    * [API Specifications](https://docs.squadco.com/Virtual-accounts/api-specifications)
    * [Encryption & Decryption](https://docs.squadco.com/Virtual-accounts/encryption-decryption)
    * [Dynamic Virtual Account Overview](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2)
  * [Transfer API](https://docs.squadco.com/Virtual-accounts/encryption-decryption/)
  * [Others](https://docs.squadco.com/Virtual-accounts/encryption-decryption/)
  * [Value Added Services (VAS)](https://docs.squadco.com/Virtual-accounts/encryption-decryption/)


  * [](https://docs.squadco.com/)
  * Virtual Accounts
  * Encryption & Decryption


# Encryption & Decryption
Encryption and Decryption function for decrypting merchant transaction
Javascript
#### Encryption

```
 let key = crypto.createHash('sha256').update(String(merchant_secret_key)).digest('base64').substr(0, 32);  
                  let IV = crypto.createHash('sha256').update(String(merchant_public_key)).digest('base64').substr(0, 16);  
                  const cipher = crypto.createCipheriv('aes256', key, IV);  
                  let encrypted = cipher.update(JSON.stringify(body), 'utf8', 'base64');  
                  return encrypted += cipher.final('base64');  
                    

```

#### Decryption

```
 let key = crypto.createHash('sha256').update(String(merchant_secret_key)).digest('base64').substr(0, 32);  
                  let IV = crypto.createHash('sha256').update(String(merchant_public_key)).digest('base64').substr(0, 16);  
                  const decipher = crypto.createDecipheriv('aes256', key, IV);  
                  let decrypted = decipher.update(body, 'base64', 'utf8');  
                  decrypted += decipher.final('utf8');  
                  return JSON.parse(decrypted);  

```

Python

```
from Crypto.Cipher import AES  
                  import base64  
                  import hashlib  
    
    
                  def _pad(s): return s + (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)   
                  def _cipher():  
                      key = hashlib.md5(merchant_secret_key).hexdigest() # 32 character hexadecimal  
                      iv = hashlib.md5(merchant_public_key).digest() # 16 byte binary  
                      return AES.new(key=key, mode=AES.MODE_CBC, IV=iv)  
    
                  def encrypt_token(data):  
                      return _cipher().encrypt(_pad(data))  
                        
                  def decrypt_token(data):  
                      return _cipher().decrypt(data)  
    
                  if __name__ == '__main__':  
                      print('Python encrypt: ' + base64.b64encode(encrypt_token('dmyz.org')))  
                      print('Python decrypt: ' + decrypt_token(base64.b64decode('FSfhJ/gk3iEJOPVLyFVc2Q==')))  

```


```

```

PHP

```
 <?php  
    
              class AES  
              {  
                    
                  function encryptToken($data, $merchant_secret_key, $merchant_public_key)  
                  {  
                      $key = substr(hash('sha256', $merchant_secret_key, true), 0, 32);  
                      $iv = substr(hash('sha256', $merchant_public_key, true), 0, 16);  
                      // use openssl:  
                      return openssl_encrypt($data, 'aes256', $key, OPENSSL_RAW_DATA, $iv);  
                  }  
    
                  function decryptToken($data, $merchant_secret_key, $merchant_public_key)  
                  {  
                      $key = substr(hash('sha256', $merchant_secret_key, true), 0, 32);  
                  $iv = substr(hash('sha256', $merchant_public_key, true), 0, 16);  
                      // use openssl:  
                      return openssl_decrypt(base64_decode($data), 'aes256', $key, OPENSSL_RAW_DATA, $iv);  
                    
                  }  
              }  
    
              $aes = new AES();  
              $arr = array(  
              'transaction_reference'=>'49test_1',  
              'virtual_account_number'=>'4899284992',  
              'principal_amount'=> '2350.00',  
              'settled_amount'=> '2338.25',  
              'fee_charged'=> '11.75',  
              'transaction_date'=> '2022-02-19T00:00:00.000Z',  
              'customer_identifier'=> '10A2',  
              'transaction_indicator'=> 'C',  
              'remarks'=> 'Payment from 10A2 to 4899284992',  
              'currency'=> 'NGN',  
              'channel'=> 'virtual-account'  
              );  
    
              echo ('PHP encrypt: '.base64_encode($aes->encryptToken(json_encode($arr), 'staging_sk_sample-secret-key-1', 'staging_pk_sample-public-key-1')))."  
";  
              echo ('PHP decrypt: '.$aes->decryptToken('Ajc/9TOSwbz1lTReb7BTo4XjL7bzJ0GWIxuncvSXfK83ZsYFt4bOt5+QQRz0jFFNSf6+7Axuqp91rR7aD/YwYczQQgUM+7QrK7nTw1KJbwTvPSSk3/IEektOlUx7DK7uXHlBBN9eVmn8tfDLKrsgj7zhymQhCfCoUTcDou3UyYWbKitwGH0o2X3hZo7cVqqq6Khnb12EwlK2kVhZvAjnu5g+T7erI1+RSb3jjab0MguWO6I3oXs9OGsiQKmCqZn564/q3ojArjk5OR8r3jBFgH4d96FoXS536rS8Toh5KPIVSGUjXLthcsWdgQ2VNzqBJ2iktzftFNgQRMdxQFCpaE0JwTKVkAyX0n3JDXt7DC+cTY+cHvAHRtl0zYhhrqT0WX4x95h+/WCdT27FEIJJJqJPBPHS1VAXwPS/v5sPGqdkqgFngTrYPaExk3YWoTxhonzT2tkagsGCaDuk8eptSA==', 'staging_sk_sample-secret-key-1', 'staging_pk_sample-public-key-1'))."  
";  
    
              ?>  
                    

```


```

```

C#

```
using System;    
                  using System.IO;    
                  using System.Security.Cryptography;    
                  class ManagedAesSample {    
                      public static void Main() {    
                          Console.WriteLine("Enter text that needs to be encrypted..");    
                          string data = Console.ReadLine();    
                          EncryptAesManaged(data);    
                          Console.ReadLine();    
                      }    
                      static void EncryptAesManaged(string raw) {    
                          try {    
                              // Create Aes that generates a new key and initialization vector (IV).      
                              // Same key must be used in encryption and decryption      
                              using(AesManaged aes = new AesManaged()) {    
                                  // Encrypt string      
                                  byte[] encrypted = Encrypt(raw, aes.Key, aes.IV);    
                                  // Print encrypted string      
                                  Console.WriteLine($ "Encrypted data: {System.Text.Encoding.UTF8.GetString(encrypted)}");    
                                  // Decrypt the bytes to a string.      
                                  string decrypted = Decrypt(encrypted, aes.Key, aes.IV);    
                                  // Print decrypted string. It should be same as raw data      
                                  Console.WriteLine($ "Decrypted data: {decrypted}");    
                              }    
                          } catch (Exception exp) {    
                              Console.WriteLine(exp.Message);    
                          }    
                          Console.ReadKey();    
                      }    
                      static byte[] Encrypt(string plainText, byte[] Key, byte[] IV) {    
                          byte[] encrypted;    
                          // Create a new AesManaged.      
                          using(AesManaged aes = new AesManaged()) {    
                              // Create encryptor      
                              ICryptoTransform encryptor = aes.CreateEncryptor(Key, IV);    
                              // Create MemoryStream      
                              using(MemoryStream ms = new MemoryStream()) {    
                                  // Create crypto stream using the CryptoStream class. This class is the key to encryption      
                                  // and encrypts and decrypts data from any given stream. In this case, we will pass a memory stream      
                                  // to encrypt      
                                  using(CryptoStream cs = new CryptoStream(ms, encryptor, CryptoStreamMode.Write)) {    
                                      // Create StreamWriter and write data to a stream      
                                      using(StreamWriter sw = new StreamWriter(cs))    
                                      sw.Write(plainText);    
                                      encrypted = ms.ToArray();    
                                  }    
                              }    
                          }    
                          // Return encrypted data      
                          return encrypted;    
                      }    
                      static string Decrypt(byte[] cipherText, byte[] Key, byte[] IV) {    
                          string plaintext = null;    
                          // Create AesManaged      
                          using(AesManaged aes = new AesManaged()) {    
                              // Create a decryptor      
                              ICryptoTransform decryptor = aes.CreateDecryptor(Key, IV);    
                              // Create the streams used for decryption.      
                              using(MemoryStream ms = new MemoryStream(cipherText)) {    
                                  // Create crypto stream      
                                  using(CryptoStream cs = new CryptoStream(ms, decryptor, CryptoStreamMode.Read)) {    
                                      // Read crypto stream      
                                      using(StreamReader reader = new StreamReader(cs))    
                                      plaintext = reader.ReadToEnd();    
                                  }    
                              }    
                          }    
                          return plaintext;    
                      }    
  }    

```


```

```

[](https://github.com/HabariPay/habaripay.github.io/tree/main/docs/Virtual-accounts/encryption-decryption.mdx)
[Previous API Specifications](https://docs.squadco.com/Virtual-accounts/api-specifications)[Next Dynamic Virtual Account Overview](https://docs.squadco.com/Virtual-accounts/dynamic-virtual-account-v2)
