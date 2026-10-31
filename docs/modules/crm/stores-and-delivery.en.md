---
description: "Set up Tellem stores and chains, addresses, fulfillment and payment methods, links, and QR codes."
---

<span id="_1"></span>

# Stores { #stores }

Create sales locations, enable fulfillment and payment methods, then share a store link or QR code.

Open **Catalog → Stores**.

<span id="_2"></span>

## Store or chain { #store-or-chain }

Click **Create**, or **Actions → Create** on a phone. Choose **Single store** for one location or **Store chain** for locations sharing fulfillment and payment methods.

- Enter the store's name, city, and street. Its warehouse and pickup point are created with it; add products through [Inventory](inventory.md).
- Add at least one store to a chain. **Add store** selects an existing one; **Create** in the selection window adds a new one. A store can belong to several chains; its name must be unique within a chain.
- **Temporarily closed** keeps the chain in the customer's list and blocks checkout. Fill in **Store chain closure message**: customers see it on the home screen, in the catalog and at checkout. Without a message, they see “Ordering is unavailable”. Change the status back to **Opened** to accept orders again. **Archived** hides the entire chain.

???+ example "Example: a single store"

    Example with demo data. The recording shows the Russian interface.

    <figure markdown="span">
    [![Creating a store: Create, then Create store, the name, city, street and house number, turning on pickup and saving; the store appears in the list.](../../media/crm/crm-store-create.en.gif){ width="960" height="540" loading=lazy }](../../media/crm/crm-store-create.en.gif)
    </figure>

??? example "Example: a store chain"

    Example with demo data. The recording shows the Russian interface.

    <figure markdown="span">
    [![Creating a chain: Create, then Create chain, the name, Add store with a store selected, turning on pickup and saving; the chain appears in the list.](../../media/crm/crm-chain-create.en.gif){ width="960" height="540" loading=lazy }](../../media/crm/crm-chain-create.en.gif)
    </figure>

<span id="_3"></span>

## Fulfillment methods { #fulfillment-methods }

Enable the required methods in **Manage fulfillment methods**. Create missing ones under [Settings → Delivery](delivery.md).

!!! warning "Method restrictions"
    Customers cannot check out without an enabled method. **Online** is incompatible with other methods: enabling one disables the other. A chain using **Online** can contain only one store.

??? example "Example: fulfillment and payment methods"

    Example with demo data. **Online** is available only to a chain with one store, so the recording takes the second store out of the window for a moment. The recording shows the Russian interface.

    <figure markdown="span">
    [![Setting a chain's methods: Edit, turning on Online switches off pickup and courier delivery, turning pickup back on switches Online off, cash on receipt stays on, then Save and the saved message.](../../media/crm/crm-store-methods.en.gif){ width="960" height="540" loading=lazy }](../../media/crm/crm-store-methods.en.gif)
    </figure>

<span id="_4"></span>

## Payment methods { #payment-methods }

Under **Manage payment methods**, enable services created in [Settings → Payments](payment-providers.md). New chains have **Cash on receipt** and **Card on receipt** enabled. Two methods of the same type, such as two YooKassa configurations, cannot be enabled together.

<span id="qr-code-and-link"></span>

<span id="qr-"></span>

## QR code and link { #qr-links }

Select a store or chain row and click **Print QR code**. Check **Point of sale** in the print window. Print the code or click **Copy link** to share it on your website or social media. The link opens the selected store in a browser; Telegram is not required.

??? example "Example: the QR code window"

    Example with demo data. The image shows the Russian interface.

    <figure markdown="span">
    [![The QR code print window: the demo store is selected as the point of sale and the preview shows the QR code; the Print QR code and Copy link buttons are highlighted.](../../media/crm/crm-store-qr.en.png){ width="1280" height="720" loading=lazy }](../../media/crm/crm-store-qr.en.png)
    </figure>

For an iiko store, you can [create a QR code for a specific table](iiko.md#qr-).

<span id="_5"></span>

## Deletion { #deletion }

Stores or chains with orders cannot be deleted. For an individual store, first set quantities to zero or remove the rows under [Catalog → Inventory](inventory.md). Deleting it also deletes its warehouse and pickup point.
