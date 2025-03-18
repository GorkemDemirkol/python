import random  

suits = ('Kupa', 'Karo', 'Sinek', 'Maça')  
ranks = ('İki', 'Üç', 'Dört', 'Beş', 'Altı', 'Yedi', 'Sekiz', 'Dokuz', 'On', 'Jack', 'Queen', 'King', 'Ace')  
values = {'İki': 2, 'Üç': 3, 'Dört': 4, 'Beş': 5, 'Altı': 6, 'Yedi': 7, 'Sekiz': 8, 'Dokuz': 9, 'On': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}  

class Card:  
    def __init__(self, suit, rank):  
        self.suit = suit  
        self.rank = rank  

    def __str__(self):  
        return self.suit + " " + self.rank  

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
    
    def reset(self):  
        self.cards = []  
        self.value = 0  
        self.aces = 0  
        
    def split(self):  
        first_hand = Hand()  
        second_hand = Hand()  
        first_hand.add_card(self.cards[0])  
        second_hand.add_card(self.cards[1])  
        return first_hand, second_hand  

class Chips:  
    def __init__(self):  
        self.total = int(input("Ne kadar çip almak istersiniz: "))  
        self.bet = 0  
        
    def winBet(self):  
        self.total += self.bet * 2  # Kazanılırsa 2 katı  
    
    def loseBet(self):  
        self.total -= self.bet  

def bahis(chips):  
    while True:  
        try:  
            chips.bet = int(input('Ne kadar bahis yapmak istersiniz: '))  
        except ValueError:  
            print("Lütfen geçerli bir sayı giriniz")  
        else:  
            if chips.bet > chips.total:  
                print(f"Yetersiz bakiye! Mevcut bakiyeniz: {chips.total}")  
            else:  
                break  

def hit(deck, hand):  
    hand.add_card(deck.deal())  
    hand.adjust_for_ace()  

def hit_or_stand(deck, hand):  
    global playing  
    while True:  
        x = input("Hit, stand veya split?(h/s/sp): ")  
        if x[0].lower() == 'h':  
            hit(deck, hand)  
        elif x[0].lower() == 's':  
            print("Oyuncu stand yapıyor. Kurupiyer'in sırası.")  
            playing = False  
        elif x[0].lower() == 'sp' and len(hand.cards) == 2 and hand.cards[0].rank == hand.cards[1].rank:  
            print("El split ediliyor!")  
            return hand.split()  
        else:  
            print("Lütfen geçerli bir seçenek giriniz.")  
            continue  
        break  

def show_some(player, dealer):  
    print("\nKurupiyer'in Eli: ")  
    print("<Kart gizli>")  
    print('', dealer.cards[1])  
    print("\nOyuncunun eli:", *player.cards, sep='\n')  

def show_all(player, dealer):  
    print("\nKurupiyer'in Eli:", *dealer.cards, sep='\n')  
    print("Kurupiyer'in Eli Toplam: ", dealer.value)  
    print("\nOyuncunun Eli:", *player.cards, sep='\n')  
    print("Oyuncunun Eli Toplam: ", player.value)  

def player_busts(chips):  
    print("Oyuncu battı!")  
    chips.loseBet()  

def player_wins(chips):  
    print("Oyuncu kazandı!")  
    chips.winBet()  

def dealer_busts(chips):  
    print("Dealer battı!")  
    chips.winBet()  

def dealer_wins(chips):  
    print("Dealer kazandı!")  
    chips.loseBet()  

def push(chips):  
    print("Berabere!")  
    chips.total += chips.bet  # Beraberlik durumunda yatırılan bahis geri alınır  

# Ana oyun döngüsü  
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

    bahis(player_chips)  

    show_some(player_hand, dealer_hand)  

    playing = True  
    
    # Burada split olup olmadığını kontrol et  
    if len(player_hand.cards) == 2 and player_hand.cards[0].rank == player_hand.cards[1].rank:  
        split_hands = hit_or_stand(deck, player_hand)  
        for hand in split_hands:  
            while playing:  
                hit_or_stand(deck, hand)  
                show_some(hand, dealer_hand)  

                if hand.value > 21:  
                    player_busts(player_chips)  
                    break  

            if hand.value <= 21:  
                while dealer_hand.value < 17:  
                    hit(deck, dealer_hand)  
                show_all(hand, dealer_hand)  

                if dealer_hand.value > 21:  
                    dealer_busts(player_chips)  
                elif dealer_hand.value > hand.value:  
                    dealer_wins(player_chips)  
                elif dealer_hand.value < hand.value:  
                    player_wins(player_chips)  
                else:  
                    push(player_chips)  

            # El bitiminde her iki eli de kontrol et  
            playing = True  # Her el için oyunu tekrar başlat  

    else:  
        # Normal oyun akışı  
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
                push(player_chips)  

    print(f"\nOyuncunun toplam fişi: {player_chips.total}")  

    new_game = input("Başka bir oyun oynamak ister misiniz? (e/h): ")  
    if new_game[0].lower() == 'e':  
        playing = True  
        continue  
    else:  
        print("Teşekkürler, tekrar görüşmek üzere!")  
        break  