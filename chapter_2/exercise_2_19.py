def first_denomination(x):
    return x[0]

def except_first_denomination(x):
    return x[1:]
    
def n_more(x):
    return len(x)

def cc(amount, coin_values):
    if amount == 0:
        return 1
    elif amount < 0 or n_more(coin_values) == 0:
        return 0
    else:
        return cc(amount, except_first_denomination(coin_values)) + cc(amount - first_denomination(coin_values), coin_values)

us_coins = [50, 25, 10, 5, 1]
uk_coins = [100, 50, 20, 10, 5, 2, 1, 0.5]

print(cc(100, us_coins))