import data_struc as ds

def sell_create(price, quantity, market_id):

    #instantiate sell object
    trade = ds.sell_object(price, quantity, market_id)
    try:
        ds.market_list[market_id].sell.append(trade)
        assert(price >= ds.market_list[market_id].min and price <= ds.market_list[market_id].max)
    except (KeyError, AssertionError):
        print("market doesnt exist or price is incorrect")

    #find matching trade 
    for i in ds.market_list[market_id].buy:
        if (i.price == price) and (i.quantity == quantity):
            print("Trade matched with trade_id: {} for {} units at {} dollars".format(i.trade_id, i.quantity, i.price))
        else:
            print("submitted trade")

    return trade