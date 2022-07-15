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

## Necessary imports
from sys import path as pythonpath
pythonpath.append('../')
from common.cards import Card, CardCollection
from war.player import WarPlayer

## Initialize a new deck and new players
deck = CardCollection()
deck.new_deck()
deck.shuffle()
playerA = WarPlayer()
playerB = WarPlayer()

## Split the deck between the playesr
deckA, deckB = deck.split(num_split=2)
playerA.deck.add_cardcollection(deckA)
playerB.deck.add_cardcollection(deckB)

# Avoid confusion later - we're done with these
del deckA, deckB

# Basic stats
num_turns = 0

# Gameplay loop
while playerA.get_controlled() not in [0,52]:
    # TODO - This does *not* verify that both players have some cards they can
    # flip. It simply shows that the total number of cards in one players active
    # and discard piles is not 52 - it's perfectly possible for there to be
    # cards still in both players' active areas.  I'm honestly not sure how to
    # resolve this right now in terms of game rules, but we could perform a
    # check on logic here for if either players deck and discard are both empty,
    # perhaps comparing the active card (including "face down") cards in
    # that case

    # Flip cards face-up
    playerA.flip()
    playerB.flip()

    # Check to see if either player has won
    if playerA.peek_active() > playerB.peek_active():
        # Add both players' active areas to playerA's discard pile
        # and empty both players' active areas
        playerA.discard.add_cardcollection(playerA.empty("active"))
        playerA.discard.add_cardcollection(playerB.empty("active"))

    elif playerB.peek_active() > playerA.peek_active():
        # Add both players' active areas to playerB's discard pile
        # and empty both players' active areas
        playerB.discard.add_cardcollection(playerA.empty("active"))
        playerB.discard.add_cardcollection(playerB.empty("active"))

    else:
        # The rank of both cards is equal - flip another card "face down" (it
        # identity will never be referenced, but can be moved between decks)
        playerA.flip()
        playerB.flip()

    num_turns += 1

# Basic checks
assert playerA.active.get_length() == 0
assert playerB.active.get_length() == 0
assert playerA.get_controlled() != playerB.get_controlled()
assert (playerA.get_controlled() + playerB.get_controlled()) == 52
print(num_turns)