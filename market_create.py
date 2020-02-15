import data_struc


def market_create(Min, Max):
    market = data_struc.market(Min, Max)
    data_struc.market_list[market.market_id] = market

    

    return market
    