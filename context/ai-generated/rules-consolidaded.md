This is a complete and consolidated set of rules for the classic Monopoly game, created by synthesizing rules documents and resolving all identified discrepancies.

This document is designed to be a definitive and unambiguous guide for developing a Monopoly computer game.

---

### **The Complete and Consolidated Rules of Monopoly**

#### **1. Object of the Game**

To become the wealthiest player by buying, renting, and selling property, ultimately forcing all other players into bankruptcy. The last player remaining in the game is the winner.

#### **2. Game Equipment**

*   1 Gameboard
*   2 Dice
*   Player Tokens
*   28 Title Deed Cards (one for each property)
*   16 Chance Cards
*   16 Community Chest Cards
*   32 Houses
*   12 Hotels
*   Monopoly Money

#### **3. Game Setup**

1.  **Board and Cards:** Place the gameboard on a flat surface. Shuffle the Chance and Community Chest card decks separately and place them face-down on their designated spaces on the board.
2.  **The Banker:** Select one player to be the Banker. The Banker is in charge of the Bank's assets.
    *   If the Banker is also a player, they must keep their personal funds and property strictly separate from the Bank's.
    *   If there are more than five players, the Banker may choose to act only as Banker and Auctioneer.
3.  **The Bank:** The Bank holds all Title Deed cards, houses, and hotels before they are purchased. The Bank:
    *   Pays salaries and bonuses.
    *   Sells and auctions properties, distributing the correct Title Deed cards.
    *   Sells houses and hotels.
    *   Loans money via mortgages on properties.
    *   Collects all taxes, fines, interest, and the price of properties sold.
    *   **The Bank never goes bankrupt.** If the Bank runs out of money, the Banker may issue as much as needed by writing on ordinary paper (or, for a computer game, by creating more money).
4.  **Player Preparation:**
    *   Each player chooses a token and places it on the "GO" space.
    *   The Banker distributes **$1,500** to each player in the following denominations:
        *   Two $500 bills
        *   Two $100 bills
        *   Two $50 bills
        *   Six $20 bills
        *   Five $10 bills
        *   Five $5 bills
        *   Five $1 bills
5.  **Starting the Game:** Each player rolls both dice. The player with the highest total roll takes the first turn. Play proceeds clockwise.

#### **4. The Gameplay Loop (A Player's Turn)**

1.  **Roll the Dice:** Roll both dice and move your token clockwise the number of spaces indicated by the total.
2.  **Action on Landing:** Perform the action corresponding to the space you land on (see Section 5). Multiple tokens may rest on the same space.
3.  **Passing GO:** Each time your token lands on or passes over the "GO" space, the Bank pays you a **$200 salary**. This salary is paid only once per trip around the board.
    *   *Exception:* If a card sends you to a space and you pass GO, you collect $200. However, if you are sent directly to Jail, you do not pass GO and do not collect a salary.
4.  **Rolling Doubles:**
    *   If you roll doubles, you move and take your action as usual, then you get to roll again and take an additional turn.
    *   If you roll doubles a second consecutive time, you take a second additional turn.
    *   If you roll doubles a third consecutive time, you are "caught speeding." Do not move your token. You must **go directly to Jail**, and your turn ends.
5.  **Ending Your Turn:** After you have completed your move and action, pass the dice to the player on your left.

#### **5. Actions on Spaces**

##### **5.1 Unowned Properties (Streets, Railroads, Utilities)**
When you land on an unowned property, you have two choices:
1.  **Buy the Property:** You may buy the property from the Bank for its printed price. Pay the Bank and receive the corresponding Title Deed card, which you place face-up in front of you.
2.  **Decline to Buy:** If you choose not to buy the property, the Banker must **immediately hold an auction** for it.
    *   Bidding may start at any price offered by any player.
    *   Any player, including the one who originally declined to buy, may bid.
    *   The property is sold to the highest bidder.
    *   If no player bids on the property, it remains unowned, and the Title Deed stays with the Bank.

##### **5.2 Owned Properties**
When you land on a property owned by another player, you must pay them rent.
*   **Rent Collection:** The owner must ask you for rent **before the next player in turn rolls the dice**. If they fail to do so, you do not have to pay.
*   **Standard Rent:** The rent amount is listed on the property's Title Deed.
*   **Monopoly Rent (Streets):** If a player owns all the streets in a single color-group (a monopoly), the rent is **doubled** on all unimproved streets in that group. This double rent can be collected even if other properties in that group are mortgaged.
*   **Railroad Rent:** Rent depends on the number of Railroads the owner possesses:
    *   1 Railroad: $25
    *   2 Railroads: $50
    *   3 Railroads: $100
    *   4 Railroads: $200
*   **Utility Rent:** Rent is based on the dice roll that brought you to the space.
    *   If the owner has one Utility, the rent is **4 times** the dice roll.
    *   If the owner has both Utilities, the rent is **10 times** the dice roll.
*   **Mortgaged Property:** No rent can be collected on a mortgaged property. The Title Deed card for a mortgaged property is placed face-down.

##### **5.3 Chance and Community Chest**
Draw the top card from the indicated deck, follow its instructions immediately, and then return the card to the bottom of the deck.
*   **Get Out of Jail Free Card:** If you draw this card, you may keep it until you need to use it or sell it to another player for a mutually agreed price.

