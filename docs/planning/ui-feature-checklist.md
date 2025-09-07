# Monopoly UI/UX Feature Checklist

This document outlines the necessary UI and UX features for a user-friendly and complete Monopoly game interface. The checkboxes indicate the current implementation status based on the source code.

---

### **1. Main Game Interface**

- [x] Display the main game board graphic.
- [x] Display player tokens on their correct board positions.
- [x] Smoothly animate token movement from one space to the next.
- [x] Handle multiple tokens on the same space by offsetting them so all are visible.
- [x] Display the result of the last dice roll.
- [ ] Visually indicate property ownership on the board itself (e.g., with a colored marker).

### **2. Player HUD (Heads-Up Display)**

- [x] Display a list of all players.
- [x] Clearly show each player's current money total.
- [x] Highlight the current player whose turn it is.
- [x] Indicate special player statuses (e.g., "In Jail", "Bankrupt").
- [ ] Display a list of properties owned by each player in the HUD.

### **3. User Input & Controls**

- [x] Provide a "Roll Dice" button for the current player to start their turn.
- [x] Provide a "Manage Properties" button to allow players to build, sell, or mortgage.
- [ ] Implement keyboard shortcuts for common actions (e.g., 'R' to roll, 'M' to manage).
- [ ] Allow players to click on any property on the board (owned or unowned) to view its details.

### **4. Dialogs & Pop-ups**

- [x] **Property Purchase:** When a player lands on an unowned property, a dialog appears with options to "Buy" or "Auction".
- [x] **Tax Payment:** When a player lands on Income Tax, a dialog appears with options to pay the flat rate or 10%.
- [x] **Card Draw:** When a player lands on a card space, a dialog appears displaying the text of the drawn card.
- [ ] **Auction:** A dedicated UI for players to bid on a property, showing the current bid and allowing players to increase their bid or drop out.
- [ ] **Trade:** A dedicated UI for players to propose and accept trades, allowing them to select properties, money, and cards to offer.

### **5. Property Management Screen**

- [x] Display a list of all properties owned by the current player.
- [x] Provide options to build houses/hotels on properties within a monopoly.
- [ ] Provide options to sell houses/hotels back to the Bank.
- [x] Provide options to mortgage or unmortgage properties.
- [ ] The UI should enforce the "build evenly" rule by disabling build buttons on properties that would violate the rule.
- [ ] The UI should clearly show the cost to build or the return from selling/mortgaging.
- [x] Provide a "Back" button to return to the main game view.

### **6. Game Over Screen**

- [x] When the game ends, display a screen announcing the winner.
- [x] Provide an option to exit the game from the game over screen.
- [ ] Provide an option to start a new game.
