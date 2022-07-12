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
pythonpath.append('../common')
from cards import Card, CardCollection

## Initialize a new deck
deck = CardCollection()
deck.new_deck()
deck.shuffle()

## Instantiate the CardCollection objects
# TODO the link between a player's deck and discard pile is not easily shown.
# TODO should we add a new type of object that combines the two?
playerA_deck, playerB_deck = deck.split(num_split=2)
playerA_discard = CardCollection()
playerB_discard = CardCollection()
playerA_active = CardCollection()
playerB_active = CardCollection()

# Gameplay loop
while playerA.get_length() not in [0,52]:
    # Flip cards face-up
    playerA_active.add_card(playerA_deck.deal())
    playerB_active.add_card(playerB_deck.deal())

    # Check to see if either player has won
    if playerA_active.peek() > playerB_active.peek():
        pass # TODO Should a CardCollection have an add_cards method?
    elif playerB_active.peek() > playerB_active.peek():
        pass # TODO Parallel above
    else:
        # The rank of both cards is equal
        # TODO Add additional cards to the active area
