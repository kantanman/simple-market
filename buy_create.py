import data_struc

def buy_create(price, quantity, market_id):
    trade = data_struc.buy_object(price, quantity, market_id)
    try:
        data_struc.market_list[market_id].buy.append(trade)
        #check price here
        
    except KeyError:
        print("market doesnt exist :(")
    
    return trade
