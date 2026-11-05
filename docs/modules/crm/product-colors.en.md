---
description: "Group Tellem products by color: configure a template, variants, stock, and customer color selection."
---

<span id="_1"></span>

# Combining two products by color { #combining-two-products-by-color }

Combine two separate products into one group so customers can choose a color directly in the product card.

Where: **Catalog → Products**.

In this example, a café sells two products from the Matcha category, **Demo matcha pink** and **Demo matcha green**, for **295 rubles** each. Only the color and the photo differ.

<span id="1"></span>

## 1. Prepare two products { #1-prepare-two-products }

The catalog must already contain two simple products:

| Product | Photo | Price |
|---|---|---|
| Demo matcha pink | Pink drink | 295 rubles |
| Demo matcha green | Green drink | 295 rubles |

If the products do not exist, add each through **Create → Create single** — see [Categories and products](products-and-categories.md). You cannot merge iiko products manually: their variants are created from [menu sizes](iiko.md#sizes-and-extras).

!!! warning "Before merging"
    The selected products must not yet have any orders. Only regular products can be merged. Record their stock quantities by store and article codes: you will need to set them again after merging. Saving the new group replaces the original products.

<span id="2"></span>

## 2. Merge the products { #2-merge-the-products }

1. Select **Group variative products**.
2. Search for “Demo matcha” and press **Enter**.
3. Select both rows using the checkboxes.
4. Open **Actions → Transform to variants**.
5. In the product editor, set **Name of group** to **Demo matcha** and check the category.

<span id="3"></span>

## 3. Add the Color attribute { #3-add-the-color-attribute }

On **Main**, under **Variative attributes**, click **Create**. In the attribute template window, select **Color** and click **Select**.

If no suitable template exists, create one in the same window: set **Name** to **Color**, **Type** to **Color**, and click **Save**. Then select the template for the group.

???+ example "Example: from two products to the Color attribute"

    Example with demo data. The recording shows the Russian interface.

    <figure markdown="span">
    [![Merging products by color: Group variative products is selected, “Demo matcha” is typed into the search, two rows are ticked, Actions → Transform to variants opens the product editor, “Demo matcha” is entered as the group name, then Create under Variative attributes opens the templates, Color is ticked and Select is clicked.](../../media/crm/crm-product-colors-merge.en.gif){ width="960" height="540" loading=lazy }](../../media/crm/crm-product-colors-merge.en.gif)
    </figure>

The **Color** type gives customers colored circles. A text attribute with the same name shows text buttons.

<span id="4"></span>

## 4. Assign colors to variants { #4-assign-colors-to-variants }

In the variants list, select the pink variant and click **Edit**. In its card, scroll to **Variative attributes** and click **Edit** in the **Color** row.

Choose an existing shade or **Create…**. For a new color, enter its name and choose a shade using the colored square:

| Variant | Color name | Example color code |
|---|---|---|
| Demo matcha pink | Pink | `#E7A3AD` |
| Demo matcha green | Green | `#2ECC71` (existing shade) |

Save the color, check the variant's photo and price, set an article code such as **DEMO-PINK**, and click **Save** in the variant card. Repeat for the green variant with **DEMO-GREEN** and choose the existing shade **Green** from the list. The color values must differ.

To show **one card** in the category, leave **Show in catalog** enabled only for the pink variant. Green remains available through the selector inside the card. To show both cards in the category, enable this checkbox for both variants.

<span id="5"></span>

## 5. Set stock and save { #5-set-stock-and-save }

On **Assortment**, select a store and set each variant's quantity using **Edit** in its row. Confirm each row using the checkmark button. This example uses **30 pieces** of each color. Repeat for other stores as needed — see [Inventory](inventory.md).

Click **Save** at the bottom of the product editor. If the CRM offers to configure empty stock in other stores, choose **Yes** to configure it or **No** if the product is not yet sold there.

???+ example "Example: colors, article codes, and stock of the variants"

    Example with demo data. The recording shows the Russian interface.

    <figure markdown="span">
    [![Colors and stock of the variants: the pink variant is ticked and Edit opens its card, the color Pink is created under Variative attributes, the article code DEMO-PINK is entered and Save is clicked. The green variant follows the same steps faster with the color Green and DEMO-GREEN. Show in catalog is turned off for green, both variants get a quantity of 30 on Assortment, and Save with the answer No finishes.](../../media/crm/crm-product-colors-variants.en.gif){ width="960" height="540" loading=lazy }](../../media/crm/crm-product-colors-variants.en.gif)
    </figure>

<span id="6"></span>

## 6. Check the customer experience { #6-check-the-customer-experience }

Open the app, select the correct store, and find Demo matcha pink in the Matcha category. The card shows **Color: Pink** and two colored circles below the price. Tapping the green circle switches the variant: the photo, name, color label, and article code change. An outline marks the selected circle.

???+ example "Example: choosing a color in the product card"

    Example with demo products. The recording shows the Russian interface.

    <figure markdown="span">
    [![App: a guest opens the catalog and the Matcha category, then the Demo matcha pink card with the label Color: Pink and two colored circles. Tapping the green circle opens Demo matcha green with the article code DEMO-GREEN, and tapping the pink circle brings back the first variant.](../../media/app/app-product-colors.en.gif){ width="960" height="540" loading=lazy }](../../media/app/app-product-colors.en.gif)
    </figure>

The example price stays at **295 rubles**; if variants have different prices, it changes too. The purchase buttons apply to the selected color. Before opening sales, switch between both colors and check photos, prices, and stock. More details: [Storefront and cart](../app/ui-and-pages.md).
