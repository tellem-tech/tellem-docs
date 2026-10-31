---
description: "Review sales, repeat purchases, RFM groups, cohorts, customer sources, and report exports in Tellem."
---

<span id="_1"></span>

# Home and analytics { #home-and-analytics }

Use Home and Analytics to review sales, repeat purchases, and customers. Home and Overview show the same metrics when their filters match.

Where: **Home** and **Analytics**.

<span id="_2"></span>

## Filters and calculations { #filters-and-calculations }

Select the period, locations, city, order type, and platform. For another period, choose “Custom dates” and enter “From” and “To”. Filters are saved in the link.

A single location is selected automatically. With several locations, an empty selection means the whole chain.

Purchase metrics include only completed orders, using the order date in the CRM time zone. Revenue includes delivery and payment fees, with redeemed points deducted. Cancellations, returns, and payment failures do not count as purchases. Editing an old order changes the metrics for its original period.

A new customer placed their first completed order across the chain in the selected period. A location or platform filter does not change that first purchase date. For a small audience, some shares and percentage changes are hidden; absolute values appear instead. “—” means a metric or comparison cannot be calculated.

<span id="_3"></span>

## Home { #home }

Use the information button to read metric formulas. Changes are compared with the preceding period of the same length. “View guests” on a card opens the corresponding customer list.

??? example "Example: Home metrics"

    Example with demo data. The image shows the Russian interface.

    <figure markdown="span">
    [![Metric cards on Home; the new customers card with its change arrow and the button that opens the guest list is highlighted.](../../media/crm/crm-dashboard.en.png){ width="1280" height="720" loading=lazy }](../../media/crm/crm-dashboard.en.png)
    </figure>

Inactive guests have no completed orders in the 90 days ending at the selected period's end, or at the current moment if earlier. Without filters, the chain-wide base includes guests who have never purchased. With a location selected, including the only location selected automatically, or a city, order type, or platform filter, it includes all-time buyers in that selection.

## Sales by day and time { #sales-by-time }

In **Analytics → Overview**, choose a period and locations. Use **Breakdown** in the revenue card:

- **Over time**: totals by date, week or month, depending on the length of the period.
- **By weekday**: totals for Mondays, Tuesdays and the other weekdays within the selected period.
- **By time of day**: **Start of day [00:00,11:00)**, **Middle of day [11:00,16:00)** and **End of day [16:00,24:00)** in the CRM time zone.

Each breakdown shows revenue and the number of completed orders. These are period totals: a partial week can give some weekdays more occurrences than others. Use the purchase distribution to plan promotions; the chart does not measure the effect of mailing send times.

The card’s **Download CSV** button exports the selected breakdown with the current filters. The new and returning customers chart and the Home sales chart keep their date grouping.

??? example "Example: revenue breakdowns and CSV"

    Demo data, recorded in the Russian interface.

    <figure markdown="span">
    [![Analytics → Overview: calendar, weekday and time-of-day breakdowns, then CSV export of the selected breakdown.](../../media/crm/crm-sales-breakdowns.en.gif){ width="960" height="540" loading=lazy }](../../media/crm/crm-sales-breakdowns.en.gif)
    </figure>

## Customers and RFM { #rfm }

In **Analytics → Customers**, buyers are grouped by how recently they purchased, how often they buy, and how much they spend. This grouping method is called RFM. Select a segment to view its customers, then open a guest's record. “All customers” beside the matrix also includes guests without purchases in the chain-wide view.

???+ example "Example: from the RFM matrix to a customer's orders"

    Example with demo data. The recording shows the Russian interface.

    <figure markdown="span">
    [![Analytics, Customers: the RFM matrix, the champions segment, the segment's customer list, opening a guest, the customer portrait window and its Orders tab.](../../media/crm/crm-rfm-drilldown.en.gif){ width="960" height="540" loading=lazy }](../../media/crm/crm-rfm-drilldown.en.gif)
    </figure>

The matrix calculates RFM over the entire history of the selected locations: a customer's purchases are combined, and each customer counts once. Mailings and saved segments use a separate all-time calculation for each location, updated separately, including after saving **Settings → RFM analytics**. The groups can therefore differ. Guests without completed orders receive no RFM segment.

### Audience segments { #audience-segments }

To select customers using your own conditions and estimate whether you can contact them, open **Analytics → Segments**. See [Segments](segments.md) for steps and limitations.

<span id="_4"></span>

## Cohorts { #cohorts }

In **Analytics → Repeat orders**, under “Cohort analysis”, compare repeat purchases by customers who first bought in the same month. This group is called a cohort.

??? example "Example: cohort table"

    Example with demo data. The image shows the Russian interface.

    <figure markdown="span">
    [![Cohort retention table: the May 2026 row is highlighted — 10 customers, 100% in M+0 and 60% (6 of 10) in M+1.](../../media/crm/crm-cohorts.en.png){ width="1280" height="720" loading=lazy }](../../media/crm/crm-cohorts.en.png)
    </figure>

- Each row is the month of the first completed purchase; “Customers” shows the group size.
- “M+0” is 100%. Later months show the share of returning customers and “N of M”. Each customer counts once per month; future months show “—”.
- “Cohort year” selects the first purchase year. Repeat purchases also count in the following year. Completed orders from all stores count by their completion date.
- Cohorts cannot be selected for mailings.

<span id="_5"></span>

## Overview { #overview }

In **Analytics → Overview**, you can view sales metrics, location comparisons, detailed breakdowns, and registrations. Under **Order diagnostics**, **Failed payments** shows the share of orders with a payment error among all orders in the selected period.

“Registrations” includes guests who registered during the period, including those without purchases. Order type and platform filters keep guests with matching purchases. Without tags, “First known attribution”, meaning the first known customer source, shows “Unknown”; it is not inferred from the order platform.

Without purchases, charts are hidden, but registrations and inactivity remain available. CSV exports use the current filters; the guest list exports in full, including other pages. See [Customers](clients.md) for working with a customer record.

<span id="_6"></span>

## Tags { #tags }

In **Analytics → Sources**, compare [first and repeat purchases by tag](utm-marks.md#effectiveness). The charts below show [invitation link assignments](utm-marks.md#tag-links), including existing customers.

<span id="_7"></span>

## Reports { #reports }

Open **Reports → Stock reports**, choose “Warehouse stock”, and click “Download”. Excel buttons on the orders, customers, products, and inventory screens export their tables.
