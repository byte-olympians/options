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
                            
    def calculate(self, legs):
        price = 0
        payoff = {}
        while price <= 100:
            value = 0
            for leg in legs:
                strat = self.strategy_map[leg.get_key()]
                value += strat.calculate_payoff(price, leg)
            payoff[price] = value
            price += 1
        return payoff
        
if __name__ == "__main__":
    result = Calculator()
    print (result.calculate([Leg("Long", "Underlying", 0, 50, 100), 
                            Leg("Short", "Call", 55, 1, 1),
                            Leg("Short", "Put", 48, 1.5, 1),
                            Leg("Long", "Put", 45, 0.5, 1),
                            Leg("Long", "Put", 42, 0.1, 1)]))
    
        
        




