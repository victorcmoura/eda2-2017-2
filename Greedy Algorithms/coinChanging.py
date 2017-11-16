def print_coins(coins):
    print('Coin list:')

    for coin in coins:
        print('Value:', coin['value'], '-', 'Quantity:', coin['quantity'], '-', 'Total value:', coin['quantity']*coin['value'])


value = float(input('Insert change value: '))

coin_possibilities = [
    {'value': 0.01, 'quantity': 0},
    {'value': 0.05, 'quantity': 0},
    {'value': 0.10, 'quantity': 0},
    {'value': 0.25, 'quantity': 0},
    {'value': 0.50, 'quantity': 0},
    {'value': 1.00, 'quantity': 0}
    ]

# Initializing with the biggest coin
selected_coin = 5

while selected_coin >= 0:
    if coin_possibilities[selected_coin]['value'] <= value:
        value = value - coin_possibilities[selected_coin]['value']
        coin_possibilities[selected_coin]['quantity'] = coin_possibilities[selected_coin]['quantity'] + 1
    else:
        selected_coin = selected_coin - 1

print_coins(coin_possibilities)
