# Monopoly Game Actions

This document outlines the possible actions a player can take during their turn in the Monopoly game, based on the logic in `src/game_manager.py`.

## Core Turn Actions

*   **Roll Dice**: The primary action at the start of a player's turn (if not in jail).
*   **Buy Property**: If a player lands on an unowned property, they have the option to buy it from the bank.
*   **Pay Rent**: If a player lands on a property owned by another player, they must pay the owner the calculated rent.
*   **Auction Property**: If a player lands on an unowned property and chooses not to buy it, the property is auctioned off to the highest bidder among all players.
*   **Draw Card**: Landing on a "Chance" or "Community Chest" space requires the player to draw a card and follow its instructions.
*   **Pay Tax**: Landing on a "Luxury Tax" or "Income Tax" space requires the player to pay the specified amount to the bank.
*   **End Turn**: Once a player has completed all their actions, they end their turn. If they rolled doubles, they get to roll again.

## Jail Actions

*   **Use "Get Out of Jail Free" Card**: A player can use this card to get out of jail at the start of their turn.
*   **Roll for Doubles**: A player can try to roll doubles to get out of jail. This can be attempted for up to three turns.
*   **Pay Fine**: After three failed attempts to roll doubles, a player must pay a fine to get out of jail.

## Property Management Actions

These actions can typically be performed at any point during a player's turn.

*   **Build Houses/Hotels**: If a player owns all properties in a color group (a monopoly), they can build houses or hotels on them to increase the rent.
*   **Sell Houses/Hotels**: Players can sell buildings back to the bank for half the purchase price.
*   **Mortgage Property**: A player can mortgage a property to the bank to receive cash. No rent can be collected on mortgaged properties.
*   **Unmortgage Property**: A player can pay back the mortgage with interest to lift the mortgage on a property.
*   **Trade**: Players can trade properties, money, and "Get Out of Jail Free" cards with each other.

## Other Actions

*   **Go to Jail**: A player is sent to jail if they land on the "Go to Jail" space, draw a card that sends them to jail, or roll doubles three times in a row.
*   **Bankruptcy**: If a player cannot pay their debts to another player or the bank, they are declared bankrupt and are out of the game. Their assets are turned over to the creditor.
