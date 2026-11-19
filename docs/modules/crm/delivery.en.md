---
description: "Configure Tellem fulfillment and free delivery, connect carriers, and manage shipments."
---

<span id="_1"></span>

# Delivery { #delivery }

Order fulfillment methods include your own courier delivery and pickup, as well as CDEK, Yandex, Ozon, and Russian Post. CRM creates shipments and updates order statuses for CDEK and Yandex Delivery.

Open **Settings → Delivery** to configure a method. Check shipments created in CRM under **Delivery information** in the order.

<span id="_2"></span>

## Fulfillment methods { #fulfillment-methods }

Select **New method → Custom fulfillment method**, **CDEK**, **Ozon**, **Yandex**, or **Russian Post**. A new method is disabled in every store chain: enable it in the store chain's settings ([Stores](stores-and-delivery.md)). Built-in methods and methods used in orders cannot be deleted.

To change the order at checkout, select a method under **Settings → Delivery** and click **Move up** or **Move down**. On a phone, use the **Actions** menu. The order is saved immediately and applies to all store chains; customers see the methods enabled for their chain. The app selects the first suitable method, including pickup point delivery that still requires a city or point selection.

For a **Custom fulfillment method**:

1. Under **General**, set a name, type, conditions, and base price. The type determines [which details the customer enters](../app/checkout.md).
2. Under **Price**, add **Order amount from → Delivery price** thresholds if needed. The highest reached threshold applies; below all thresholds, the base price applies. Example: courier delivery costs ₽300 and is free from ₽2,000.
3. Under **Geography**, limit regions and cities. An empty list allows the method everywhere; an empty field in a row means any value.

???+ example "Example: a custom fulfillment method"

    Example with demo data. The recording shows the Russian interface.

    <figure markdown="span">
    [![Creating a fulfillment method: New method, then Custom fulfillment method, the name, the Delivery type, time and base price, a price threshold on the Price tab; the method is turned on in the chain, and the app shows its price and time among the fulfillment methods.](../../media/crm/crm-delivery-method.en.gif){ width="960" height="540" loading=lazy }](../../media/crm/crm-delivery-method.en.gif)
    </figure>

**Carriers**:

| Carrier | What the customer gets | Type | Shipments in CRM |
|---|---|---|---|
| CDEK | A rate for delivery to the door or a pickup point | Delivery or Pickup, depending on the rate | Yes |
| Yandex (Across Russia) | A pickup point | Pickup | Yes |
| Ozon | A pickup point | Pickup | No |
| Russian Post | Delivery to an address, calculated by postal code | Delivery | No |

For CDEK and Yandex pickup points, the customer selects a city from suggestions, then finds a point by street, name, or code. A home address is not required ([Checkout](../app/checkout.md)). **Geography** restrictions use the location of the selected pickup point.

The carrier calculates price and delivery time; **Geography** restrictions still apply. Under **Integration**:

- Disable **Test mode** for live CDEK and Yandex credentials. Ozon has no test mode; for Russian Post, it does not affect the calculation.
- Set a default product weight and box dimensions. The order is calculated as one package: CRM sums product weights including quantities, using the default for missing weights. One set of dimensions applies to the order.

Keep carrier passwords and keys secret; do not include them in screenshots.

**Check connection** calculates a sample delivery and shows its price and delivery time. This check never creates a shipment.

Changing the CDEK account, Yandex token, or **Test mode** stops tracking existing shipments: their status becomes **Needs attention**. Complete active deliveries first or arrange the change with the Tellem team.

## Free delivery for the customer { #free-delivery }

Every fulfillment method has a **Free delivery from** field on the **General** tab.
Enter an amount in the store's currency; leave the field empty or enter 0 to disable the condition.
When the product total reaches the threshold, delivery costs the customer 0. The total includes discounts and payment fees,
but excludes delivery and redeemed bonuses. This condition takes priority over the **Price** tab rules.
The store pays the carrier's charge; an unavailable delivery method remains unavailable.

At checkout, customers see how much more to add for free delivery. Each method has its own threshold; changing the setting does not recalculate existing orders.

