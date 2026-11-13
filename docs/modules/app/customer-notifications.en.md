---
description: "Connect Tellem notifications in Telegram, VK, email, and on your device, grant permissions, and manage mailings."
---

<span id="_1"></span>

# Customer notifications { #customer-notifications }

Connect order and bonus messages under **Profile → Notifications**. You can also check an order's status in [My orders](checkout.md).

## Where to send { #channels }

**Where to send** shows the Telegram, VK, and email channels offered by the store. Messages go to every enabled and available channel. A disabled channel is not replaced by another. [Enable device push notifications separately](#push).

A connected channel has a switch. If the store offers only one channel and it is already enabled, no switch appears. You cannot disable the last enabled channel: connect or enable another first. If none is enabled, follow **Connect a channel…**.

??? example "Example: the Notifications screen"

    Example with demo data. The image shows the Russian interface.

    <figure markdown="span">
    [![The notifications sheet: the where-to-send block with its only channel, email (anna@example.com), is highlighted; the mailings switch is above it.](../../media/app/app-notification-channels.en.png){ width="1280" height="720" loading=lazy }](../../media/app/app-notification-channels.en.png)
    </figure>

To connect a channel, select the action in its row:

- **Telegram:** **Connect**, or **Open bot** if it has not been started. [Start the store bot](#telegram).
- **VK:** **Connect** to link your account, or **Allow** to grant message permission. [Connect community messages](#vk).
- **Email:** **Add** if no address is set, or **Verify**. **Personal data** opens; the code goes to the address you entered. No switch appears until confirmation.

Signing in with an emailed code also confirms your address. For order emails, the store must configure email delivery and you must enable email under **Where to send**. This switch does not disable sign-in emails or emails sent manually by the store.

## VK { #vk }

<span id="vk_1"></span>

### Sign in or link VK { #sign-in-or-link-vk }

Choose **VK ID** on **Sign in or sign up**. If you already have a store account, sign in as usual first, then click **Link** next to VK in your profile or **Connect** under **Profile → Notifications**. This associates messages with your orders. If you connect from **Notifications**, you return to that screen afterwards.

Screenshots show the Russian interface.

![Sign in or sign up: the VK ID button above the email form.](../../media/vk-setup/customer-login.png){ width="440" }

<span id="_2"></span>

### Allow messages { #allow-messages }

1. After sign-in or linking, allow messages using the VK button in **VK notifications**. Use the same VK account linked to the store.
2. Wait for connection to finish. If permission is already granted, click **Connect notifications**.

![VK notifications: Connect notifications when message permission has already been granted.](../../media/vk-setup/customer-connect.png){ width="352" }

The permission covers private community messages about orders and bonus points, plus mailings if you enable them. It does not join the community or subscribe you to its posts.

**Later** closes the offer; sign-in and ordering remain available. Return using **Allow** in the VK row under **Notifications**, without signing in again.

<span id="_3"></span>

### If it does not work { #if-it-does-not-work }

| Message | What to do |
|---|---|
| **A different VK account is open in the widget** | Switch VK to the account linked to the store |
| **VK widget unavailable** | Click **Retry** or **Open VK**, allow messages in the community chat, then return to **Connect notifications** |
| **Could not connect notifications** | Try **Connect notifications** again; you do not need to grant permission again |

To stop messages, disable VK under **Where to send** or block messages in the community chat. VK ID sign-in and purchases remain available.

After you block messages in VK, the channel row updates on the next attempt to send a message and shows **Allow**. To resume delivery, click this button in the store app. Linking VK again or granting permission only in VK does not resume delivery.

## Telegram { #telegram }

In a browser, select **Connect** under **Profile → Notifications**. Select **Open bot**, then tap **Start** and **Confirm linking** in Telegram. If Telegram did not open, select **Open bot** again. After confirming, return to the app. If the storefront offers a merge, follow the [steps for merging accounts](account.md#linking-and-merging-accounts).

If the bot is stopped or blocked, select **Open bot** and start it again.

Inside Telegram, your account connects when you open the store. If the bot has not been started, follow **Tap Start in the bot chat**.

<span id="e-mail"></span>

## Email { #email }

Connect and confirm email under [Where to send](#channels). If you change your address in **Personal data**, confirm the new address using the emailed code.

<span id="push-notifications-on-your-device"></span>

## Push notifications on your device { #push }

After signing in, open **Profile → Notifications**, enable **Push notifications**, and allow them in the browser prompt. They report order status changes on this device; tapping one opens the order. Mailings and bonus messages do not arrive by push.

If you see **Blocked in browser settings**, allow notifications in the browser or system settings. On iPhone and iPad, first [add the app to your home screen](account.md); push is unavailable in a regular browser tab. If no push card appears, the browser or store does not support push.

Signing out disables push on this device; enable it again after your next sign-in. **Log out of other devices** stops push on the other devices until their next sign-in.

<span id="_4"></span>

<span id="order-notifications-and-mailings"></span>

## Order notifications and mailings { #mailings }

**Mailings** at the top of the screen controls informational store messages: news and useful information, rather than advertising. It does not control order or bonus messages, including bonus expiry reminders.

Mailings require **Mailings** to be enabled and at least one connected channel under **Where to send**. VK also requires permission for community messages. If several channels are enabled and available, mailings arrive in each.

!!! info "For store owners"
    Connect a [VK community](../crm/vk.md) or [Telegram bot](../../getting-started/bot-setup.md). Create informational messages under [Mailings](../crm/mass-mailings.md). [CRM notification settings](../crm/crm-notifications.md) are for employees; customers connect channels in their app.
