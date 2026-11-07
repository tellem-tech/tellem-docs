---
description: "Find and choose products in the Tellem app, select variants, use favorites and the cart, and proceed to checkout."
---

<span id="_1"></span>

# Storefront and cart { #storefront-and-cart }

Choose products in the catalog and add them to your cart. Guests can browse products, choose variants and extras, and edit the cart. The app asks you to [sign in](account.md) at checkout or when opening favorites and orders.

If the store shows **18+ content**, continue only after confirming **I am 18 or older**.

<span id="_2"></span>

## Home screen { #home-screen }

Tap the name and address in the header to choose a store or store chain (sales area). The catalog and stock depend on your choice. A guest opening a store-specific link or QR code goes to that store's catalog.

??? example "Example: choosing a sales area"

    Example with demo data. The recording shows the Russian interface.

    <figure markdown="span">
    [![The home screen: tapping the name and address in the header, the sheet for choosing a sales area listing two areas, choosing the second one, and the updated home screen with its catalog.](../../media/app/app-zone-switch.en.gif){ width="960" height="540" loading=lazy }](../../media/app/app-zone-switch.en.gif)
    </figure>

Open **Catalog** to choose products, **Favorites** for saved items, or **Previously ordered** to find past purchases. Home screen blocks and warnings depend on store settings; the store warning appears only after sign-in.

Search is at the bottom. The cart button appears when it contains products and shows their quantity and amount.

??? example "Example: the home screen with a cart"

    Example with demo data. The image shows the Russian interface.

    <figure markdown="span">
    [![The home screen: the store name and address in the header; the Catalog and Favorites buttons and the previously ordered heading are highlighted; Search and the cart button with 580 RUB and 2 items are at the bottom.](../../media/app/app-home-overview.en.png){ width="1280" height="720" loading=lazy }](../../media/app/app-home-overview.en.png)
    </figure>

<span id="_3"></span>

## Catalog and search { #catalog-and-search }

Choose a category or enter a search query; product and category results appear as you type. If there are no matches, change the query or check the selected sales area.

<span id="_4"></span>

## Product card { #product-card }

Check the description, specifications, price, and availability. If the product has variants, such as size or color, choose one before adding it. Tap a photo to open it full screen or the SKU, the product's code, to copy the code.

??? example "Example: product variants in the card"

    Example with demo products. The image shows the Russian interface.

    <figure markdown="span">
    [![The cappuccino with cheese foam card at 340 RUB: the volume row with the 300 ml and 400 ml buttons and the cheese foam row with No and Yes are highlighted.](../../media/app/app-dish-options.en.png){ width="1280" height="720" loading=lazy }](../../media/app/app-dish-options.en.png)
    </figure>

- **Buy** adds the product and opens the cart with only that product selected.
- **Add to cart** adds it without opening the cart. For an item already added, **Go to cart** opens the cart; adjust the quantity beside it, up to available stock.
- Products with no stock show an inactive **Out of stock** button. When stock is low, the card shows the exact quantity.

**Share** opens the system share menu or copies a link. For signed-in customers, the link opens the product inside Telegram if the store connected a bot; otherwise, it opens the website.

### Dish size and extras { #dish-options }

If a dish has sizes, choose the product variant you want. When adding a dish with extras, choose them in the panel that opens. Required groups have an “*”; the allowed quantity appears beside them. An extra has “−” and “+” buttons when the store allows several portions. Complete the required choices before adding the dish.

Check the total price including extras before adding it. Promotions and birthday discounts reduce the price of the dish itself; extras keep their price.

<span id="_5"></span>

## Favorites { #favorites }

Tap the heart on a product card to save it to **Favorites**. **Clear** removes the entire list after confirmation.

<span id="_6"></span>

## Cart { #cart }

Your guest cart stays in this browser when you reload or return from sign-in. Each sales area has its own guest cart. Clearing browser data removes it.

1. Select the products for your order. All items are selected when you open the cart; unselected items stay there.
2. Check quantities, which cannot exceed available stock. After reducing a quantity to zero, you can use **Undo** while the button is visible.
3. Check **Total** for the selected items and click **Place order for <amount>**. If you have not signed in, sign in or confirm your email to create an account. You then continue to [checkout](checkout.md), where you can apply promo codes, bonus points, and personal discounts. Your guest cart is added to your account cart: quantities of identical variants with identical extras are summed; different extras stay on separate lines. Check the updated prices before placing the order.

???+ example "Example: from the catalog to the cart"

    Example with demo products. The recording shows the Russian interface.

    <figure markdown="span">
    [![Choosing a category in the catalog, the cappuccino card with the 400 ml size, adding it to the cart, quantity 2, and the button to place the order for 700 RUB.](../../media/app/app-catalog-to-cart.en.gif){ width="960" height="540" loading=lazy }](../../media/app/app-catalog-to-cart.en.gif)
    </figure>

!!! warning "Deleting products"
    **Delete** removes all selected items after confirmation. You cannot undo this deletion.

Guest products are not reserved. If the store reserves products in a signed-in customer’s cart, the reservation and cart quantities reset after a period of inactivity. Check your cart again before checkout.

For a dish with extras, tap **Edit** to change the selection. The same product with different extras or extra quantities occupies separate lines; identical selections merge. The order retains the size and extras.

<span id="_7"></span>

## Profile, orders, documents, and theme { #profile-orders-documents-and-theme }

Addresses, bonus points, language, theme, and installation are available in your [profile](account.md). See [Checkout and orders](checkout.md#orders) for order statuses and actions.

[Tellem legal documents](../../legal/index.md) are linked in the app: in the footers of the home screen, profile, and **About the app**, during sign-in and checkout, and in the cookie banner. Documents open in the interface language.

!!! info "For store owners"
    Configure [product color variants](../crm/product-colors.md) and [the home screen and app colors](../crm/main-page.md). Import dish sizes and extras from the [iiko menu](../crm/iiko.md#sizes-and-extras). Warnings, reservations, and profile information sections are under [general settings](../crm/general-settings.md). Get a location's link and QR code from its [store card](../crm/stores-and-delivery.md).
