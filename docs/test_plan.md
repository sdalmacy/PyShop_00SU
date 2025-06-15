# Test Plan

This document outlines the unit tests implemented for the project.

## Accounts App
- **Account model**: verifies that the string representation returns the username and that a record can be created.
- **Index view**: ensures the `/accounts/` endpoint returns a 200 response containing `Accounts Home`.

## Products App
- **Product model**: creation and retrieval of a product.
- **Offer model**: creation of an offer entry.
- **Index view**: ensures the main products page renders `index.html` and displays stored products.
- **New view**: verifies the `new/` endpoint returns the welcome message.

## Orders App
- **Order model**: creation of an order and associated order item.
- **Index view**: simple endpoint returning `Orders Home`.

## Payments App
- **Payment model**: creation of a payment linked to an order.
- **Index view**: simple endpoint returning `Payments Home`.
