import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True
global Betting 
global total

# Laver en card klasser der skal opretter mit deck


class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + ' of ' + self.suit

# Opretter min deck, Som random.suffle til at fylde listen op med en tilfældig række følge af kortne

class Deck:
    
    def __init__(self):
        self.deck = []   # Tom liste
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__() # Tilføjer til deck indtil den er fyldt
        return 'The deck has' + deck_comp
            
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card

#creating a hand#

class Hand:
    def __init__(self):
        self.cards = []  # Starter med en tom liste
        self.value = 0   # Setter deres total til 0
        self.aces = 0    # sørgre får checkeren får ace er 0
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 11
            self.aces -= 1
                  
  
             

# HIt metode til at få kort

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

# Hit og stand metoeden, når man spiller spliiet

def hit_or_stand(deck,hand):
    global playing
    
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's'")
        
        if x[0].lower() == 'h':
            hit(deck,hand) 

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue
        break

# Her viser jeg kortne fra spillet men kune det ene kort får dealeren#functions to display cards#

def show_some(player,dealer):
    print("\nDealer's Hand")
    print("<card hidden>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand: ", *player.cards, sep= '\n')
    print("Player's Hand = ", player.value)    
        
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep="\n")
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand: ", *player.cards, sep= '\n')
    print("Player's Hand = ", player.value)
    

# Her oprettes spil logikken
def game():
    global playing
    total = 100
    Betting = 0
    while True:
        # Velkommen besked samt hvor meget han vil bette
        print("Welcome to the best Blackjack game.")
        print("Your Chips are: "+ str(total))
        while True:
            Betting = input("How much u wanna bet?")
            if int(Betting) > total:
                print("You dont have that much chips try again")
            else:
                break    
        
        # Opretter og shuffler et nyt deck og giver kort til begge dealer og spiller
        deck = Deck()
        deck.shuffle()
    
        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())
    
        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())
    
        # Viser kortne
        show_some(player_hand, dealer_hand)
        while playing:
            # Her laver jeg logikken får double down
            if player_hand.value<=11:
                double_input = input("Do you want to double down? (Y/N)") 
                print(double_input)
                if double_input == "Y" and (int(Betting)+int(Betting)) <= total:
                    Betting = int(Betting)+int(Betting)
                    print(Betting)
                elif double_input == "Y" and (int(Betting+Betting)) > total:
                    print("You dont have the money to double down!")
                elif (double_input == "N"):
                    print("You have rejected to doubledown")
         # venter på at spiller kommer med sit valg om hit or stand
            hit_or_stand(deck, player_hand)

        #  Viser kornte igen med det næste kort i tilfælde af playerne tasted h
            show_some(player_hand, dealer_hand)

        # Hvis spilleren's total er højre 21 så vinder dealer samt mister han sin betting
            if player_hand.value >21:
                print("PLayer bust, Dealer wins")
                total = total - int(Betting)
                break

    # Hvis spiller ikke er busted så fortsætter dealeren med at trække indtil hans værdi er højre end 17
        if player_hand.value <= 21:
            
            while dealer_hand.value <17:
                hit(deck, dealer_hand)
                if(dealer_hand.value > player_hand.value):
                    break
    
        # Viser alle kortene nu
            show_all(player_hand,dealer_hand)
        
         # Checker får de forksellige scenarioer fra spillet
            if dealer_hand.value > 21:
                print("Dealer bust , Player wins")
                total = total + int(Betting)

            elif dealer_hand.value > player_hand.value:
                if (dealer_hand.value == 21):
                    print("Dealer Blackjack")
                print("Dealers value higher than player, Dealer wins")
                total = total - int(Betting)

            elif dealer_hand.value < player_hand.value:
                if (dealer_hand.value == 21):
                    print("Player Blackjack")
                print("Player hand better than Dealer, Player wins")
                total = total + int(Betting)

            else:
                print("Tie nobody lose anything")
        
    
    # Viser playeren sin chips værdi samt hvis den 0 så er det slut
        print("\nPlayers winnings stand at", total)     
        if(total<=0):
            print("U are out chips u lose")
            break    
    
    # Spørg om han vil spille igen
        new_game = input("would you like to play again? Enter 'y' or 'n'")
        if new_game[0].lower() == 'y':
            playing = True
            continue
        else:
            print('Thanks for playing! ')

            break

if __name__ == "__main__":
    game()        