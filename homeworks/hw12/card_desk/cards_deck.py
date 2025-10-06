import random


class Card:
    number_list = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    mast_list = ["Diamond", "Club", "Spade", "Heart"]

    def __init__(self, number, mast):
        self.number = number
        self.mast = mast


class CardsDeck:
    def __init__(self):
        self.cards = []
        self._create_deck()

    def _create_deck(self):
        for mast in Card.mast_list:
            for number in Card.number_list:
                new_card = Card(number, mast)
                self.cards.append(new_card)

        self.cards.append(Card(mast="Black", number="Joker"))
        self.cards.append(Card(mast="Red", number="Joker"))

        print(f"There are {len(self.cards)} cards in deck")

    def shuffle(self):
        random.shuffle(self.cards)
        print("The Card has been shuffled.")

    def get_card(self, index):
        valid_index = self._card_validator(index)
        real_index = valid_index - 1

        card = self.cards[real_index]
        self.cards.pop(real_index)
        return card

    def get_remaining_cards(self):
        return self.cards

    def _card_validator(self, index):
        if not isinstance(index, int):
            raise ValueError("Error: enter a card number from 1 to 54")
        real_index = index - 1
        if 0 <= real_index < len(self.cards):
            return index
        else:
            raise ValueError("Error: enter a card number from 1 to 54")
