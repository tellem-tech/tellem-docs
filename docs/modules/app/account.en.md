---
description: "Sign in to the Tellem app, manage personal details and bonus points, merge accounts, review sessions, and install the app."
---

<span id="_1"></span>

# Account, installation, and notifications { #account-installation-and-notifications }

Sign in to place orders, save addresses, and connect bonus points. Without signing in, you can [browse the catalog and search for products](ui-and-pages.md).

<span id="_2"></span>

## Profile { #profile }

Open your profile using the button in the home screen header. The card with your name opens **Personal data**; **My orders**, **Delivery addresses**, and bonus points, if enabled by the store, are nearby. Find store contacts under **Support**; this item appears if the owner added contact details.

??? example "Example: the top of the profile"

    Example with demo data. The image shows the Russian interface.

    <figure markdown="span">
    [![The profile sheet: the name card and the 100 bonus points, My orders and Delivery addresses tiles are highlighted; the store card is below.](../../media/app/app-profile-overview.en.png){ width="1280" height="720" loading=lazy }](../../media/app/app-profile-overview.en.png)
    </figure>

Choose your sales area, interface language, and theme in the profile. The language on first opening depends on Telegram or your browser; after sign-in, your choice is saved to your account. **System** theme follows your device; **Light** and **Dark** are manual choices. The app does not inherit Telegram's theme.

<span id="_3"></span>

## Sign-in and registration { #sign-in-and-registration }

In **Sign in or sign up**, enter your email, click **Get code**, enter the six-digit code from the email, and click **Sign in**. A new account is created after code confirmation. If the code expires or stops working after incorrect attempts, request a new one; the screen shows the wait before another request. On your first code sign-in, you receive an email with an automatically generated password.

