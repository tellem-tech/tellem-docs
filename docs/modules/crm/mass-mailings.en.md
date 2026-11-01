---
description: "Prepare and send Tellem mailings, choose an audience, check available channels, and review the result."
---

<span id="_1"></span>

# Campaigns and mailings { #mailings }

Create a campaign for customers in selected segments and send a message immediately or at a scheduled time. Only the CRM owner can create and launch campaigns.

Where: **Marketing → Mailings**. On a phone, choose **Actions → Create**.

On a computer, **More** contains “Send now”, “Repeat”, and “Cancel”. On a phone, use **Actions**.

<span id="_2"></span>

## Recipients and channels { #recipients }

Mailings go to customers with mailings enabled, through every available channel they have not disabled in their [profile](../app/account.md#channels):

- Telegram: the integration is enabled, and the customer has started the bot and has not blocked it;
- VK: the [store community is connected](vk.md), and the customer has linked VK ID and allowed messages;
- email: the address is verified and email sending is available to the store.

Choose a channel, **“Auto”**, or **“All channels”**. The latter two use all channels the customer has enabled. Images go only to Telegram; VK receives text and links, and email receives text. An image-only message goes only to Telegram. Mailings do not use push.

In **“Segments”**, combine up to 20 standard RFM segments and [saved segments](segments.md) from one location. A customer matching several choices joins the audience once. RFM covers all time; the analytics report period does not change the audience. Archived segments cannot be selected or launched.

CRM selects a single location automatically. Changing the location keeps standard RFM choices and clears incompatible saved segments.

Review the available recipient count on the right. Expand **“Excluded”** for opt-outs, unavailable channels, and the frequency limit. CRM flags an audience smaller than 30 customers; you can still save the campaign.

CRM fixes the audience membership at launch. Later segment changes and new orders do not alter it; CRM checks consent and channel availability before sending. By default, a customer participates in at most one new campaign per location in seven days across all channels. An unknown result keeps the restriction. CRM does not reconstruct audience membership for older sends.

!!! warning "Advertising requires separate consent"
    The mailing switch covers informational messages. It does not replace separate prior consent for advertising. Sellers obtain consent and are responsible for message content; see [Legal documents](../../legal/index.md).

[Points expiry reminders](bonus-system.md#expiry) are configured separately and are unaffected by opting out of mailings.

<span id="create-a-mailing"></span>

<span id="_4"></span>

## Create and send { #create-and-send }

1. Click **“Create”**. Under **“Audience and goal”**, set the name, location, purpose, and audience. **“Segments”** contains **“Standard”** and **“Saved”** groups.
2. Under **“Message”**, select the channel and enter the text. The preview updates as you type. For “Auto” and “All channels”, switch **“Message appearance”** between Telegram, VK, and email; this does not change the sending channel.
3. Under **“Schedule”**, set a date at least two minutes ahead and an **“Observation window”** of 7, 14, or 30 days. CRM uses this window to show the campaign result.
4. Click **“Schedule campaign”**, check the audience and channel, then confirm. Sending starts within a minute after the scheduled time. For an early send, select **“Send now”** in the list and confirm.

??? example "Example: create a campaign"

    Demo data: standard and saved segments, text, preview, and scheduling. The shared GIF shows Russian interface labels and captions.

    <figure markdown="span">
    [![Create a campaign: segments, text, preview, date, and scheduling confirmation](../../media/crm/campaign-creation.gif){ width=720 height=900 loading=lazy }](../../media/crm/campaign-creation.gif)
    </figure>

Under **“Formatting”**, choose Markdown or HTML and open the help. The text limit is 4,000 characters, or 9,000 for VK. VK receives plain text and links. The form checks formatting before saving; correct any errors it reports.

**“Add image”** accepts SVG, PNG, JPEG, GIF, WebP, BMP, or HEIC up to 10 MB. In Telegram, the image and text arrive in one card. HTML preserves emphasis, links, and line breaks. Markdown uses the previous Telegram rules, so saved mailings do not need to be rewritten.

Only an “Await” campaign can be edited or cancelled; other campaigns are available for viewing. To repeat a campaign that has started, create a new one instead of editing the original.

<span id="email"></span>

<span id="_5"></span>

### Email behavior { #email-behavior }

The first line becomes the subject and heading, up to 100 characters. HTML keeps formatting; Markdown arrives as text without conversion. Tellem adds the layout and footer. Without text, no email is sent.

<span id="list-and-statuses"></span>

<span id="_3"></span>

## Check the result { #results }

| Status | Meaning and next action |
| --- | --- |
| “Await” | Waiting for its date; edit, cancel, or send now |
| “In progress” | Sending; wait for the result |
| “Sent” | Every channel accepted the message for at least one customer; this does not confirm reading |
| “Canceled” | Cancelled manually or nobody has an available channel |
| “Failed” | No channel accepted the message or validation failed before sending |
| “Partially sent” | Some channels accepted the message and others did not |
| “Unknown result” | A channel did not confirm acceptance; the message may have arrived. Repeat is blocked |

**“Repeat”** creates a new campaign with the original text, image, format, all segments, location, and observation window. At launch, CRM selects the audience again and checks frequency. After partial sending, a repeat may duplicate messages in channels that accepted them; check the result before sending again.

## Assess a campaign { #campaign-result }

Assess a mailing through its audience's actions: how many customers visited the store, how many
bought, and how much revenue their orders generated. The share of buyers and revenue per participant
help you compare campaigns with different audience sizes. Use the same observation window
and wait for the final result when comparing.

1. Under **“Marketing → Mass mailings”**, select a sent campaign and click **“Result”**.
2. Compare **“Audience”**, **“Visited the store”**, and **“Made a purchase”**. The **“Share of buyers”** bar shows how much of the original audience placed an order.
3. Review **“Revenue”** and **“Revenue per participant”**. The order count and average order value help explain the total.

???+ example "Example: assess a campaign result"

    Demo data: of 100 participants, 40 visited the store and 20 bought.
    The share of buyers is 20%, revenue from 25 orders is ₽37,500, and revenue per participant is ₽375.
    The recording shows the Russian interface.

    <figure markdown="span">
    [![Assess a campaign: open its result, compare audience, visits and purchases, then review the share of buyers and revenue](../../media/crm/crm-campaign-result.en.gif){ width=960 height=540 loading=lazy }](../../media/crm/crm-campaign-result.en.gif)
    </figure>

The preview next to the figures shows the selected mailing. Click **“Expand”** to read a long message
in full; for multiple channels, you can switch its appearance. Click the short text in the mailing
list to open the full message. You can also open the result from a
[customer record](clients.md#campaigns): under **“Campaigns”**, select a row and click **“Campaign result”**.

The 7-, 14-, or 30-day window includes the entire sending day and the following 6, 13, or 29 CRM
calendar days. A morning visit and evening purchase on the day of an afternoon mailing both count.
The sending time does not limit visits or purchases within that day. CRM counts only the campaign
location and completed orders; an order with zero revenue still counts as an order.

The share of buyers divides buyers by the original audience. Revenue per participant uses the
same audience as its denominator; average order value uses the order count. Repeat views and visits
on different days count as one visitor over the window. Visitors are signed-in customers who open
a product or category; some views may be missing from the statistics. Purchases count independently.

Results remain preliminary while the window is open. CRM refreshes them daily and includes later
returns and order corrections after the window closes. For a preliminary result, click **“Refresh”**
to request updated figures. Final results do not show this button.
The screen keeps previous values during the update. When data is unavailable, it marks the saved
values. “—” means a value is unavailable, including unavailable visit history.

Audience means campaign participation without individual delivery confirmation. Unsubscribing
after launch does not change the original audience size. Customers may receive other mailings or
buy for other reasons, so these figures do not measure additional revenue caused by the campaign.
For audiences of fewer than 30 customers, consider the small sample when comparing. Older mailings without
a saved audience and campaigns with unconfirmed sending may have no result.

<span id="create-with-ai"></span>

## AI assistance { #ai }

**“Write with AI”** appears when the [AI integration](integrations.md#ai) is enabled and has an API key. First select the campaign audience and location.

Select a purpose or **“Choose automatically”** to let AI suggest a purpose from all selected segment conditions. Add optional wishes of up to 1,000 characters and click **“Generate”**. Review the message and the **“Why this message”** explanation, then click **“Apply”**. The campaign purpose and text stay unchanged until you apply; AI does not change the audience or location. You can cancel the request or generate another version. For VK, AI drafts plain text.

AI uses segment conditions, stores, catalog information, popular products, active promotions, and promo codes, including their codes. AI also considers daily segment history and past campaigns with the same location, purpose, channel, and observation window. The explanation describes facts, comparison limits, and a hypothesis for the new mailing. If history is missing or limited, AI still proposes a message and explains what is unknown. The recipient list is not included. Before applying, check prices, conditions, and codes against CRM.

## Customer history { #customer-history }

In the [customer record](clients.md#campaigns), choose a location and open **“Campaigns”**. Select a row and click **“Open campaign”** to review its original message and audience. Membership does not confirm delivery or reading. Merging accounts combines history rows and marks the merge; the original audience size remains unchanged.
