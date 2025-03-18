import random

# Kart destesi oluşturma
suits = ('Kupa', 'Karo', 'Sinek', 'Maça')
ranks = ('İki', 'Üç', 'Dört', 'Beş', 'Altı', 'Yedi', 'Sekiz', 'Dokuz', 'On', 'Jack', 'Queen', 'King', 'Ace')
values = {'İki': 2, 'Üç': 3, 'Dört': 4, 'Beş': 5, 'Altı': 6, 'Yedi': 7, 'Sekiz': 8, 'Dokuz': 9, 'On': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.suit +" "+ self.rank

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    def __init__(self):
        self.total = 100  # Başlangıç bakiyesi
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('Ne kadar bahis yapmak istersiniz? '))
        except ValueError:
            print('Lütfen geçerli bir sayı giriniz.')
        else:
            if chips.bet > chips.total:
                print(f'Yetersiz bakiye! Mevcut bakiyeniz: {chips.total}')
            else:
                break

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input("Hit veya Stand? (h/s): ")

        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("Oyuncu stand yapıyor. Dealer'ın sırası.")
            playing = False
        else:
            print("Lütfen geçerli bir seçenek giriniz.")
            continue
        break

def show_some(player, dealer):
    print("\nDealer'ın Eli:")
    print(" <kart gizli>")
    print('', dealer.cards[1])
    print("\nOyuncunun Eli:", *player.cards, sep='\n ')

def show_all(player, dealer):
    print("\nDealer'ın Eli:", *dealer.cards, sep='\n ')
    print("Dealer'ın Eli =", dealer.value)
    print("\nOyuncunun Eli:", *player.cards, sep='\n ')
    print("Oyuncunun Eli =", player.value)

def player_busts(chips):
    print("Oyuncu battı!")
    chips.lose_bet()

def player_wins(chips):
    print("Oyuncu kazandı!")
    chips.win_bet()

def dealer_busts(chips):
    print("Dealer battı!")
    chips.win_bet()

def dealer_wins(chips):
    print("Dealer kazandı!")
    chips.lose_bet()

def push():
    print("Berabere! Push.")

while True:
    print("Blackjack'e Hoşgeldiniz!")

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()

    take_bet(player_chips)

    show_some(player_hand, dealer_hand)

    playing = True

    while playing:
        hit_or_stand(deck, player_hand)
        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_chips)
            break

    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_chips)
        else:
            push()

    print(f"\nOyuncunun toplam fişi: {player_chips.total}")

    new_game = input("Başka bir oyun oynamak ister misiniz? (e/h): ")
    if new_game[0].lower() == 'e':
        playing = True
        continue
    else:
        print("Teşekkürler, tekrar görüşmek üzere!")
        break
