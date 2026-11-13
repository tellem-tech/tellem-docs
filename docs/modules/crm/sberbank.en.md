---
description: "Connect Sberbank payments to Tellem: internet acquiring contract, internet terminal credentials in SberBusiness, payment notifications, and a test order."
---

# Sberbank { #sberbank }

Connect Sberbank internet acquiring so customers can pay for orders on the website by card or through SBP, Russia's Faster Payments System.

## Contract with the bank { #contract }

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

## Internet terminal credentials { #terminal }

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

## Payment notifications { #notifications }

The bank uses notifications to tell Tellem that an order has been paid. The checksum type and key let CRM verify that a notification came from the bank. Until they are set in Tellem, CRM rejects bank notifications, and the order status updates only on the next payment check.

1. Ask [Tellem support](https://t.me/tellem_tech_bot) for the notification URL.
2. Ask your bank manager for the notification checksum type and the key for verifying notifications.
3. In SberBusiness, open the internet terminal and go to **Настройки → Колбэк-уведомления → Подключить** (Settings → Callback notifications → Connect).
4. Paste the full URL into **Ссылка для уведомлений** (notification URL) and click **Подключить** (Connect). The status should change to **Подключены** (Connected).

!!! warning "The URL is shared by the merchant's terminals"
    The notification URL changes for all internet terminals of the same connection point (merchant). If another website accepts payments through this merchant, agree on the change with the person responsible for that website first.

For details on callback notifications, see the [Sber help center](https://www.sberbank.ru/help/business/sbbol/acquiring/work/100752) (in Russian).

## Setting up Tellem { #setup }

1. Open **Settings → Payments**, click **New service**, and choose **Sberbank** for card payments. For SBP payments, create a separate **SBP (Sberbank)** service after the bank confirms that SBP is enabled.
2. Fill in the fields:

    | Field | What to enter |
    |---|---|
    | **Name** | The method name shown to customers, such as “Online by card” |
    | **Login**, **Password** | The gateway login and password from the [internet terminal settings](#terminal) |
    | **Test mode** | Turn on for test credentials, turn off for live ones |
    | **Callback checksum type** | The type specified by the bank: **Symmetric (HMAC-SHA256)** or **Asymmetric (SHA512withRSA)** |
    | **Callback verification key** | The key from the bank: a secret key for the symmetric type or a public key (certificate) for the asymmetric type |

    Set the commission, payment waiting time, and order fields as for [any payment method](payment-providers.md#creating-a-method).

3. Click **Generate a test payment link** and open the link. For **Sberbank**, the Sber payment page should open; for **SBP (Sberbank)**, an SBP payment page. If an error appears instead of a link, check the login, password, and **Test mode**: test credentials work only with the mode on, and live credentials only with it off.
4. Click **OK** and choose **Save as inactive**.

## Testing and launch { #launch }

The test link checks only the login and password and does not create a CRM order. Check notifications and status changes with a real order.

1. If you tested with test credentials, enter the live login and password, turn off **Test mode**, and check the test link again.
2. Enable the method only in the required store or chain: **Catalog → Stores** → store → **Edit** → **Manage payment methods** → **Save**. For details, see [Payment methods](stores-and-delivery.md#payment-methods).
3. Place a small order on the website with this method and pay for it.
4. Check that the order has the [“Paid” status](orders.md#online-payment) in CRM, the payment for the same amount appears in SberBusiness, and the customer received a receipt if receipt sending is set up.
5. If the test payment needs to be refunded, [refund it](orders.md#cancellation) separately.

If the payment link does not open or the order does not get the “Paid” status, disable the method in the store and contact [Tellem support](https://t.me/tellem_tech_bot). Ask your bank manager about the contract, terminal, and notifications, or see the [SberBusiness help center](https://www.sberbank.ru/help/business/sbbol) (in Russian).
