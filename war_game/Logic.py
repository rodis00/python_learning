import random
from Cards import Cards
from Player import Player
from Bot import Bot


class Logic:
    def __init__(self):
        self.cards = Cards()
        self.player = Player()
        self.bot = Bot()

    # shuffle cards
    def shuffleCards(self):
        random.shuffle(self.cards.cards_list)

    def show(self):
        for card in self.cards.cards_list:
            print(card)

    # order cards to players
    def orderCards(self):
        all_cards = len(self.cards.cards_list)
        counter = 0
        for card in self.cards.cards_list:
            if counter < all_cards // 2:
                self.player.on_hand.append(card)
                self.cards.cards_list.remove(card)
                counter += 1

        for card in self.cards.cards_list:
            self.bot.on_hand.append(card)

    def showPlayerCards(self):
        for card in self.player.on_hand:
            print(card)

    def showBotCards(self):
        for card in self.bot.on_hand:
            print(card)
