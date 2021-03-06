from sys import path as pythonpath
pythonpath.append('../')
from common.cards import Card, CardCollection

class WarPlayer:
    # A class of objects used to representing a player in the game of war.
    # Each player has a deck, a discard pile, and an active player area.

    # At initialization each CardCollection is empty.  We'll have to
    # add cards later
    def __init__(self):
        self.deck = CardCollection()
        self.discard = CardCollection()
        self.active = CardCollection()

    # Return one of this players' CardCollections and replace it with an
    # empty CardCollection.
    def empty(self, collection_name):
        assert collection_name in ["deck", "discard", "active"]

        if collection_name == "deck":
            ret = self.deck
            self.deck = CardCollection()
        if collection_name == "discard":
            ret = self.discard
            self.discard = CardCollection()
        if collection_name == "active":
            ret = self.active
            self.active = CardCollection()

        return ret

    # Shuffle the discard pile and then add it to the deck
    def reshuffle(self):
        self.discard.shuffle()
        self.deck.add_cardcollection(self.empty(collection_name="discard"))

    # Move the top card of the deck into the active area
    def flip(self):
        # If the deck is empty, shuffle the discard pile and
        # add it to the deck
        if self.deck.get_length() == 0:
            self.reshuffle()

        # If the deck is still empty, there are no cards in deck or
        # discard pile.  This is currently undefined behavior
        if self.deck.get_length() == 0:
            raise NotImplementedError

        # Add the top card of the deck to the active CardCollection
        self.active.add_card(self.deck.deal(num_cards=1))

    # Return a copy of the top card of the active area for comparison.
    # Do not modify the active area in the process, as there may be a tie.
    def peek_active(self):
        return self.active.peek()

    # Return the number of cards in the deck and discard piles combined
    def get_controlled(self):
        return self.deck.get_length() + self.discard.get_length()