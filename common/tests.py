import unittest
from cards import Card, CardCollection

class TestObjects(unittest.TestCase):

    def test_valid_Card_1(self):
        # Create a 7 of hearts and check its properties
        card = Card(rank="7", suit="hearts")
        self.assertEqual(card.rank, "7")
        self.assertEqual(card.suit, "Hearts")
        self.assertEqual(card.index, 7)
        self.assertEqual(str(card), "7 of Hearts")

    def test_valid_Card_2(self):
        # Like test_valid_card_1, but supplies rank as integer
        card = Card(rank=7, suit="Hearts")
        self.assertEqual(card.rank, "7")
        self.assertEqual(card.suit, "Hearts")
        self.assertEqual(card.index, 7)
        self.assertEqual(str(card), "7 of Hearts")

    def test_valid_Card_3(self):
        # Create a Queen of diamonds and check its properties
        card = Card(rank="QUEEN", suit="DIAMONDS")
        self.assertEqual(card.rank, "Queen")
        self.assertEqual(card.suit, "Diamonds")
        self.assertEqual(card.index, 12)
        self.assertEqual(str(card), "Queen of Diamonds")

    def test_invalid_Card_1(self):
        # Create a card with an invalid rank (1 of clubs)
        rank = "1"
        suit = "clubs"
        try:
            card = Card(rank=rank, suit=suit)
        except AssertionError:
            pass
        else:
            self.fail("Allowed to create card with rank {rank}".format(rank=rank))

    def test_invalid_Card_2(self):
        # Create a card with an invalid rank (12 of spades)
        rank = "12"
        suit = "SPADES"
        try:
            card = Card(rank=rank, suit=suit)
        except AssertionError:
            pass
        else:
            self.fail("Allowed to create card with rank {rank}".format(rank=rank))

    def test_invalid_Card_3(self):
        # Create a card with an invalid suit (8 of clovers)
        rank = "8"
        suit = "clovers"
        try:
            card = Card(rank=rank, suit=suit)
        except AssertionError:
            pass
        else:
            self.fail("Allowed to create with suit {suit}".format(suit=suit))

    def test_Card_comparison_1(self):
        # Tests that a nine of hearts is greater than a four of diamonds
        card_0 = Card(rank="9", suit="hearts")
        card_1 = Card(rank="4", suit="Diamonds")
        self.assertTrue(card_0 > card_1)
        self.assertTrue(card_1 < card_0)

    def test_Card_comparison_2(self):
        # Tests that a king of spades is greater than a 10 of hearts
        card_0 = Card(rank="king", suit="SPADES")
        card_1 = Card(rank="10", suit="Hearts")
        self.assertTrue(card_0 > card_1)
        self.assertTrue(card_1 < card_0)

    def test_Card_comparison_3(self):
        # Tests that we get NotImplementedError when using the equals operator
        card_0 = Card(rank="5", suit="clubs")
        card_1 = Card(rank="5", suit="diamonds")
        try:
            truthiness = (card_0 == card_1)
        except NotImplementedError:
            pass
        else:
            self.fail("Allowed to compare equality of two cards")

    def test_Card_comparison_4(self):
        # Tests that we get NotImplementedError when using >=
        card_0 = Card(rank="6", suit="spades")
        card_1 = Card(rank=3, suit="hearts")
        try:
            truthiness = (card_0 >= card_1)
        except NotImplementedError:
            pass
        else:
            self.fail("Allowed to use >= comparing two cards")

    def test_Card_comparison_5(self):
        # Tests that we get NotImplementedError when using <=
        card_0 = Card(rank=2, suit="clubs")
        card_1 = Card(rank=8, suit="diamonds")
        try:
            truthiness = (card_0 <= card_1)
        except NotImplementedError:
            pass
        else:
            self.fail("Allowed to use <= comparing two cards")

    def test_valid_CardCollection_1(self):
        # Tests that we can create an "empty" CardCollection
        collection = CardCollection()
        self.assertEqual(len(collection.collection), 0)

    def test_valid_CardCollection_2(self):
        # Tests that we can create a CardCollection with one card,
        # and that the CardCollection behaves as expected
        card = Card(rank="Queen", suit="Hearts")
        collection = CardCollection([card])
        dealt = collection.deal()
        self.assertEqual(card.rank, dealt.rank)
        self.assertEqual(card.suit, dealt.suit)
        self.assertEqual(card.index, dealt.index)
        self.assertEqual(len(collection.collection), 0)

    def test_valid_CardCollection_3(self):
        # Tests that we can create a CardCollection with one card
        # (using a slightly different construction method),
        # and that the CardCollection behaves as expected
        card = Card(rank="Queen", suit="Hearts")
        collection = CardCollection()
        collection.add_card(card)
        dealt = collection.deal()
        self.assertEqual(card.rank, dealt.rank)
        self.assertEqual(card.suit, dealt.suit)
        self.assertEqual(card.index, dealt.index)
        self.assertEqual(len(collection.collection), 0)

    def test_valid_CardCollection_3(self):
        # Tests that we can create a CardCollection with one card
        # (using a slightly different construction method),
        # and that the CardCollection behaves as expected
        card = Card(rank="Queen", suit="Hearts")
        collection = CardCollection(card)
        dealt = collection.deal()
        self.assertEqual(card.rank, dealt.rank)
        self.assertEqual(card.suit, dealt.suit)
        self.assertEqual(card.index, dealt.index)
        self.assertEqual(len(collection.collection), 0)

    def test_valid_CardCollection_4(self):
        # Test creating a CardCollection with multiple cards as in
        # test_validCardCollection_2
        card0 = Card(rank="Jack", suit="Spades")
        card1 = Card(rank="4", suit="Clubs")
        card2 = Card(rank="Ace", suit="Diamonds")
        card3 = Card(rank="2", suit="Hearts")
        card4 = Card(rank="10", suit="Hearts")

        collection = CardCollection([card0, card1, card2, card3, card4])
        dealt = collection.deal(num_cards=5)
        # Check the rank of each card
        self.assertEqual(card0.rank, dealt[0].rank)
        self.assertEqual(card1.rank, dealt[1].rank)
        self.assertEqual(card2.rank, dealt[2].rank)
        self.assertEqual(card3.rank, dealt[3].rank)
        self.assertEqual(card4.rank, dealt[4].rank)

        # Check the suit of each card
        self.assertEqual(card0.suit, dealt[0].suit)
        self.assertEqual(card1.suit, dealt[1].suit)
        self.assertEqual(card2.suit, dealt[2].suit)
        self.assertEqual(card3.suit, dealt[3].suit)
        self.assertEqual(card4.suit, dealt[4].suit)

        # Check the index of each card
        self.assertEqual(card0.index, dealt[0].index)
        self.assertEqual(card1.index, dealt[1].index)
        self.assertEqual(card2.index, dealt[2].index)
        self.assertEqual(card3.index, dealt[3].index)
        self.assertEqual(card4.index, dealt[4].index)

        # Check that the Collection is empty
        self.assertEqual(len(collection.collection), 0)

        pass

    def test_valid_CardCollection_5(self):
        # Test creating a CardCollection with multiple cards as in
        # test_valid_CardCollection_3
        card0 = Card(rank="Jack", suit="Spades")
        card1 = Card(rank="4", suit="Clubs")
        card2 = Card(rank="Ace", suit="Diamonds")
        card3 = Card(rank="2", suit="Hearts")
        card4 = Card(rank="10", suit="Hearts")

        collection = CardCollection()
        collection.add_card(card0)
        collection.add_card(card1)
        collection.add_card(card2)
        collection.add_card(card3)
        collection.add_card(card4)
        dealt = collection.deal(num_cards=5)

        # Check the rank of each card
        self.assertEqual(card0.rank, dealt[0].rank)
        self.assertEqual(card1.rank, dealt[1].rank)
        self.assertEqual(card2.rank, dealt[2].rank)
        self.assertEqual(card3.rank, dealt[3].rank)
        self.assertEqual(card4.rank, dealt[4].rank)

        # Check the suit of each card
        self.assertEqual(card0.suit, dealt[0].suit)
        self.assertEqual(card1.suit, dealt[1].suit)
        self.assertEqual(card2.suit, dealt[2].suit)
        self.assertEqual(card3.suit, dealt[3].suit)
        self.assertEqual(card4.suit, dealt[4].suit)

        # Check the index of each card
        self.assertEqual(card0.index, dealt[0].index)
        self.assertEqual(card1.index, dealt[1].index)
        self.assertEqual(card2.index, dealt[2].index)
        self.assertEqual(card3.index, dealt[3].index)
        self.assertEqual(card4.index, dealt[4].index)

        # Check that the Collection is empty
        self.assertEqual(len(collection.collection), 0)

        pass

    def test_valid_CardCollection_6(self):
        # Tests that we can create a standard (single) deck of
        # cards with the correct number of unique cards
        collection = CardCollection()
        collection.new_deck(include_joker=False)

        # Check number of cards
        self.assertEqual(len(collection.collection), 52)

        # Check that all cards are unique
        card_names = [str(card) for card in collection.collection]
        self.assertEqual(len(collection.collection), len(set(card_names)))

    def test_valid_CardCollection_7(self):
        # Tests that we can create a CardCollection containing two
        # standard decks of cards with the correct number of unique cards
        collection = CardCollection()
        num_decks = 2
        collection.new_deck(num_decks=num_decks, include_joker=False)

        # Check number of cards
        self.assertEqual(len(collection.collection), 104)

        # Check that all cards are unique
        card_names = [str(card) for card in collection.collection]
        self.assertEqual(len(collection.collection)/num_decks, len(set(card_names)))

    def test_CardCollection_shuffle_1(self):
        # Tests that the shuffling algorithm reorders cards.
        # There is a (1/52)*(1/51)*(1/50)*(1/49) chance of this test failing
        # even in a perfectly fair shuffling algorithm, but this is
        # a low enough rate (less than one in a million) to be sufficient
        collection = CardCollection()
        collection.new_deck(include_joker=False)
        collection.shuffle()

        # Create a baseline representation of the first four cards shown in
        # a shuffled deck and count the cards in the deck
        before_rep = ""
        for i in range(4):
            before_rep += str(collection.collection[i])
        before_count = len(collection.collection)

        # Shuffle the cards once more
        collection.shuffle()

        # Create another representation of the first four cards after the
        # second shuffle
        after_rep = ""
        for i in range(4):
            after_rep += str(collection.collection[i])
        after_count = len(collection.collection)

        # If shuffling has worked, these two string representations will
        # almost always be different.  However the count of cards
        # should remain the same
        self.assertNotEqual(before_rep, after_rep)
        self.assertEqual(before_count, after_count)

    def test_CardCollection_peek_1(self):
        # Tests that the peek function works as expected
        # Decks are generated in a standard way (not shuffled), so we
        # know which card should be on top at first
        collection = CardCollection()
        collection.new_deck()
        peeked = collection.peek()
        card = Card(rank="Ace", suit="Clubs")

        self.assertEqual(card.rank, peeked.rank)
        self.assertEqual(card.suit, peeked.suit)
        self.assertEqual(card.index, peeked.index)
        self.assertEqual(len(collection.collection), 52)

    def test_CardCollection_length_1(self):
        # Tests that the get_length() function works as expected
        # after creating a standard deck and after dealing some
        # cards
        collection = CardCollection()
        collection.new_deck()

        self.assertEqual(collection.get_length(), 52)
        dealt = collection.deal(num_cards=3)
        self.assertEqual(collection.get_length(), 49)


if __name__ == "__main__":
    unittest.main()