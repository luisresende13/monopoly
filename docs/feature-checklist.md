# Monopoly Feature Implementation Checklist

This document outlines all the features required for a complete and faithful implementation of the classic Monopoly game. The checkboxes indicate the current implementation status based on the source code.

---

### **1. Game Setup & Initialization**

- [x] Create a game board with 40 spaces as per the standard layout.
- [x] Create and shuffle separate Chance and Community Chest card decks.
- [x] Initialize the Bank with the correct number of houses (32) and hotels (12).
- [x] The Bank correctly manages money and property deeds.
- [x] Create 2-8 players, each with a unique token.
- [x] Distribute the correct starting money ($1,500) to each player.
- [x] Determine the starting player by having each player roll the dice; the highest roll goes first.
- [ ] Handle ties in the initial dice roll by having the tied players re-roll.

### **2. Core Gameplay Loop**

- [x] Player turn proceeds in a clockwise order.
- [x] Player rolls two six-sided dice to determine their move.
- [x] Player's token moves the exact number of spaces shown on the dice.
- [x] Player collects a $200 salary from the Bank each time they land on or pass over GO.
- [x] If a player rolls doubles, they take another turn after completing their first one.
- [x] If a player rolls doubles three times in a row, they go directly to Jail and their turn ends.
- [ ] The game correctly identifies the last remaining player as the winner.

### **3. Actions on Board Spaces**

#### **3.1. Properties (Streets, Railroads, Utilities)**
- [x] **Landing on Unowned Property:**
    - [x] Player has the option to buy the property at its listed price.
    - [ ] If the player declines to buy, the property is immediately auctioned by the Bank to the highest bidder. (Current implementation is simplified and not a true auction).
- [x] **Landing on Owned Property:**
    - [x] If the property is unmortgaged, the player must pay the owner the correct rent.
    - [x] No rent is collected on mortgaged properties.
    - [x] **Street Rent:**
        - [x] Rent is based on the number of houses/hotels on the property.
        - [x] Rent is doubled on unimproved properties if the owner has a monopoly on that color group.
    - [x] **Railroad Rent:**
        - [x] Rent is calculated based on the total number of railroads owned by the player ($25, $50, $100, $200).
    - [x] **Utility Rent:**
        - [x] If one utility is owned, rent is 4 times the value of the dice roll.
        - [x] If both utilities are owned, rent is 10 times the value of the dice roll.

#### **3.2. Chance & Community Chest Spaces**
- [x] Player draws the top card from the correct deck.
- [x] The card is returned to the bottom of the deck after its action is completed.
- [x] **Card Actions Implemented:**
    - [x] `MOVE_TO_SPACE`: Move to a specific space (e.g., "Advance to Go").
    - [x] `RECEIVE_FROM_BANK`: Collect money from the Bank.
    - [x] `PAY_BANK`: Pay money to the Bank.
    - [x] `GO_TO_JAIL`: Go directly to Jail.
    - [x] `ADD_GET_OUT_OF_JAIL_FREE_CARD`: Player receives and can hold this card.
- [ ] **Card Actions Not Implemented:**
    - [ ] `MOVE_TO_NEAREST`: Move to the nearest Utility or Railroad.
    - [ ] `MOVE_BACK`: Move backward a set number of spaces.
    - [ ] `PAY_REPAIRS`: Pay for repairs based on the number of houses and hotels owned.
    - [ ] `PAY_EACH_PLAYER`: Pay a certain amount to every other player.
    - [ ] `RECEIVE_FROM_EACH_PLAYER`: Collect a certain amount from every other player.

#### **3.3. Tax Spaces**
- [x] **Luxury Tax:** Player pays a flat fee of $75 to the Bank.
- [x] **Income Tax:** Player has the choice to pay a flat $200 or 10% of their total worth.
- [x] Player's total worth is correctly calculated (cash + property prices + building costs).

#### **3.4. Corner Spaces**
- [x] **GO:** Salary is collected when landing on or passing.
- [x] **Jail (Just Visiting):** No penalty for landing on the space.
- [x] **Free Parking:** The space has no special action; it is a "free rest" space.
- [x] **Go To Jail:** Player is sent directly to the "In Jail" section of the board, does not pass GO, and does not collect $200.

### **4. Jail Rules**

- [x] A player is sent to Jail for rolling three consecutive doubles, landing on "Go To Jail", or drawing a "Go To Jail" card.
- [ ] While in Jail, a player can perform all normal actions (collect rent, build, trade, etc.). (Current implementation does not allow this).
- [x] **Getting Out of Jail:**
    - [x] Use a "Get Out of Jail Free" card.
    - [x] Attempt to roll doubles on one of their next three turns. If successful, they move immediately.
    - [ ] Player has the option to pay a $50 fine on their turn to get out. (Currently, payment is only forced after 3 failed rolls).
    - [x] If a player fails to roll doubles after three turns, they must pay the $50 fine and then move according to their roll.

### **5. Buildings (Houses & Hotels)**

- [x] A player must own a full, unmortgaged color-group monopoly to build.
- [x] Houses must be built evenly across all properties in a color group.
- [x] A hotel can be bought only after four houses have been built on every property in a color group.
- [x] Buying a hotel returns the four houses on that property to the Bank.
- [x] **Building Shortage:**
    - [x] Players cannot build if the Bank has run out of houses or hotels.
    - [ ] If multiple players wish to buy the last remaining building(s), they are auctioned to the highest bidder.

### **6. Mortgages**

- [x] Only unimproved properties can be mortgaged. All buildings in a color group must be sold first.
- [x] Player receives the mortgage value from the Bank when mortgaging a property.
- [x] To unmortgage, the player must pay the mortgage value plus 10% interest to the Bank.
- [ ] **Transfer of Mortgaged Property:**
    - [ ] When a player receives a mortgaged property via trade or bankruptcy, they must immediately choose to either unmortgage it (paying value + 10% interest) or keep the mortgage (paying only the 10% interest fee at the time of transfer).

### **7. Trading & Private Sales**

- [ ] Players can trade or sell unimproved properties to each other for any agreed-upon price or asset combination. (A trade function exists but there is no UI to facilitate it).
- [x] A property cannot be traded if any property in its color group has buildings on it.

### **8. Bankruptcy**

- [x] A player is bankrupt if they owe more than they can pay after selling all buildings and mortgaging all properties.
- [x] **Debt to another player:** The bankrupt player gives all their assets (money, properties, cards) to the creditor.
- [x] **Debt to the Bank:** The Bank receives all assets and auctions off the properties to the remaining players.
