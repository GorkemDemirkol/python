import random

max_lines = 3
max_bet = 300
min_bet = 1
rows = 3
cols = 3

symbol_count = {
    '🍒': 2,
    '🍊': 4,
    '🍋': 6,
    '🍉': 8,
    '🍇': 10,
    '🍓': 12,
    '🍑': 14,
    '🍍': 16
}
symbol_values = {
    '🍒': 8,
    '🍊': 7,
    '🍋': 6,
    '🍉': 5,
    '🍇': 4,
    '🍓': 3,
    '🍑': 2,
    '🍍': 1
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    for line in range(lines):
        symbol = columns[0][line]
        count = 1
        for col in range(1, cols):
            if columns[col][line] == symbol:
                count += 1
            else:
                break
        if count == cols:
            winnings += values[symbol] * bet
    return winnings

def generate_slot():
    return [random.choice(list(symbol_count.keys())) for _ in range(cols)]

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)
    
    columns = []
    for _ in range(cols):
        column = random.sample(all_symbols, rows)
        columns.append(column)
    
    return columns

def deposit():
    while True:
        amount = input("Yatırmak istediğiniz miktarı giriniz: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Lütfen 0'dan büyük bir miktar giriniz.")
        else:
            print("Lütfen rakam giriniz.")
    return amount

def get_number_of_lines():
    while True:
        lines = input(f"Oynayacağınız satır sayısı (1-{max_lines}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= max_lines:
                break
            else:
                print(f"Lütfen 1 ile {max_lines} arasında bir sayı giriniz.")
        else:
            print("Lütfen rakam giriniz.")
    return lines

def get_bet():
    while True:
        bet = input(f"Oynayacağınız miktarı giriniz ({min_bet}-{max_bet}): ")
        if bet.isdigit():
            bet = int(bet)
            if min_bet <= bet <= max_bet:
                break
            else:
                print(f"Lütfen {min_bet} ile {max_bet} arasında bir miktar giriniz.")
        else:
            print("Lütfen rakam giriniz.")
    return bet

def main():
    balance = deposit()
    lines = get_number_of_lines()
    
    while True:
        bet = get_bet()
        total_bet = lines * bet
        if total_bet > balance:
            print("Bakiyeniz yetersiz.")
            print(f"Bakiyeniz {balance}₺, toplam bahis tutarınız {total_bet}₺.")
        else:
            break
    
    print(f"Bahis tutarınız {bet}₺, {lines} slot için toplam bahis tutarınız {total_bet}₺.")
    slots = get_slot_machine_spin(rows, cols, symbol_count)
    for row in slots:
        print(" | ".join(row))
    wininngs=check_winnings(slots,lines,bet,symbol_values)
    print(f"Kazanılan miktar: {wininngs}₺")
    balance += wininngs 
    print(f"Yeni bakiyeniz: {balance}₺") 

main()