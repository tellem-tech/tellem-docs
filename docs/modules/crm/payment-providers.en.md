---
description: "Connect and test Tellem payments, order payment methods, and configure provider credentials and notifications."
---

<span id="_1"></span>

# Payment { #payment }

Connect online payments or let customers pay on receipt.

Open **Settings → Payments**.

<span id="_2"></span>

## Creating a method { #creating-a-method }

1. Click **New service**, choose a provider, and enter credentials from its account. The name is shown to customers and must be unique.
2. Set a commission and payment deadline if needed. Commission increases product prices, excluding delivery; Alfa-Bank has no commission field. After the deadline, an unpaid order enters **Payment error** with a delay.
3. Under **Order fields**, configure contact visibility and requirements. Email is required for T-Bank and SBP (T-Bank), and for Tochka Bank when fiscal receipts are enabled. SBP is Russia's Faster Payments System.
4. Click **OK**. For a new service, a dialog asks how to save it: **Save as active** enables it in all chains and disables other services of the same type. For testing, choose **Save as inactive**, then enable it in the [required chain](stores-and-delivery.md).

???+ example "Example: a new payment method"

    Example with demo data; the credentials in the recording are placeholders. The recording shows the Russian interface.

    <figure markdown="span">
    [![Creating a payment method: New service, then YooKassa; the name and credentials, the commission, the order fields; OK, then Save as inactive; turning the method on in the chain and seeing it under the payment method in the app.](../../media/crm/crm-payment-method.en.gif){ width="960" height="540" loading=lazy }](../../media/crm/crm-payment-method.en.gif)
    </figure>

!!! warning "Secret credentials"
    Enter passwords, tokens, and secret keys only in CRM and the provider's account. Do not include them in screenshots or support requests. Use notification addresses shown in CRM without changes.

You can edit **Card on receipt** and **Cash on receipt**, but cannot delete them. A method used in orders cannot be deleted either.

Online payments in Tellem are available for orders in rubles. For another currency, use payment on receipt.

!!! warning "Online transfer"
    The app does not show payment details for this previously available method. Disable it in chains under **Catalog → Stores → Manage payment methods**. For an existing **New** order, agree on payment with the customer and click [Accept order](orders.md).

## Method order { #method-order }

In **Settings → Payments**, select a row and click **Move up** or **Move down**. On a phone, find these commands under **Actions**. The order is saved immediately and applies to all store chains; customers see only methods enabled in their chain.

<span id="_3"></span>

## Testing { #testing }

**Generate a test payment link** checks whether the provider accepts the credentials. Open the resulting page. The test link is not associated with an order and does not change a CRM order status.

