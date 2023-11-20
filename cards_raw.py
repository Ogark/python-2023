import itertools
from enum import Enum, auto, IntEnum

class Suit(Enum):
    SPADES = auto()
    HEARTS = auto()
    DIAMONDS = auto()
    CLUBS = auto()

class UpperRank(IntEnum):
    J = 11
    Q = 12
    K = 13
    A = 14

ranks = [6, 7, 8, 9, 10, UpperRank.J, UpperRank.Q, UpperRank.K, UpperRank.A]

class Card:
    __slots__ = 'rank', 'suit'

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank} of {self.suit.name}'

if __name__ == '__main__':
    # Create a deck of cards
    deck = [Card(rank, suit) for rank, suit in itertools.product(ranks, Suit)]

    # Display the deck
    for card in deck:
        print(card)