For [CDEK pickup points](#cdek), the threshold and tip apply only to the default country. In other countries, the customer sees the rate calculated by CDEK.

[Example: use free delivery to increase order value](free-delivery.md).

## Connect a carrier { #carrier-setup }

=== "CDEK"

    <span id="_3"></span>

    ### CDEK { #cdek }

    On the **Integration** tab, enter the **Account** and **Secret password** from your CDEK account and select a **CDEK rate**, such as **Parcel — warehouse to warehouse (136)**. **Refresh rates** reloads the list. Warehouse means a CDEK point; door means an address. The rate determines the method's type: door delivery is **Delivery**, and delivery to a pickup point is **Pickup**. Parcel locker rates are not supported. Automatic registration works only for rates from a door or warehouse to a door or pickup point.

    For a pickup point rate, open the **General** tab. First check in your CDEK account that your contracted rate covers the countries you want to add. Add them under **Additional delivery countries**. Customers see the country list at [checkout](../app/checkout.md#delivery-method).

    **Default delivery country** starts as Russia. If you select another country, the previous one moves to **Additional delivery countries**. To stop shipping to the previous country, remove it from that list.

    **Sender postal code** is required. For automatic shipments, also complete:

    - **Origin city**: the full city name.
    - **Sender name** and **Sender phone**.
    - For warehouse-origin rates, **CDEK origin point**, where you hand over the parcel. This is not the customer's pickup point.
    - For door-origin rates, **Full sender address**.

    If registration fails after payment because these details are missing, see **Diagnostic message** under [Delivery information](#delivery-information). Rate calculation can proceed without these details.

=== "Yandex"

    <span id="_4"></span>

    ### Yandex { #yandex }

    Connect your company and accept the offer in your Yandex Delivery account ([Yandex guide](https://yandex.ru/support/delivery-profile/ru/other-day/how-to-join)). A successful rate check in CRM does not mean shipment creation is available.

    Enter the **API token** for **Across Russia**, using the selected environment, then select an **Origin station**: a warehouse or acceptance point. After entering the token, use **Refresh stations**. **Packaging weight, g** is added to the product weight.

    A Yandex shipment does not call a courier. If you use your own warehouse, configure dispatches in your Yandex account.

=== "Ozon"

    ### Ozon { #ozon }

    1. In Ozon Delivery for Business, create a delivery method and note its identifier.
    2. In the Ozon private applications section, create an application with `delivery-api.delivery`, `delivery-api.delivery-point`, and `delivery-api.order` access. Copy its Client ID and Client Secret.
    3. Select **New method → Ozon** and complete **Client ID**, **Client secret**, and **Shipping method ID**. When saving, CRM requests a token from Ozon; invalid credentials cannot be saved. Each dispatch point needs its own configuration.
    4. For **Check connection**, complete **Test recipient phone** with a number registered with Ozon, and **Test pickup point ID**. The sample calculation uses the default box; it does not confirm the final price for a real order.

    The customer needs a Russian phone number registered with Ozon. Frequent checks of different numbers temporarily make the method unavailable. An order cannot be placed with Ozon until the calculation succeeds. Pickup points take time to load after connection: customers may see **The Ozon pickup point list is loading. Try again in a minute.** Only pickup points are available; couriers and parcel lockers are not supported. The price includes delivery and insurance based on the product total. Ozon's final rate at acceptance may differ from the estimate.

=== "Russian Post"

    <span id="_5"></span>

    ### Russian Post { #russian-post }

    Only price and delivery time calculation through Russian Post's public calculator is supported. It uses the recipient's postal code, so the customer must include that code in their address. Russian Post pickup points are not available.

    Complete **Calculation object code** (the shipment type in the calculator) and **Sender postal code**. **Declared value** provides insurance: a fixed amount, the order amount, or a percentage of it, capped by **Maximum declared value**. The object code must support declared value. When insurance is enabled, CRM checks this with Russian Post and will not save an unsupported configuration.

<span id="_6"></span>

## Shipments { #shipments }

CRM creates Yandex Delivery and CDEK shipments, including shipments to CDEK pickup points outside Russia. Create Ozon and Russian Post shipments in the carrier's account. Update those order statuses manually.

The following rules apply to shipments in CRM.

- A shipment is created as soon as an order becomes **Paid**, without waiting for the hourly check. It is prepaid, with no cash on delivery: the customer pays nothing on receipt, and the carrier charges you under your contract.
- If you accept an order before it becomes **Paid**, or use payment on receipt, no shipment is created automatically. Create it in the carrier's account. The order's section will show **Not created**.
- CRM checks active shipments at the start of each hour. When the carrier accepts the parcel, the order becomes **In delivery**; when it is delivered, the order becomes **Completed**. Arrival at a pickup point does not complete the order. If the order is already **Pending pickup**, acceptance does not change its status, but delivery completes it.
- Canceling an order does not cancel its shipment. Manage waybills, labels, and collections in the carrier's account.

<span id="_7"></span>

### Delivery information { #delivery-information }

The order's **Delivery information** section shows **Shipment status** and **Tracking number**. CRM checks the status automatically.

If the status is **Needs attention**, check **Diagnostic message** in this section. If the shipment has not been created and **Retry after correction** is available, fix the issue and click the button.

Expand **Technical delivery details** for information about other failures and the remaining manual actions. **Next check** shows when CRM will request an update.

- **Create shipment**: available when shipment status is **Not created** and the order is **Paid**.
- **Check with carrier**: available after a registration attempt while the order is not **Completed**, **Canceled**, **Returned**, or **Payment error**. It does not wait for the hourly check. If the response during creation was lost, it first looks for an existing shipment to avoid a duplicate. After a few seconds, click **Refresh displayed data** to reload the order details.

| Shipment status | Meaning and action |
|---|---|
| Not created | Payment is unconfirmed or payment on receipt is used. Wait for Paid or create the shipment with the carrier |
| Awaiting registration, Registering | Creation is in progress; wait |
| Registered | The carrier created the shipment but has not accepted the parcel. Prepare and hand it over; the order status does not change |
| In delivery | The carrier accepted the parcel. The order is In delivery; the next change follows delivery to the customer |
| Delivered | The order is Completed; checks stop |
| Result being confirmed | The carrier's response was lost or the status is unknown. Click Check with carrier if available; otherwise wait for the hourly check |
| Needs attention | The carrier rejected the shipment or required details are missing. Check Diagnostic message |
| Not delivered, Canceled | Investigate in the carrier's account and handle the order manually; it is not marked successfully completed automatically |

**Examples under Diagnostic message**

- Yandex: **Complete company connection and accept the offer in your Yandex Delivery account** means the contract and offer steps are incomplete. Complete them, then click **Retry after correction**.
- CDEK: the sender's name, phone, origin point, or address is missing, or the order has no recipient details.
- **Shipment settings changed before registration; check them and retry after correction** means the fulfillment method or account changed while the shipment was awaiting creation.

Checks stop after **Delivered**, **Not delivered**, **Canceled**, or **Needs attention**, and when the order becomes **Completed**, **Canceled**, **Returned**, or **Payment error**.