Check the return to the app and status changes using a real order for an agreed small amount. Do not enable the method in all chains before this check. If the test payment needs to be refunded, [refund it](orders.md#cancellation) separately.

<span id="provider-details"></span>

<span id="_4"></span>

## Provider requirements { #provider-requirements }

Copy the remaining credentials from the selected provider's account.

| Service | What to check |
|---|---|
| T-Bank, SBP (T-Bank); Alfa-Bank, SBP (Alfa-Bank) | Optional order number prefix: Latin letters |
| Robokassa | MD5 is the supported hash algorithm |
| SBP (ArcoPay) | Choose a single-use or reusable SBP link |
| Sberbank, SBP (Sberbank) | [Obtain internet terminal credentials and set up notifications](#sberbank) |
| Beta Transfer | Set **Minimum payment amount** according to the provider terms. It limits the positive balance after redeeming bonuses and cannot lower the service's minimum in CRM |
| Tochka Bank, Tochka Bank (SBP) | [Obtain a token and select account details](#tochka) |

<span id="_5"></span>

## Provider notifications { #provider-notifications }

Copy addresses from CRM to the provider's account:

- **YooKassa:** **Details for personal account → Notification URL**; select `payment.succeeded` and `payment.canceled` events.
- **Robokassa:** on the same tab, use POST for Result URL and GET for Success URL and Fail URL.
- **Beta Transfer:** Result, Success, and Fail URLs are under **Additional information**.
- **Sberbank:** Tellem support provides the address. Enter it in SberBusiness and set the verification parameters in CRM as described in [Payment notifications](#sberbank-notifications).

T-Bank and ArcoPay receive the address with the payment. Alfa-Bank checks statuses without notifications. YooKassa status checks continue regardless of **Update payment statuses using the scheduler**.

## Sberbank and SBP (Sberbank) { #sberbank }

Accepting card and SBP payments requires an internet acquiring contract with Sber.

### Contract with the bank { #sberbank-contract }

Prepare the following for the application:

- the name and taxpayer number (INN) of your sole proprietorship (IP) or limited liability company (OOO);
- the name, phone number, and work email of the employee who will contact the bank;
- the bank account details for receiving revenue;
- the store website address;
- details of your current online cash register, if you have one.

Apply on the [Sber website](https://www.sberbank.ru/ru/s_m_business/bankingservice/sberpay) or contact your bank manager. Say that you need internet acquiring for card payments on a Tellem store website. If you need SBP payments, ask to enable them as well.

Ask the bank how to send fiscal receipts to customers: Tellem's Sberbank settings have no receipt options. Before signing the contract, check the bank fee including taxes, the cost of sending receipts, and when revenue is credited to your account.

!!! note "If you already have a contract"
    Ask the bank whether the Tellem website can be added to your contract. If Sber payments already work on another website, change their settings only after agreeing with the person responsible for that website.

### Internet terminal credentials { #sberbank-terminal }

After approving the application, the bank connects an internet terminal for the website. The steps below use the Russian labels of SberBusiness, Sber's online bank for businesses.

In SberBusiness, open **Эквайринг → Оборудование** (Acquiring → Equipment) and select the internet terminal. If it is not listed, ask your manager for the connection status and terminal number.

The terminal's **Настройки** (Settings) tab contains the credentials for Tellem:

- **Логин шлюза** (gateway login) is the service login for connecting the website. It usually ends with `-api`.
- For **Пароль шлюза** (gateway password), click **Сгенерировать** (Generate), then **Скопировать пароль** (Copy password), and store the password securely. The password is shown once: after you click **Закрыть** (Close), you cannot view it again.

!!! warning "A new password replaces the old one"
    If the terminal already accepts payments on another website, agree on the password change first: that website will need the new password.

Tellem does not need your SberBusiness sign-in credentials or SMS codes.

Test credentials differ from live ones. If you want to test without real payments, ask your manager for them.

For details on terminal settings, see the [Sber help center](https://www.sberbank.ru/help/business/sbbol/acquiring/work/100667) (in Russian).

### Payment notifications { #sberbank-notifications }

The bank uses notifications to tell Tellem that an order has been paid. The checksum type and key let CRM verify that a notification came from the bank. Until they are set in Tellem, CRM rejects bank notifications, and the order status updates only on the next payment check.

1. Ask [Tellem support](https://t.me/tellem_tech_bot) for the notification URL.
2. Ask your bank manager for the notification checksum type and the key for verifying notifications.
3. In SberBusiness, open the internet terminal and go to **Настройки → Колбэк-уведомления → Подключить** (Settings → Callback notifications → Connect).
4. Paste the full URL into **Ссылка для уведомлений** (notification URL) and click **Подключить** (Connect). The status should change to **Подключены** (Connected).

!!! warning "The URL is shared by the merchant's terminals"
    The notification URL changes for all internet terminals of the same connection point (merchant). If another website accepts payments through this merchant, agree on the change with the person responsible for that website first.

For details on callback notifications, see the [Sber help center](https://www.sberbank.ru/help/business/sbbol/acquiring/work/100752) (in Russian).

### Setting up Tellem { #sberbank-setup }

1. Under **New service**, choose **Sberbank** for card payments. For SBP payments, create a separate **SBP (Sberbank)** service after the bank confirms that SBP is enabled.
2. Fill in the fields:

    | Field | What to enter |
    |---|---|
    | **Login**, **Password** | The gateway login and password from the [internet terminal settings](#sberbank-terminal) |
    | **Test mode** | Turn on for test credentials, turn off for live ones |
    | **Callback checksum type** | The type specified by the bank: **Symmetric (HMAC-SHA256)** or **Asymmetric (SHA512withRSA)** |
    | **Callback verification key** | The key from the bank: a secret key for the symmetric type or a public key (certificate) for the asymmetric type |

3. **Generate a test payment link** opens the Sber payment page for **Sberbank** and an SBP payment page for **SBP (Sberbank)**. If an error appears instead of a link, check the login, password, and **Test mode**: test credentials work only with the mode on, and live credentials only with it off.
4. Before the [real-order check](#testing), enter the live login and password and turn off **Test mode**. After payment, the order should get the [“Paid” status](orders.md#online-payment), the payment for the same amount should appear in SberBusiness, and the customer should receive a receipt if receipt sending is set up.

If the order does not get the “Paid” status, disable the method in the store and contact [Tellem support](https://t.me/tellem_tech_bot). Ask your bank manager about the contract, terminal, and notifications, or see the [SberBusiness help center](https://www.sberbank.ru/help/business/sbbol) (in Russian).

## Tochka Bank and Tochka Bank (SBP) { #tochka }

1. In Tochka's account, open **Services → All services → Integrations and API → JWT keys**. Create an access token with permissions for the required product:

    | Product | Permissions |
    |---|---|
    | Card | `ReadCustomerData`, `MakeAcquiringOperation`, `ReadAcquiringData`, `ManageWebhookData` |
    | SBP | `ReadCustomerData`, `ReadSBPData`, `EditSBPData`, `ManageWebhookData` |

2. Paste the token into **Access token** without `Bearer`. A `client_id` or website builder login will not work.
3. Select the loaded account details: company and merchant for cards, or merchant and account for SBP. If lists are empty, check token expiry and permissions, test mode, and whether the bank enabled the product.
4. Click **Get** for **Public JWK for webhook**. This is the bank's public key for checking notifications. Copy **Webhook notification URL** into Tochka's integration settings and select `acquiringInternetPayment` for cards or `incomingSbpPayment` for SBP.

Before enabling **With fiscal receipts**, activate the service with the bank. The setting applies to new links and makes customer email mandatory. The receipt includes products with commission and delivery; redeemed bonuses reduce the amount.

Use Tochka's test credentials in **Test mode**. Before live payments, disable the mode, replace the token with a live one, and select the account details again. Then [test payment](#testing).
