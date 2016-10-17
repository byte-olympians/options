from option_leg import *

class LongUnderlying:
    def calculate_payoff(self, strike, entry, price):
        payoff = price - entry
        return payoff
        
class ShortUnderlying:
    def calculate_payoff(self, strike, entry, price):
        payoff = entry - price
        return payoff

class LongCall:
    def calculate_payoff(self, strike, premium, price):
        if price <= strike:
            payoff = 0 - premium
        else:
            payoff = price - strike - premium
        return payoff

class ShortCall:
    def calculate_payoff(self, strike, premium, price):
        if price <= strike:
            payoff = premium
        else:
            payoff = strike - price + premium
        return payoff
        
class LongPut:
    def calculate_payoff(self, strike, premium, price):
        if price <= strike:
            payoff = strike - price - premium
        else:
            payoff = 0 - premium
        return payoff
        
class ShortPut:
    def calculate_payoff(self, strike, premium, price):
        if price <= strike:
            payoff = price - strike + premium
        else:
            payoff = premium
        return payoff