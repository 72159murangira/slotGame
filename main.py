import random

max_lines = 3
max_bet = 100
min_bet = 1

rows = 3
columns = 3

symbol_count = {
    "A":8,
    "B":6,
    "C":4,
    "D":2
}

symbol_value = {
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def check_winnings(col, lines, bet, value):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = col[0][line]
        for cols in col:
            symbol_to_check = cols[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += value[symbol] * bet
            winnings_lines.append(line + 1)
    return winnings, winnings_lines

def get_slot_spin(rows, columns, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    col = []
    for _ in range(columns):
        cols = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            cols.append(value)

        col.append(cols)
    return col

def print_slot_spin(col):
    for row in range(len(col[0])):
        for i, cols in enumerate (col):
            if i != len(cols) - 1:
                print(cols[row], end=" | ")
            else:
                print(cols[row], end= "")
        print()

def deposit():
    while True:
        amount = input("What is your deposit? $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero")
        else:
            print("please enter a number")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter number of lines(1-" + str(max_lines)+ ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= max_lines:
                break
            else:
                print("Enter valid Number of lines")
        else:
            print("please enter a number")

    return lines

def get_bet():
    while True:
        amount = input("What is your bet amount? $ ")
        if amount.isdigit():
            amount = int(amount)
            if min_bet <= amount <= max_bet:
                break
            else:
                print(f"Amount must be between ${min_bet} or ${max_bet}.")
        else:
            print("please enter a number")

    return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet *lines

        if total_bet > balance:
            print(f"you don't have enuff to bet. you only have ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_spin(rows, columns, symbol_count)
    print_slot_spin(slots)
    winnings, winnings_line = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    if winnings_line:
        print(f"You won on Lines: ", *winnings_line)
    else:
        print("No lines matched. Better Luck next time. ")


main()