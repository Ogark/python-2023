from collections import namedtuple
from enum import Enum, IntEnum

BasicSuit = namedtuple('BasicSuit', ['name', 'symbol'])


class SymbolMixin:

    def __str__(self):
        return self.symbol


# A little bit of overengineering
class Suit(SymbolMixin, BasicSuit):
    pass


# Or simply:
##class Suit(BasicSuit):
##    def __str__(self):
##        return self.symbol

##spades, hearts, diamonds, clubs = [
##    Suit(symbol=sym) for sym in ['\u2660', '\u2665', '\u2666', '\u2663']
##]

### OR more explicitly
##spades = Suit(symbol='\u2660')
##hearts = Suit(symbol='\u2665')
##diamonds = Suit(symbol='\u2666')
##clubs = Suit(symbol='\u2663')


class UpperRank(IntEnum):
    J = 11
    Q = 12
    K = 13
    A = 14


##    @classmethod
##    def _missing_(cls, value):
##        iv = int(value)
##        if iv > 0 and iv < cls.J:
##            return iv
##        # if execution continues, not exit from function by return
##        return super()._missing_(value)

ranks = [6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
# or  ranks = list(range(6, 10 + 1)) + list('JQKA')
suits = {
    'spades': '\u2660',
    'hearts': '\u2665',
    'diamonds': '\u2666',
    'clubs': '\u2663'
}

# Make name.value representation for creating Enum
_suitvals = {k: Suit(name=k, symbol=v) for k, v in suits.items()}
CardSuit = Enum('CardSuit', _suitvals)


class Card:
    __slots__ = 'rank', 'suit'  # consume less memory

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit


if __name__ == '__main__':
    ...
