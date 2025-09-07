# Monopoly - Implementation Plan

This document outlines a step-by-step plan to implement all remaining features identified in the `feature-checklist.md` and `ui-feature-checklist.md` documents.

### **Step 1: Core Game Rule Adjustments**

This step focuses on small but important corrections to the existing game logic to align it more closely with the official rules.

*   **Tasks:**
    1.  Modify the `start_game` logic in `game_manager.py` to handle ties in the initial dice roll by making the tied players re-roll.
    2.  Update the `handle_jail_turn` logic in `game_manager.py` to give the player the *option* to pay the $50 fine on any of their turns in jail, rather than forcing it after the third turn.
    3.  Ensure a player in jail can still perform actions like collecting rent (this is a passive action and should already work, but needs verification) and initiating property management.

*   **Features Completed After This Step:**
    *   `feature-checklist.md`:
        *   [x] Handle ties in the initial dice roll by having the tied players re-roll.
        *   [x] While in Jail, a player can perform all normal actions (collect rent, build, trade, etc.).
        *   [x] Player has the option to pay a $50 fine on their turn to get out.

### **Step 2: Implement Advanced Card Actions**

This step will complete the functionality of the Chance and Community Chest decks by implementing the remaining card actions.

*   **Tasks:**
    1.  In `game_manager.py`, add logic to handle the `MOVE_TO_NEAREST` action for Utilities and Railroads.
    2.  Add logic for the `MOVE_BACK` action.
    3.  Implement the `PAY_REPAIRS` action, which requires iterating through a player's properties to calculate the total cost based on houses and hotels.
    4.  Implement the `PAY_EACH_PLAYER` and `RECEIVE_FROM_EACH_PLAYER` actions, which involve transactions with all other active players.

*   **Features Completed After This Step:**
    *   `feature-checklist.md`:
        *   [x] `MOVE_TO_NEAREST`: Move to the nearest Utility or Railroad.
        *   [x] `MOVE_BACK`: Move backward a set number of spaces.
        *   [x] `PAY_REPAIRS`: Pay for repairs based on the number of houses and hotels owned.
        *   [x] `PAY_EACH_PLAYER`: Pay a certain amount to every other player.
        *   [x] `RECEIVE_FROM_EACH_PLAYER`: Collect a certain amount from every other player.

### **Step 3: Develop the Auction System**

This step introduces the critical auction mechanic for when a player declines to buy an unowned property.

*   **Tasks:**
    1.  **Game Logic (`game_manager.py`):** Create a new game state for auctions. Implement logic to manage bidding between players, track the current high bid, and handle the sale to the winner.
    2.  **UI (`ui_manager.py`):** Design and implement a dedicated auction dialog. This UI should display the property being auctioned, the current high bid, and provide buttons for active players to place a new bid or drop out of the auction.

*   **Features Completed After This Step:**
    *   `feature-checklist.md`:
        *   [x] If the player declines to buy, the property is immediately auctioned by the Bank to the highest bidder.
    *   `ui-feature-checklist.md`:
        *   [x] **Auction:** A dedicated UI for players to bid on a property, showing the current bid and allowing players to increase their bid or drop out.

### **Step 4: Enhance Property Management**

This step improves the existing property management screen with better rule enforcement and user feedback.

*   **Tasks:**
    1.  **Game Logic (`game_manager.py`):** Add logic to handle selling buildings back to the bank.
    2.  **UI (`ui_manager.py`):**
        *   Add "Sell House/Hotel" buttons to the management screen.
        *   Implement logic to enable/disable the "Build" and "Sell" buttons to enforce the "build evenly" rule.
        *   Display the cost to build/unmortgage or the money returned from selling/mortgaging next to the action buttons.

*   **Features Completed After This Step:**
    *   `ui-feature-checklist.md`:
        *   [x] Provide options to sell houses/hotels back to the Bank.
        *   [x] The UI should enforce the "build evenly" rule by disabling build buttons on properties that would violate the rule.
        *   [x] The UI should clearly show the cost to build or the return from selling/mortgaging.

### **Step 5: Implement Complex Property Transfers**

This step adds logic for less common but important rules regarding mortgaged properties and building shortages.

*   **Tasks:**
    1.  **Mortgage Transfers:** In `game_manager.py`, update the bankruptcy and trading logic to handle the transfer of mortgaged properties, forcing the new owner to either pay 10% interest immediately or unmortgage the property fully.
    2.  **Building Shortage:** In `game_manager.py`, add logic to initiate an auction if multiple players want to buy the last available house or hotel from the Bank.

*   **Features Completed After This Step:**
    *   `feature-checklist.md`:
        *   [x] If multiple players wish to buy the last remaining building(s), they are auctioned to the highest bidder.
        *   [x] **Transfer of Mortgaged Property:** When a player receives a mortgaged property... they must immediately choose to either unmortgage it... or keep the mortgage...

### **Step 6: Develop the Trading System**

This is a major feature that allows for player-to-player negotiation.

*   **Tasks:**
    1.  **Game Logic (`game_manager.py`):** Refine the existing `process_trade_request` to be more robust and handle various asset types (money, properties, get-out-of-jail-free cards).
    2.  **UI (`ui_manager.py`):** Design and implement a comprehensive trading screen. This UI should allow a player to select another player to trade with, add/remove assets from both sides of the offer, and then send the proposal. The receiving player should see a dialog to accept or reject the trade.

*   **Features Completed After This Step:**
    *   `feature-checklist.md`:
        *   [x] Players can trade or sell unimproved properties to each other for any agreed-upon price or asset combination.
    *   `ui-feature-checklist.md`:
        *   [x] **Trade:** A dedicated UI for players to propose and accept trades...

### **Step 7: Final UI/UX Polish**

This final step adds smaller features that enhance game clarity and user experience.

*   **Tasks:**
    1.  **UI (`ui_manager.py`):**
        *   Implement a system to draw small colored markers or icons on board spaces to indicate property ownership.
        *   Add a section to the player HUD that lists the properties owned by each player.
        *   Add a "New Game" option to the Game Over screen.
        *   Implement keyboard shortcuts for common actions.

*   **Features Completed After This Step:**
    *   `ui-feature-checklist.md`:
        *   [x] Visually indicate property ownership on the board itself.
        *   [x] Display a list of properties owned by each player in the HUD.
        *   [x] Implement keyboard shortcuts for common actions.
        *   [x] Provide an option to start a new game.
