global_trade_id = 0
global_market_id = 0
market_list = {}

class market:
    def __init__(self, Min, Max):
        global global_market_id
        self.sell = []
        self.buy = []
        self.min = Min
        self.max = Max
        self.market_id = global_market_id 
        global_market_id += 1
        
        
class buy_object:
    def __init__(self, price, quantity, market_id):
        global global_trade_id
        self.trade_id = global_trade_id  
        self.price = price
        self.quantity = quantity
        self.status = True
        self.market_id = market_id
        global_trade_id += 1

class sell_object:
    def __init__(self, price, quantity, market_id):
        global global_trade_id
        self.trade_id = global_trade_id 
        self.price = price
        self.quantity = quantity
        self.status = True
        self.market_id = market_id
        global_trade_id += 1