from random import randint
from collections import Counter

class Deck:

    def __init__(self):
        self.cards = []
        for suit in ["Clubs", "Diamonds", "Hearts", "Spades"]:
            values = list(range(2, 11))
            values.extend(["Jack", "Queen", "King"])
            for val in values:
                self.cards.append((val, suit))

    def shuffle(self):
        temp = self.cards[:]
        self.cards = []
        while len(temp):
            idx = randint(0, len(temp) - 1)
            card = temp.pop(idx)
            self.cards.append(card)

def test(num_samples):
    deck = Deck()
    pos_ctr = Counter()
    for _ in range(num_samples):
        deck.shuffle()
        for i, card in enumerate(deck.cards):
            pos_ctr[card] += i

    for card in pos_ctr.keys():
        pos_ctr[card] /= num_samples

    return pos_ctr

print(test(10000))
    
