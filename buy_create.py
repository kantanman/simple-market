# Creates a buy order

import data_struc as ds

def buy_create(price, quantity, market_id):

    #instantiate buy object
    trade = ds.buy_object(price, quantity, market_id)

    #check if market_id is correct and price in is range
    try:
        ds.market_list[market_id].buy.append(trade)
        assert(price >= ds.market_list[market_id].min and price <= ds.market_list[market_id].max)
    except (KeyError, AssertionError):
        print("market doesnt exist or price is incorrect")

    #find matching trade 
    for i in ds.market_list[market_id].sell:
        if (i.price == price) and (i.quantity == quantity):
            matched = {"buy": trade, "sell": i}
            ds.completed_trades.append(matched.copy())
            #trade matched, remove both buy and sell trades and add to completed trade list
            ds.market_list[market_id].sell.remove(i)            #remove sell trade
            ds.market_list[market_id].buy.remove(trade)         #remove buy trade

            print("Trade matched with trade_id: {} for {} units at {} dollars in market {}".format(i.trade_id, i.quantity, i.price, i.market_id))
        else:
            print("submitted trade")

    return trade
