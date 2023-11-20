import itertools
from enum import Enum

_ranks = [6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
_suits = {
    'spades': '\u2660',
    'hearts': '\u2665',
    'diamonds': '\u2666',
    'clubs': '\u2663'
}

class SuitEnum(Enum):
    def __str__(cls):
        return cls.value

Suit = SuitEnum('Suit', _suits)

class Card:
    __slots__ = 'rank', 'suit'

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

class CardDeckBase:
    def __init__(self):
        self.cards = []

class FrenchDeck(CardDeckBase):
    def __init__(self):
        super().__init__()
        self.cards = [Card(rank, Suit[suit]) for rank, suit in itertools.product(_ranks, _suits)]

if __name__ == '__main__':
    french_deck = FrenchDeck()
    
    print("French Deck created with the following cards:")
    for card in french_deck.cards:
        print(f'{card.rank} of {card.suit}')
