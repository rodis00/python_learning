import sys

from Logic import Logic

class Game:
    def __init__(self):
        self.logic = Logic()
        self.logic.shuffleCards()
        # self.logic.show()
        self.logic.orderCards()
        # print('--------------------------')
        # print('Player cards:')
        # self.logic.showPlayerCards()
        # print('------------')
        # print('Bot cards:')
        # self.logic.showBotCards()

    def startGame(self):
        while True:
            for bot_card in self.logic.bot.on_hand:
                print(bot_card)
                input("rzuć kartę.")
                for player_card in self.logic.player.on_hand:
                    print(player_card)
                    if bot_card.value > player_card.value:
                        print('bot win')
                        print('---------')
                        self.logic.bot.on_hand.append(player_card)
                        self.logic.player.on_hand.remove(player_card)
                        self.logic.bot.on_hand.append(bot_card)
                        self.logic.bot.on_hand.remove(bot_card)
                        break
                    elif player_card.value > bot_card.value:
                        print('player win')
                        print('---------')
                        self.logic.player.on_hand.append(bot_card)
                        self.logic.bot.on_hand.remove(bot_card)
                        self.logic.player.on_hand.append(player_card)
                        self.logic.player.on_hand.remove(player_card)
                        break
                    else:
                        print('draw')
                        self.logic.bot.on_hand.append(bot_card)
                        self.logic.bot.on_hand.remove(bot_card)
                        self.logic.player.on_hand.append(player_card)
                        self.logic.player.on_hand.remove(player_card)
                        break

                if len(self.logic.bot.on_hand) == 0:
                    print('Player is winner')
                    sys.exit()
                elif len(self.logic.player.on_hand) == 0:
                    print('Bot is winner')
                    sys.exit()


game = Game()
game.startGame()