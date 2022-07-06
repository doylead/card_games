import pylab as plt
from random import shuffle

class Card:
    # A class of objects used to represent playing cards.  Currently supports
    # 2-Ace of the four standard suits (hearts, diamonds, clubs, spades).
    # Card creation expects a rank and suit.  Where applicable, rank may be an integer
    # or string.  Suit will be saved in standard capitalization, but input is not
    # case-sensitive

    def __init__(self, rank, suit):
        # Standardize formatting
        suit = str(suit).lower().capitalize()
        rank = str(rank).lower().capitalize()

        # Basic validation of input data
        assert rank in ["2", "3", "4", "5", "6", "7", "8", "9", "10",
                        "Jack", "Queen", "King", "Ace"]
        assert suit in ["Hearts", "Diamonds", "Spades", "Clubs"]

        # Convert to numerical indices for easier comparison
        index_translation = {"Jack": 11, "Queen": 12, "King": 13, "Ace": 14}
        for i in range(2,11):
            index_translation[str(i)] = i

        # Store the provided information into the Card object
        self.rank = rank
        self.suit = suit
        self.index = index_translation[rank]

    def __str__(self):
        # Return a human-readable string representing the card
        return "{rank} of {suit}".format(rank=self.rank, suit=self.suit)

    # Basic comparison operators for cards
    def __gt__(self, other):
        return self.index > other.index

    def __lt__(self, other):
        return self.index < other.index

    # Not defining __ge__, __le__, or __eq__ because I'm not sure
    # how I'd want those to interact with suits in a common way
    # across games
    def __ge__(self, other):
        raise NotImplementedError

    def __le__(self, other):
        raise NotImplementedError

    def __eq__(self, other):
        raise NotImplementedError


class CardCollection:
    # A class of objects that represent collections of cards.  Designed for
    # objects of the Card class, though it can likely be extended for other
    # types of cards if implemented.  Users may conceptualizse a "deck", a
    # "discard pile", a "hand", and a payer's "active area" as examples of
    # CardCollections

    def __init__(self, cards=[]):
        # Initially the collection is empty
        self.collection = []

        # Handle a predictable user behavior where they pass one card rather
        # than a list of length one
        if isinstance(cards, Card):
            cards = [cards]

        # If a list of cards was provided, add them to the initial collection
        for card in cards:
            self.add_card(card)

    def add_card(self, new_card):
        # Check the type of the input object, and if it is a Card add it to
        # (the end of) the collection
        assert isinstance(new_card, Card)
        self.collection.append(new_card)

    def new_deck(self, num_decks=1, include_joker=False):
        # Create an integer num_decks standard deck(s) of playing cards
        assert isinstance(num_decks, int)

        # Lists available ranks and suits
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
                 "Jack", "Queen", "King", "Ace"]
        suits = ["Hearts", "Spades", "Diamonds", "Clubs"]

        # Iterates over available ranks and suits to create each card
        for deck_count in range(num_decks):
            for rank in ranks:
                for suit in suits:
                    this_card = Card(rank=rank, suit=suit)
                    self.add_card(this_card)

        # Does not currently support adding jokers to the deck, may be an
        # area for future development
        if include_joker:
            raise NotImplementedError

    def shuffle(self):
        # Randomly rearrange the cards in the CardCollection
        shuffle(self.collection)

    def split(self, num_split):
        # Divide the collection as evenly as possible into integer
        # num different CardCollections
        assert isinstance(num_split, int)

        # Initialize the object we'll return
        sub_collections = []

        # Algorithmically split this collection into sub-collections:
        num_cards = len(self.collection)
        num_rem = num_cards % num_split

        for i in range(num_split):
            # Third terms account for potentially uneven splits, where some
            # sub-collections will include more than num_cards//num_split entries
            start_index = i * (num_cards//num_split) + min(i, num_rem)
            end_index = (i+1) * (num_cards//num_split) + min(i+1, num_rem)
            sub_collections.append(CardCollection(self.collection[start_index:end_index]))

        return sub_collections

    def deal(self, num_cards=1):
        # Remove the first integer n cards from the collection and return them
        # This may be an area for future optimization
        assert isinstance(num_cards, int)
        assert num_cards > 0

        # Create the list that will contain returned cards
        dealt = []
        for i in range(num_cards):
            dealt.append(self.collection.pop(0))

        # If we've only requested one card, return one card (rather than a list)
        if num_cards == 1:
            dealt = dealt[0]

        return dealt

    def peek(self):
        # Return a copy of the last (most recently added) card in a collection
        return self.collection[-1]