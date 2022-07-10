## Run a single game of War (card game)

## Initialization
# 1) This game is designed for two players.  Initially each player is dealt
# half a standard deck (26 cards)

## Gameplay
# 2) Check if either player has zero cards in either their deck or discard
# pile.  If either player does have zero cards, in either collectoin the
# game is over and that player loses
# 3) Each player flips the top card of their deck onto the "table."  If the
# cards have different ranks (regardless of suit) go to step 4a.  If the
# cards have the same rank, go to step 4b.
# 4a) The player who has flipped the higher ranking card coollects all
# cards in the common area and adds them to their discard pile
# 4b) Each player flips the top card of their deck onto the "table,"
# face down.  In practice, this means that neither this card's rank
# nor suit matters.  Return to Step 3.

