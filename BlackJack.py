'''
Program Name : BlackJack.py
Log          : 22-Oct-2019 - Initial Creation
Status       : Complete
'''

import random

values = {'ace': 11, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
                '10':10, 'jack':10, 'queen':10, 'king':10}

ranks = ['ace','2','3','4','5','6','7','8','9','10','jack','queen','king']

suits = ['Spades','Hearts','Diamonds','Clubs']


class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        temp = ''
        temp = "-" * len(f"| {self.suit} --> {self.rank} |")+'\n'
        temp += f"| {self.suit} --> {self.rank} |\n"
        temp += "-" * len(f"| {self.suit} --> {self.rank} |")
        return temp

class Deck:
    def __init__(self):
        self.deck = []
        for i in suits:
            for j in ranks:
                self.deck.append(Card(i,j))

    def __str__(self):
        temp = ''
        for i in self.deck:
            temp += i.suit + ' --> ' + i.rank + '\n'
        return temp

    def shuffle(self):
        random.shuffle(self.deck)

    def random_pick(self):
        temp_card = random.choice(self.deck)
        self.deck.pop(self.deck.index(temp_card))
        return temp_card

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0

    def add_cards(self,Card):
        self.cards.append(Card)

    def cal_value(self):
        self.value = 0
        for i in self.cards:
            self.value += values[i.rank]
        return self.value

    def __str__(self):
        for i in self.cards:
            print(i)

class Chips:
    def __init__(self):
        self.total_chips = 100
        self.bet = 0

    def win_bet(self):
        self.total_chips += self.bet

    def lose_bet(self):
        self.total_chips -= self.bet


def hit_card(Deck,Hand):
    Deck.shuffle()
    print("Picking new card...")
    pick_card = Deck.random_pick()
    print(pick_card)
    Hand.add_cards(pick_card)
    print(Hand.value)
    Hand.cal_value()
    Hand.__str__()
    print(Hand.value)
    return Hand


def bust_check(Hand):
    if Hand.value > 21:
        return True
    else:
        return False


def win_lose(Chips,sym):
    if sym == 'w':
        Chips.win_bet()
        print(f"Player has WON, his bet was {Chips.bet} and his updated chips count is {Chips.total_chips}")
    else:
        Chips.lose_bet()
        print(f"Player has LOST, his bet was {Chips.bet} and his updated chips count is {Chips.total_chips}")


def main():
    print("Welcome to BLACKJACK !!!!\n")

    deck = Deck()
    deck.shuffle()

    p1ch = Chips()
    Dealer = True

    print("Player has 100 chips allocated and how much would he like to bet?")

    while True:
        try:
            p1ch.bet = int(input("Enter bet amount : "))
            if p1ch.bet < p1ch.total_chips:
                print("total chips -",p1ch.total_chips)
                print("bet amount -",p1ch.bet)
                break
            else:
                print("Your bet amount exceeds the chips allocated to you, try again.")
                continue
        except:
            print("Incorrect value, Enter the bet value within the allocated chips range.")

    print("Assigning 2 cards to the player with open face")
    player1 = Hand()
    player1.add_cards(deck.random_pick())
    player1.add_cards(deck.random_pick())
    player1.__str__()
    print("Player card Value -",player1.cal_value())

    print("Assigning 2 cards to the dealer and revealing only one face")
    dealer = Hand()
    dealer.add_cards(deck.random_pick())
    dealer.add_cards(deck.random_pick())
    print(dealer.cards[0])
    dealer.cal_value()

    print("PLAYER's turn to HIT the card...")

    while True:

        if bust_check(player1):
            print("Last Rank -",player1.cards[-1].rank)
            if player1.cards[-1].rank == 'ace':
                print("Player got BUST but his last pick was an ace, adjusting ace value to 1.")
                player1.value -= 10
                if bust_check(player1):
                    print(f"GAME OVER!! It's a BUST! Player's card value after adjustment is {player1.value} and has exceeded 21.")
                    win_lose(p1ch, 'l')
                    Dealer = False
                    break
                else:
                    continue
            else:
                print("GAME OVER!! It's a BUST! Player's card value has exceeded 21.")
                win_lose(p1ch, 'l')
                Dealer = False
                break
        else:
            print(f"Players hand value is {player1.value}. Would you like to HIT or STAND?")
            while True:
                try:
                    hit_stand = int(input("Press 1 to 'HIT' and 2 to 'STAND'"))
                    if hit_stand not in (1,2):
                        print("Please enter valid input.")
                        continue
                    else:
                        break
                except Exception as e:
                    print("Invalid input -",e,"- Try again.")

            if hit_stand == 1:
                print("Player decided to HIT!")
                player1 = hit_card(deck, player1)
                continue
            else:
                print("Player decided to STAND! Playing the dealer now.")
                break

    if Dealer:
        print("\nPlaying the DEALER's turn now...")
        print("Reveling the dealer's 2nd card")

        dealer.__str__()
        print("Dealer card Value -", dealer.cal_value())


    while Dealer:
        if dealer.value < 17:
            print("Dealer's cards value is less than 17, Dealer HITs again.")
            dealer = hit_card(deck, dealer)
            continue
        elif dealer.value > 21:
            print(f"GAME OVER!! DEALER BUST! Dealer's cards value is {dealer.value} and has exceeded 21. PLAYER WINS THE MATCH!!")
            win_lose(p1ch,'w')
            break
        else:
            if player1.value > dealer.value:
                print(f"PLAYER WINS!! Player's value is {player1.value} and is greater than dealer's value {dealer.value}")
                win_lose(p1ch, 'w')
                break
            elif player1.value == dealer.value:
                print(f"The match is a STALEMATE as both dealer and player scores are same, Dealer - {dealer.value} and Player - {player1.value}")
                break
            else:
                print(f"DEALER WINS!! Dealer's value is {dealer.value} and is greater than player's value {player1.value}")
                win_lose(p1ch, 'l')
                break



if __name__ == '__main__':
    while True:
        main()
        cont = input('Do you want to play again? Press "Y" for yes and "N" for no - ')
        if cont.lower() in ('y','yes'):
            continue
        else:
            break