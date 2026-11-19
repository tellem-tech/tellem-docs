---
description: "Find customers who bought once, choose a reminder day, and check how many campaign participants ordered again."
---

# Get customers to place a second order { #second-order }

## 1. See how many buyers came back { #diagnose }

1. Under **Analytics → Repeat orders**, select a location and a past date range that gave new buyers time to order again.
2. In **“Repeat purchase funnel”**, compare the first two steps. In this example, 64 of 200 customers made a second purchase, a transition rate of **32%**. Click **“No order #2 yet”** to open the customer list.
3. In **“When customers buy again”**, find **“After order #1”**. In this example, buyers typically reorder after **12 days** and CRM suggests **“Remind on day 9”**. If there is no suggestion yet, look at first and second purchase dates in the order history.

???+ example "From first to second order"

    Demo data. The recording shows the Russian interface.

    <figure markdown="span">
    [![The camera moves in on the funnel, where 64 of 200 buyers returned. It then shows the day-nine reminder and the button to open the list of customers who have yet to reorder.](../../../media/crm/repeat-second-order.en.gif){ width="864" height="486" loading=lazy }](../../../media/crm/repeat-second-order.en.gif)
    </figure>

## 2. Build the segment and launch the campaign { #launch }

1. Open **Analytics → Segments → Create segment** and select the same location. Set both **“Order count: from”** and **“Order count: to”** to **1**.
2. For this example, set **“Days since last order: from”** to **9** and **“Days since last order: to”** to **15**. Save the segment as “Second order”.
3. [Create a mailing](index.md#prepare-campaign). Under **“Saved”**, choose “Second order”. Set the goal to **“Increase purchase frequency”** and the window to **7 days**. Link to a popular item that is in stock.

**Example message**

> Thanks for your first order! If you're shopping for coffee to brew at home, try our whole beans.

## 3. Check how many participants ordered again { #review }

After the window closes, select the mailing and open **“Result”**. In this example, **24** of **100 participants** made a purchase. The **“Share of buyers”** was **24%**.

Compare 24% with the [result of a similar mailing](index.md#read-result). The funnel shows **32% among all new buyers** in the selected range. The mailing result shows **24% among its participants**.
