---
description: "Create, save, and archive audiences in Tellem analytics and understand their usage restrictions."
---

<span id="_1"></span>

# Segments { #segments }

Select customers by conditions and check how many you can contact. This screen does not send messages.

Where: **Analytics → Segments**. On narrow screens, the table buttons are under “Actions”.

<span id="_2"></span>

## Explore an audience { #explore-an-audience }

Select a segment to see its sales area, conditions, customer counts, and contacts. Membership uses current data; RFM groups use the [saved calculation](analytics.md#rfm).

Contact requires mailings to be enabled and a contact in the selected channel. The table also includes customers you cannot contact. Changing the channel updates the availability estimate without changing conditions. “Refresh preview” recalculates results; the list is not fixed for a future campaign.

<span id="_3"></span>

## Create or edit { #create-or-edit }

1. Click “Create segment” and enter a name and sales area. A single location is selected automatically. Customer profiles are evaluated across all time for that area.
2. Choose conditions for purchases, RFM groups, products, fulfillment, time, or source.
3. Check the customer count and click “Create segment”; in an existing segment, “Save changes”. The detailed table appears on the main screen.

???+ example "Example: creating a segment"

    Example with demo data. The recording shows the Russian interface.

    <figure markdown="span">
    [![Creating a segment in Analytics, Segments: the segment builder, the name, the condition of up to 30 days since the last order, the customer count and message availability, Create segment, then the segment tiles and its customer table.](../../media/crm/crm-segment-create.en.gif){ width="960" height="540" loading=lazy }](../../media/crm/crm-segment-create.en.gif)
    </figure>

All selected conditions apply together; an empty field imposes no restriction. An unknown value does not match a condition: for example, no profile does not mean zero orders. Avoid the negative-feedback condition: its data is not collected, so both “Yes” and “No” produce an empty audience.

Under **“RFM and repeat purchases”**, use **“Repeat purchase status”** to save customers marked [“Due” or “Asleep”](analytics.md#repeat-orders). Choose the conditions for your audience in the [repeat-purchase guides](repeat-purchases/index.md).

“Edit conditions” opens an existing segment. “Save changes” updates it; “Save as new” creates a copy. “Cancel” keeps the previous conditions. If the segment was changed in another tab, save your input as new or reopen it.

<span id="_4"></span>

## Archive { #archive }

“Archive” removes a segment from “Saved”. Under “Archive”, choose “Restore and save”, review the conditions, and save to restore it. Segments cannot be deleted.

Segments are shared: any CRM user can change or archive them. The [RFM matrix](analytics.md#rfm) uses its own filters. A [campaign](mass-mailings.md#recipients) can use a segment saved here alongside standard RFM groups from the same location.
