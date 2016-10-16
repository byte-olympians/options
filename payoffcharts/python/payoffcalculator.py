from option_leg import *
from view import *
from strategies import *


class Calculator:
    def __init__(self):
        self.strategy_map = {}
        self.strategy = LongUnderlying()
    # def register_strategy(self, strategy):
    #     self.strategy_map[Option_Leg().get_key()]
        
        
    def calculate(self, *args):
        price = 0
        payoff = {}
        while price <= 100:
            result = []
            for leg in args:
                result.append(self.strategy.calculate_payoff(leg.entry, price)) 
                payoff[price] = sum(result)
            price += 1
        return payoff
        
if __name__ == "__main__":
    result = Calculator()
    print (result.calculate(Underlying("Long Underlying", 40), Underlying("Long Underlying", 50)))
    
        
        


    # def buy_call(self, price, strike, premium):
    #     if price <= strike:
    #         payoff = 0 - premium
    #     else:
    #         payoff = price - strike - premium
    #     return payoff
        
    # def buy_put(self, price, strike, premium):
    #     if price <= strike:
    #         payoff = strike- price - premium
    #     else:
    #         payoff = 0 - premium
    #     return payoff
        
    # def sell_call(self, price, strike, premium):
    #     if price <= strike:
    #         payoff = premium
    #     else:
    #         payoff = strike - price + premium
    #     return payoff
        
    # def sell_put(self, price, strike, premium):
    #     if price <= strike:
    #         payoff = price - strike + premium
    #     else:
    #         payoff = premium
    #     return payoff
    
    # def long_underlying(self, price, entry):
    #     payoff = price - entry
    #     return payoff
        
    # def short_underlying(self, price, entry):
    #     payoff = entry - price
    #     return payoff
    
    # def calculate(self):
    #     leg1 = Options("Buy","Call",50,5)
    #     leg2 = Options("Buy", "Put",50,5)
    #     self.strategy= [leg1,leg2]
        
    #     j = 0
    #     payoff = {}
    #     while j <= 100:
    #         payoff[j] = self.buy_call(j, self.strategy_map['Long Straddle'][0].strike, self.strategy_map['Long Straddle'][0].premium) + self.buy_put(j,self.strategy_map['Long Straddle'][1].strike, self.strategy_map['Long Straddle'][1].premium)
    #         j += 1
    #     print (payoff)
        



