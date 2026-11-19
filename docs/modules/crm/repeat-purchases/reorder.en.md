---
description: "Find customers who are due to order again, remind them about a familiar item, and calculate orders per participant."
---

# Remind customers when it's time to reorder { #reorder }

## 1. See who may be ready for a reminder { #diagnose }

1. Under **Analytics → Repeat orders**, select a location. Under **“Who to remind”**, click **“Due”** and see how many customers are in the list.
2. In **“When customers buy again”**, check the usual number of days between orders. Look at favourite products under **“Profile”** in a few [customer records](../clients.md#customer-record). Choose a product that is in stock.

## 2. Save the segment and schedule the reminder { #launch }

1. Under **Analytics → Segments → Create segment**, select the same location. Set **“Order count: from”** to **2**. In **“Repeat purchase status”**, select **“Due”**.
2. If the reminder is about one category or item, add **“Favourite category”** or **“Favourite product”**. Review the audience size and save the segment as “Due to reorder”.
3. [Create a mailing](index.md#prepare-campaign) for that segment from **“Saved”**. Set the goal to **“Increase purchase frequency”** and the window to **7 days**. Remind customers about the familiar item and add a link.

**Example message**

> Running low on coffee? Whole coffee beans are in stock.

???+ example "The Due to reorder segment"

    Demo data. The recording shows the Russian interface.

    <figure markdown="span">
    [![In the segment builder, select the Due status and check the customer count.](../../../media/crm/repeat-reorder.en.gif){ width="864" height="486" loading=lazy }](../../../media/crm/repeat-reorder.en.gif)
    </figure>

## 3. Review the share of buyers and order count { #review }

After the window closes, select the mailing and open **“Result”**. In this example, **48** of **128 participants** made a purchase (**37.5%**). They placed **60 orders**, or **0.47 orders per participant**. To calculate this metric, divide **“Orders”** by **“Audience”** and round to two decimal places.

Compare with a [similar mailing](index.md#read-result). If orders per participant went up, check how the share of buyers changed.
