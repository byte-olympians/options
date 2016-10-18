class OptionLeg:
    
    def __init__(self, type, strike, premium, sellbuy):
        self.type = type
        self.strike = strike
        self.premium = premium
        self.sellbuy = sellbuy
        
    def get_strategy(self):
        strat = self.sellbuy + self.type
        
        return strat
    