**Receive informational store mailings** is selected by default and applies only when creating an account. Later, change your subscription in [notification settings](customer-notifications.md#mailings).

???+ example "Example: signing in with an email code"

    Example with demo products. The recording shows the Russian interface.

    <figure markdown="span">
    [![Signing in as a guest: Add to cart on the latte card opens the sign-in form; the guest enters an email, requests a code, enters it and signs in; the latte is already in the cart.](../../media/app/app-sign-in-email.en.gif){ width="960" height="540" loading=lazy }](../../media/app/app-sign-in-email.en.gif)
    </figure>

Other sign-in methods:

- **Sign in with password** uses your email and password. **Forgot password?** sends a reset code; requesting a new code invalidates the previous one. A new password must contain at least 8 characters.
- **Telegram, VK ID, and Yandex**: select an available button above the form. For Telegram, start the store bot and return to the app. If Telegram does not open, click **Telegram didn't open? Open the link**. If confirmation expires, start sign-in again.

After signing in from a product card, you return to the same product. If sign-in started from **Add to cart**, the product is added to the cart and the card closes; after **Buy**, the cart opens. The sales area selected before sign-in replaces the one saved in your profile, including when signing in through VK ID or Yandex. Closing the sign-in form returns you to the product.

In the Telegram Mini App, the app running inside Telegram, sign-in uses your Telegram account. Passwords, **Active sessions**, **Sign out**, Telegram linking, and push notifications are unavailable there. To manage them, open the store link in a browser and sign in using the Telegram button.

<span id="_4"></span>

## Personal details and sign-in methods { #personal-details-and-sign-in-methods }

Open **Profile → your name card → Personal data** to change your first name, last name, phone, or email. Confirm a new email address with the code sent to it.

**Change password** requires the current password and ends sessions on other devices. If you have no password of your own, for example after using only an external sign-in service, use **Set password**.

When you sign in or link a service, the app fills in empty first name, last name, and phone fields if the service supplies them. Values you edited or cleared manually are preserved. Profile details are filled in at [checkout](checkout.md) until you edit the recipient's details in the order itself.

### Birthday discount example { #birthday }

In **Personal data**, choose the day and month of your birthday, without the year, and click **Save**. **Remove date** clears both fields; save that change too. You can enter your birthday even if the store offers no gift.

If the store offers a birthday gift and you have not saved a date yet, the profile shows a **Birthday not set** card with the gift amount. Click it to open **Personal data**. Once you save the date, the card disappears, and the gift amount and validity period appear under the date.

??? example "Example: birthday discount in the profile"

    Example with demo data: a **10%** discount applies for **3 days before, on the birthday, and 3 days after**, or 7 days in total. For a birthday on October 31, that is October 28 through November 3. Your store's terms may differ. The images show the Russian interface.

    <figure markdown="span">
    [![Profile: the Birthday not set card is highlighted; its text offers a 10% discount on products if you enter your birthday in advance. The Anna Petrova card is above it.](../../media/app/app-birthday-card.en.png){ width="1280" height="720" loading=lazy }](../../media/app/app-birthday-card.en.png)
    </figure>

    <figure markdown="span">
    [![Personal data: the Birthday card is highlighted, with day 31, month 10, a line saying the 10% discount on products applies from 28.10 through 03.11 inclusive, and the Remove date link.](../../media/app/app-birthday.en.png){ width="1280" height="720" loading=lazy }](../../media/app/app-birthday.en.png)
    </figure>

For a discount, save the date before the promotion period begins; for gift points, before the birthday starts. Saving it later does not unlock a gift whose period has begun. Bonus points require a connected bonus account; you can connect it on the birthday itself if you saved the date in advance.

### Linking and merging accounts { #linking-and-merging-accounts }

Sign-in methods are at the bottom of the profile. **Unlink** is available only if another sign-in method remains: your own password, a verified email address, or a linked service. Before unlinking your last contact channel, connect another notification channel under [Where to send](customer-notifications.md#channels). A password or another sign-in method alone does not meet this requirement.

!!! warning "Merging cannot be undone"
    If the service is linked to another Tellem account, the app offers **Merge accounts**. Orders, addresses, the cart, and favorites move to the selected account.

If both accounts have bonus accounts, the selected account's balance remains: the balances are not added together. If only the other account has a bonus account, it moves with its balance. The bonus transaction history is preserved.

An opt-out from marketing messages on either account remains in effect after merging.

A notification channel disabled in either account stays disabled if at least one enabled channel remains after merging. Otherwise, the selected account's channels are kept. Check [notification settings](customer-notifications.md#channels) after merging.

<span id="_5"></span>

## Addresses and bonus points { #addresses-and-bonus-points }

Open **Profile → Delivery addresses → Add address**. Enter a name, fill in the address, and tap **Save**. You can select the saved address at [checkout](checkout.md).

??? example "Example: saving a delivery address"

    Example with demo data. The recording shows the Russian interface.

    <figure markdown="span">
    [![Adding a demo address: entering the country, region, city, street, and house number, saving, and checking the new card in the address list.](../../media/app/app-delivery-address.en.gif){ width="960" height="540" loading=lazy }](../../media/app/app-delivery-address.en.gif)
    </figure>

If the store has enabled its bonus program and you do not have a bonus account yet, **Join the bonus program** opens after sign-in. Check or enter your phone number in +7 format and tap **Register**. The number is saved to your profile; you cannot use another customer's number. You can close the window with the close icon and return to registration through **Connect bonus system** in your profile.

Points start accumulating after you connect the account; welcome points, if offered by the store, are awarded when you connect. Their amount appears in the invitation and registration card. After registration, the card shows your balance and nearest expiry date. Open **Bonus points** to check the rules, validity, and history.

<span id="_6"></span>

## Active sessions { #active-sessions }

Open **Active sessions** to check which devices are signed in. After confirmation, **Log out of other devices** ends sessions on the other devices; the current device stays signed in.

<span id="_7"></span>

## Installation { #installation }

The installed app appears on your home screen and opens in a separate window. Select **Install app** in your profile; sign-in is not required.

??? example "Example: “Install app” in the profile"

    Example with demo data. The image shows the Russian interface.

    <figure markdown="span">
    [![The lower part of the profile without signing in: the Install app row below the interface language block is highlighted, with legal document links under it.](../../media/app/app-install.en.png){ width="1280" height="720" loading=lazy }](../../media/app/app-install.en.png)
    </figure>

=== "Android and computer"

    In a browser that supports installation, select **Install app** in your profile. This item appears when the browser is ready to offer installation and opens the system dialog. If it is absent after you close the dialog, reload the page.

=== "iPhone and iPad"

    Open the store in Safari: **Share → Add to Home Screen**. **Install app** in the profile shows these instructions.

=== "Telegram"

    The installation option is absent inside Telegram. Open the store link in an external browser and follow the instructions for your device.

The installation option is absent in an already installed app and in browsers without installation support.

## Where to send { #channels }

Connect Telegram, VK, and email under **Profile → Notifications → Where to send**. See [connecting channels, disabling messages, and managing mailings](customer-notifications.md#channels).

## Push notifications { #push }

Push notifications report order statuses on your device. See [enabling push and the restrictions on iPhone and iPad](customer-notifications.md#push).

!!! info "For store owners"
    App name and icon, support contacts, and profile information sections: [store settings](../crm/general-settings.md). Birthday gifts: [promotions](../crm/promo-codes.md#birthday) and [bonus rules](../crm/bonus-system.md). For Telegram sign-in, [connect a bot](../../getting-started/bot-setup.md).
