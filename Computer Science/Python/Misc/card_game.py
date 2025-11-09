import random

class PlayingCard():
    
    def __init__(self,given_suit: str, given_rank: str, given_value: int, given_hidden_state = False):
        self._isHidden = given_hidden_state
        self._rank = given_rank
        self._suit = given_suit
        self._value = given_value        #Value = how much a card is worth towards a players total score

    def get_rank(self):

        return self._rank

    def get_suit(self):

        return self._suit
        
class Player():
    _isDealer = False

    def __init__(self, given_name):
        self._name = given_name
        self._score = 0
    
    def get_decision(self):
        #ask for player's input (i.e stick or draw in first stage of game)

        answer = input(f"{self._name} would you like to stick or draw?")

        while answer.lower() != ("stick","deal"):
            answer = input(f"Invalid answer. {self._name} would you like to stick or draw?")
        


class Dealer(Player):
    _isDealer = True

    def get_decision(self):
        pass


class Deck():

    def __init__(self):
        self._cards = []
        
        #Instantiating 52 playing cards
        
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

        for i in range(len(suits)):
            for j in range(len(ranks)):
                new_card = PlayingCard(suits[i], ranks[j], values[j])
                self._cards.append(new_card)

#    def hide_card(self, given_card_index: int):
        #hide given card in a deck

        #janky code to store both the hidden card and its original index in its deck in a seperate array
#        self._cards[given_card_index]._isHidden = True

#    def reveal_card(self, given_card_index: int):
        #reveal given card in a deck (i.e. the opposite of hide_card)

#       self._cards[given_card_index]._isHidden = False

    def show_deck(self):
        #prints whole deck in rank-suit format
        
        print("\nCurrent Deck: ")
        for card in self._cards:
            print(f"{card.get_rank()} of {card.get_suit()}, ",end = " ")

    def shuffle(self):
        #shuffles whole deck randomly
        
        random.shuffle(self._cards)

    def deal(self, given_num: int):
        #picks card on top of deck then removes it from the deck

        dealt_cards = []
        for i in range(given_num):
            dealt_cards.append(self._cards[len(self._cards) - 1])
            self._cards.pop(len(self._cards) - 1)
        
        return dealt_cards
    
class Hand(Deck):

    def __init__(self, given_player: object):
        self._cards = []
        self._player = given_player

    def receive(self, given_dealt_cards):
        #adds given dealt card to the player's hand

        for i in range(len(given_dealt_cards)):
            self._cards.append(given_dealt_cards[i-1])

    def show_deck(self):
        #prints whole hand in rank-suit format
        
        if self._player._isDealer == True:
            print(f"\n{self._player._name}'s (Dealer) hand:\n")
            for card in self._cards:
                print(f"[{card.get_rank()} of {card.get_suit()}] ",end = " ")
        
        else:
            print(f"\n{self._player._name}'s hand:\n")
            for card in self._cards:
                print(f"[{card.get_rank()} of {card.get_suit()}] ",end = " ")


def main():
    dealer_1 = Dealer(input("Enter dealer's name: "))
    player_1 = Player(input("\nEnter player's name: "))

    deck_1 = Deck()

    hand_1 = Hand(dealer_1)
    hand_2 = Hand(player_1)

    deck_1.shuffle()
    
    dealt_cards = deck_1.deal(1)

    hand_1.receive(dealt_cards)

    dealt_cards = deck_1.deal(2)

    hand_2.receive(dealt_cards)

    hand_1.show_deck()

    hand_2.show_deck()

    decision = player_1.get_decision()

    dealer_1.get_decision()

main()
