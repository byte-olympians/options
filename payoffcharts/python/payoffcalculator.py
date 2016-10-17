from option_leg import *
from view import *
from strategies import *


class Calculator:
    def __init__(self):
        self.strategy_map = {"LongUnderlying": LongUnderlying(),
                            "ShortUnderlying": ShortUnderlying(),
                            "LongCall": LongCall(),
                            "ShortCall": ShortCall(),
                            "LongPut": LongPut(),
                            "ShortPut": ShortPut()
                            }
                            
    def register_legs(self, *args):
        legs =[leg for leg in args]
        return legs
    
    def register_strategy(self, legs):
        registered_strategies = {}
        for leg in legs:
            if leg.get_key() in self.strategy_map:
                registered_strategies[leg.get_key()] = [leg, self.strategy_map[leg.get_key()]]
        return registered_strategies
        
    def calculate(self, strategies):
        price = 0
        payoff = {}
        while price <= 100:
            result = []
            for strat in strategies:
                result.append(strategies[strat][1].calculate_payoff(strategies[strat][0].strike, strategies[strat][0].entry_price, price)) 
                payoff[price] = sum(result)
            price += 1
        return payoff
        
if __name__ == "__main__":
    result = Calculator()
    legs = result.register_legs(Leg("Long", "Call", 50, 5), Leg("Long", "Put", 50, 5), Leg("Long", "Underlying", 0, 50))
    strats = result.register_strategy(legs)
    print (result.calculate(strats))
    
        
        




