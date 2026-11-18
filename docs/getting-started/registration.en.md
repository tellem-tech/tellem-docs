---
description: "Register, create a subscription, get CRM access, and complete your first store settings in Tellem."
---

<span id="_1"></span>

# Connection and first sign-in { #connection-and-first-sign-in }

Create a subscription and get access to the CRM, then set up your store.

<span id="_2"></span>

## Personal account { #personal-account }

1. Open [tellem.tech/lk](https://tellem.tech/lk). To register by email, click **Don't have an account? Sign up**. Enter your first name, last name, and email, select the checkbox to consent to the processing of your personal data, and click **Create account**. Enter the code from the email and click **Confirm**. You can also sign in with Yandex or VK ID.
2. Under **Subscriptions**, click **Add subscription** and choose a plan. In **Store address**, enter 1 to 63 lowercase Latin letters, digits, or hyphens. Start and end with a letter or digit. For example, to use `myshop.tellem.store`, enter `myshop`.
3. Click **Continue**, then click the payment button. Pay for the subscription in the new tab. Return to your personal account and click **Refresh status**.

If you close the tab before paying, return to the subscription card marked **Awaiting payment** and click the payment button. Store setup starts automatically after payment. Once the store is ready, **Open CRM** and **Open store** appear on the card.

!!! note "CRM access"
    The Tellem team will send your CRM sign-in details. Contact [Tellem support](https://t.me/tellem_tech_bot) to add employees as well.

<span id="crm"></span>

## Signing in to the CRM { #signing-in-to-the-crm }

Open `https://<subdomain>.tellem.store/crm` (or **Open CRM** in your personal account), enter your **Login** and **Password**, and click **Sign in**.

There is no password recovery button. Contact [Tellem support](https://t.me/tellem_tech_bot) if you lose your password.

To change your password, open **the user menu in the header → Profile → Password**, enter the new password and confirmation, then click **Save**.

To open your personal account in a new tab, choose **the user menu in the header → Personal account**.

If a lock appears in the header, click it to see why access is restricted. From this window, you can open your personal account or contact support.

<span id="_3"></span>

## Welcome configuration wizard { #welcome-configuration-wizard }

Complete the wizard on your first sign-in and click **Finish**. Until it is finished, the wizard opens on every CRM page load for every employee. Choose at least one option for each question.

???+ example "Example: welcome configuration wizard"

    Example with demo data. The recording shows the Russian interface.

    <figure markdown="span">
    [![The four steps of the welcome configuration wizard: the restaurant or café business type, features, number of seats and payment methods; after Finish the home page opens.](../media/crm/crm-welcome-wizard.en.gif){ width="960" height="540" loading=lazy }](../media/crm/crm-welcome-wizard.en.gif)
    </figure>

The business type affects the [Telegram bot's button label](bot-setup.md#2-write-a-welcome-message). **Online shop** also hides store addresses in the app. The other answers do not configure the store; follow the checklist below.

Before creating a store or order, check the [country in general settings](../modules/crm/general-settings.md). You cannot change it afterwards.

Next: [store launch checklist](../modules/crm/getting-started.md).
