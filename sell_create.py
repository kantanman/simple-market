import data_struc

def sell_create(price, quantity, market_id):
    trade = data_struc.sell_object(price, quantity, market_id)
    try:
        data_struc.market_list[market_id].buy.append(trade)
    except KeyError:
        print("Market doesnt exist :(")

    return trade