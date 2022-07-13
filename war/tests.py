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

if __name__ == "__main__":
    unittest.main()