##### **5.4 Tax Spaces**
*   **Income Tax:** You must choose one of two options:
    1.  Pay a flat **$200** to the Bank.
    2.  Pay **10% of your total worth** to the Bank. Your worth is calculated as: cash on hand + printed prices of all unmortgaged properties + mortgage value of all mortgaged properties + purchase price of all buildings.
    *   You must declare your choice *before* you calculate your total worth.
*   **Luxury Tax:** Pay the flat amount of **$75** to the Bank.

##### **5.5 Corner Spaces**
*   **GO:** Collect a $200 salary when you land on or pass over this space.
*   **Jail (Just Visiting):** If you land on this space during a normal move, you are "Just Visiting." There is no penalty, and you move as usual on your next turn.
*   **Free Parking:** This is a "free" resting space. Nothing happens. You do not receive any money, property, or reward of any kind.
*   **Go to Jail:** You must move your token directly to the "In Jail" section of the Jail space. Your turn ends immediately. You do not pass GO and do not collect a $200 salary.

#### **6. Jail**

##### **6.1 How to Go to Jail**
You are sent to Jail if:
1.  You land on the "Go to Jail" space.
2.  You draw a Chance or Community Chest card that says "Go to Jail."
3.  You roll doubles three times in a row on your turn.

##### **6.2 While in Jail**
You cannot move your token. However, you **can** still collect rent, buy and sell buildings, mortgage properties, and trade with other players.

##### **6.3 How to Get Out of Jail**
You have three options:
1.  **Pay the Fine:** Pay a **$50 fine** to the Bank before you roll the dice on your turn. You are then out of Jail and can roll and move as normal.
2.  **Use a Card:** Use a "Get Out of Jail Free" card (or buy one from another player). Place the card at the bottom of the appropriate deck, then roll and move.
3.  **Roll Doubles:** On any of your next three turns, you may try to roll doubles.
    *   If you succeed, you are immediately out of Jail. Use that roll to move your token. You do **not** get to roll again for rolling doubles on this turn.
    *   If you fail to roll doubles by your third turn in Jail, you **must pay the $50 fine** to the Bank. You then move your token the number of spaces shown on that third roll.

#### **7. Buildings (Houses and Hotels)**

*   **Requirement:** To build, you must own an entire color-group (a monopoly), and none of the properties in that group can be mortgaged.
*   **Buying Houses:** You may buy houses from the Bank at any time for the price listed on the Title Deed.
*   **Building Evenly:** You must build evenly. You cannot build a second house on any street until you have built one house on every street in that color-group. This rule applies up to four houses per street.
*   **Buying Hotels:** Once you have four houses on every street of a complete color-group, you may buy a hotel. You pay the hotel price listed on the Title Deed and return the four houses from that street to the Bank. Only one hotel may be built per street.
*   **Building Shortage:** If the Bank runs out of houses or hotels, no player can build until some are returned to the Bank. If multiple players want to buy the last available building(s), the Banker must auction them to the highest bidder.

#### **8. Selling and Trading**

*   **Selling Buildings:** Buildings (houses and hotels) can be sold back to the Bank at any time for **half their purchase price**.
    *   Houses must be sold evenly, in the reverse manner they were bought.
    *   Selling a hotel immediately returns four houses to the property and gives you cash equal to half the hotel's purchase price.
*   **Trading Unimproved Properties:** You may sell any unimproved street, railroad, or utility to another player in a private transaction for any agreed-upon price or trade.
*   **Trading Improved Properties:** You cannot sell or trade a street to another player if there are any buildings on any street in its color-group. You must first sell all buildings in that group back to the Bank.

#### **9. Mortgages**

*   **Mortgaging Property:** You may mortgage any unimproved property. First, you must sell all buildings on its color-group back to the Bank. To mortgage, turn the property's Title Deed face-down and collect the mortgage value from the Bank.
*   **Effect of Mortgage:** You retain ownership, but you cannot collect rent on a mortgaged property.
*   **Unmortgaging Property:** To lift a mortgage, you must pay the Bank the mortgage value plus **10% interest**.
*   **Transfer of Mortgaged Property:** A mortgaged property can be sold or traded to another player at any agreed price. The new owner must immediately choose one of two options:
    1.  **Unmortgage Immediately:** Pay the Bank the full mortgage value plus the 10% interest.
    2.  **Keep the Mortgage:** Pay the Bank a **10% interest fee** immediately. If they choose to unmortgage the property on a later turn, they must pay the mortgage value plus an **additional 10% interest fee**.

#### **10. Bankruptcy**

You are bankrupt if you owe more than you can pay to either another player or the Bank.
*   **Debt to Another Player:** You must turn over all of your assets to that player.
    *   Sell any buildings back to the Bank for half price and give the cash to the creditor.
    *   Give the creditor all your cash, Title Deeds, and any "Get Out of Jail Free" cards.
    *   For any mortgaged properties transferred, the new owner must immediately follow the rules in Section 9 (pay 10% interest now or unmortgage fully).
    *   You are out of the game.
*   **Debt to the Bank:** You must turn over all your assets to the Bank.
    *   The Bank auctions off all properties received (except buildings). Mortgages on these properties are cancelled before the auction.
    *   Any "Get Out of Jail Free" cards are returned to the bottom of their decks.
    *   You are out of the game.