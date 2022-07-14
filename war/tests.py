import unittest
from sys import path as pythonpath
pythonpath.append('../')
from common.cards import Card, CardCollection
from war.player import WarPlayer

class TestObjects(unittest.TestCase):

    def test_valid_WarPlayer_1(self):
        # Verifies that we can construct a WarPlayer without issues
        player = WarPlayer()

    def test_valid_WarPlayer_2(self):
        # Verifies that we can construct a WarPlayer and add some cards
        # to its deck
        player = WarPlayer()

        deck = CardCollection()
        deck.new_deck()

        player.deck.add_cardcollection(deck)

    def test_WarPlayer_flip_1(self):
        # Verifies that we can flip the top card of the deck and we get
        # expected results
        player = WarPlayer()

        deck = CardCollection()
        deck.new_deck()

        player.deck.add_cardcollection(deck)
        player.flip()
        flipped = player.active.peek()
        card = Card(rank="2", suit="Hearts")

        self.assertEqual(card.rank, flipped.rank)
        self.assertEqual(card.suit, flipped.suit)
        self.assertEqual(card.index, flipped.index)
        self.assertEqual(player.deck.get_length(), 51)

    def test_WarPlayer_flip_2(self):
        # Verifies that we can flip the top card of the deck twice and
        # we get expected results
        player = WarPlayer()

        deck = CardCollection()
        deck.new_deck()

        player.deck.add_cardcollection(deck)
        player.flip()
        player.flip()
        flipped = player.active.peek()
        card = Card(rank="2", suit="Spades")

        self.assertEqual(card.rank, flipped.rank)
        self.assertEqual(card.suit, flipped.suit)
        self.assertEqual(card.index, flipped.index)
        self.assertEqual(player.deck.get_length(), 50)

    def test_WarPlayer_peek_active_1(self):
        # Verifies that the peek_active() method provides expected behavior
        # after flipping one card
        player = WarPlayer()

        deck = CardCollection()
        deck.new_deck()

        player.deck.add_cardcollection(deck)
        player.flip()
        flipped = player.peek_active()
        card = Card(rank="2", suit="Hearts")

        self.assertEqual(card.rank, flipped.rank)
        self.assertEqual(card.suit, flipped.suit)
        self.assertEqual(card.index, flipped.index)
        self.assertEqual(player.deck.get_length(), 51)

    def test_WarPlayer_peek_active_2(self):
        # Verifies that the peek_active() method provides expected behavior
        # after flipping one card
        player = WarPlayer()

        deck = CardCollection()
        deck.new_deck()

        player.deck.add_cardcollection(deck)
        player.flip()
        player.flip()
        flipped = player.peek_active()
        card = Card(rank="2", suit="Spades")

        self.assertEqual(card.rank, flipped.rank)
        self.assertEqual(card.suit, flipped.suit)
        self.assertEqual(card.index, flipped.index)
        self.assertEqual(player.deck.get_length(), 50)

    def test_WarPlayer_empty_1(self):
        # Verifies that the empty() method provides expected behavior
        player = WarPlayer()

        deck = CardCollection()
        deck.new_deck()

        player.deck.add_cardcollection(deck)
        self.assertEqual(player.deck.get_length(), 52)

        emptied = player.empty(collection_name="deck")
        self.assertEqual(player.deck.get_length(), 0)
        self.assertEqual(emptied.get_length(), 52)

    def test_WarPlayer_reshuffle_1(self):
        # Verifies that the reshuffle() method provides expected behavior,
        # Bringing the (shuffled) discard pile into the deck
        player = WarPlayer()

        deck = CardCollection()
        deck.new_deck()

        player.discard.add_cardcollection(deck)
        self.assertEqual(player.deck.get_length(), 0)
        self.assertEqual(player.discard.get_length(), 52)

        player.reshuffle()
        self.assertEqual(player.deck.get_length(), 52)
        self.assertEqual(player.discard.get_length(), 0)

    def test_WarPlayer_reshuffle_2(self):
        # Verifies that the player will reshuffle their discard pile into
        # their deck if the former is not empty and the latter is empty
        # after a call to flip()
        player = WarPlayer()

        deck = CardCollection()
        deck.new_deck()

        player.discard.add_cardcollection(deck)
        self.assertEqual(player.deck.get_length(), 0)
        self.assertEqual(player.discard.get_length(), 52)
        self.assertEqual(player.active.get_length(), 0)

        player.flip()
        self.assertEqual(player.deck.get_length(), 51)
        self.assertEqual(player.discard.get_length(), 0)
        self.assertEqual(player.active.get_length(), 1)

    def test_WarPlayer_getcontrolled_1(self):
        # Verifies that the getcontrolled() method returns the correct
        # number of cards in play when only the deck has a nonzero number
        # of cards
        player = WarPlayer()

        deck = CardCollection()
        deck.new_deck()

        player.deck.add_cardcollection(deck)
        self.assertEqual(player.get_controlled(), 52)

    def test_WarPlayer_getcontrolled_2(self):
        # Verifies that the getcontrolled() method returns the correct
        # number of cards in play when only the discard has a nonzero number
        # of cards
        player = WarPlayer()

        deck = CardCollection()
        deck.new_deck()

        player.discard.add_cardcollection(deck)
        self.assertEqual(player.get_controlled(), 52)

    def test_WarPlayer_getcontrolled_3(self):
        # Verifies that getcontrolled() method returns the correct
        # number of cards in play when deck and discard both have
        # a nonzero number of cards, but there are no active cards
        player = WarPlayer()

        deck = CardCollection()
        deck.new_deck()
        d1, d2, d3 = deck.split(num_split=3)
        # These should have 18, 17, and 17 cards respectively

        player.deck.add_cardcollection(d1)
        player.discard.add_cardcollection(d2)
        self.assertEqual(player.get_controlled(), 35)

    def test_WarPlayer_getcontrolled_3(self):
        # Verifies that getcontrolled() method returns the correct
        # number of cards in play when deck, discard, and active all have
        # a nonzero number of cards
        player = WarPlayer()

        deck = CardCollection()
        deck.new_deck()
        d1, d2, d3 = deck.split(num_split=3)
        # These should have 18, 17, and 17 cards respectively

        player.deck.add_cardcollection(d1)
        player.discard.add_cardcollection(d2)
        player.active.add_cardcollection(d3)
        self.assertEqual(player.get_controlled(), 35)

    def test_WarPlayer_getcontrolled_4(self):
        # Verifies that getcontrolled() method returns the correct
        # number of cards in play after calling flip()
        player = WarPlayer()

        deck = CardCollection()
        deck.new_deck()
        d1, d2, d3 = deck.split(num_split=3)
        # These should have 18, 17, and 17 cards respectively

        player.deck.add_cardcollection(d1)
        player.discard.add_cardcollection(d2)
        player.active.add_cardcollection(d3)
        player.flip()

        self.assertEqual(player.get_controlled(), 34)

if __name__ == "__main__":
    unittest.main()