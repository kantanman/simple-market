import data_struc


def market_create(Min, Max):
    try:
        assert (Min < Max) and (Min >= 0)
    except AssertionError:
        print ("input error")
    market = data_struc.market(Min, Max)
    
    data_struc.market_list[market.market_id] = market

    return market
    