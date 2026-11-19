---
description: "Find customers who are due to order again, remind them about a familiar item, and calculate orders per participant."
---

# Remind customers when it's time to reorder { #reorder }

Use the **“Due”** status to send a reminder once the location's usual interval has passed since the customer's last order.

## 1. See who may be ready for a reminder { #diagnose }

1. Under **Analytics → Repeat orders**, select a location. Under **“Who to remind”**, click **“Due”** and see how many customers are in the list.
2. In **“When customers buy again”**, check the usual interval for buyers who have placed several orders. Review recent orders in a few [customer records](../clients.md#customer-record). Pick a product customers come back for and that is in stock.

## 2. Save the segment and schedule the reminder { #launch }

1. Under **Analytics → Segments → Create segment**, select the same location. Set **“Order count: from”** to **2**. In **“Repeat purchase status”**, select **“Due”**.
2. If the reminder is about one category or item, add **“Favourite category”** or **“Favourite product”**. Review the audience size and save the segment as “Due to reorder”.
3. Under **Marketing → Mailings → Create**, select the same location, this segment from **“Saved”**, and **“Increase purchase frequency”**. Write a short reminder with a link to the familiar item, such as coffee beans. Review the audience and [schedule the campaign](index.md#prepare-campaign) with a **7-day** window.

**Example message**

> Running low on coffee? The beans from your previous order are in stock.

???+ example "The Due to reorder segment"

    Demo data. The recording shows the Russian interface.

    <figure markdown="span">
    [![In the segment builder, select the Due status and check the customer count.](../../../media/crm/repeat-reorder.en.gif){ width="960" height="540" loading=lazy }](../../../media/crm/repeat-reorder.en.gif)
    </figure>

## 3. Review the share of buyers and order count { #review }

After the window closes, select the mailing and open **“Result”**. In this example, **48** of **128 participants** made a purchase (**37.5%**). They placed **60 orders**, or **0.47 orders per participant**. To calculate this metric, divide **“Orders”** by **“Audience”** and round to two decimal places.

Keep the share of buyers and orders per participant for [your next comparison](index.md#read-result). If the share of buyers holds steady and orders per participant rise, see whether the pattern holds in the next comparable window.
