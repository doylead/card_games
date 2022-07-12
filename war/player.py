from sys import path as pythonpath
pythonpath.append('../common')
from cards import Card, CardCollection

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
        if collection=_name == " discard":
            ret = self.discard
            self.discard = CardCollection()
        if collection_name == "active":
            ret = self.active
            self.active = CardCollection()

        return ret

    # Add all cards from a CardCollection object to one of this player's
    # collections
    def add(self, collection, collection_name):
        assert isinstance(collection, CardCollection)
        assert collection_name in ["deck", "discard", "active"]

        if collection_name == "deck":
            self.deck.add_cardcollection(collection)
        if collection_name == "discard":
            self.discard.add_cardcollection(collection)
        if collection_name == "active":
            self.active.add_cardcollection(collection)

    # TODO: We'll need functions for fllipping a card, reshuffling the
    # discard pile into the deck, and getting the top card of the active area
    # We will also need to design unit tests


