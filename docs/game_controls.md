# Monopoly Game Controls

This document outlines the user control actions for playing the Monopoly game, based on the UI logic in `src/ui_manager.py`. The game is controlled by clicking on UI elements with the mouse.

## Main Actions

*   **Roll Dice**: At the beginning of a turn, a "Roll" button is displayed. Clicking this button rolls the dice and moves the player's token.
*   **Manage Properties**: A "Manage" button is available at the start of a turn, allowing the player to build houses, mortgage properties, etc.

## Property Purchase

When a player lands on an unowned property, a dialog box appears with two options:

*   **Buy**: Clicking the "Buy" button purchases the property for the listed price.
*   **Auction**: Clicking the "Auction" button starts an auction for the property among all players.

## Card Actions

When a player draws a "Chance" or "Community Chest" card, a dialog box displays the card's text.

*   **OK**: Clicking the "OK" button dismisses the card dialog and executes the card's action.

## Other Controls

The game may present other dialogs with buttons for actions such as:

*   Choosing how to pay income tax.
*   Responding to trade offers.
*   Managing properties in the "Manage Properties" screen (building, mortgaging, etc.).
