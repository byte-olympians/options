from option_leg import *

class LongUnderlying:
    def calculate_payoff(self, strike, entry, price, amount):
        payoff = (price - entry) * amount
        return payoff
        
class ShortUnderlying:
    def calculate_payoff(self, strike, entry, price, amount):
        payoff = (entry - price) * amount
        return payoff

class LongCall:
    def calculate_payoff(self, strike, premium, price, amount):
        if price <= strike:
            payoff = -premium * amount * 100
        else:
            payoff = (price - strike - premium) * amount * 100
        return payoff

class ShortCall:
    def calculate_payoff(self, strike, premium, price, amount):
        if price <= strike:
            payoff = premium * amount * 100
        else:
            payoff = (strike - price + premium) * amount * 100
        return payoff
        
class LongPut:
    def calculate_payoff(self, strike, premium, price, amount):
        if price <= strike:
            payoff = (strike - price - premium) * amount * 100
        else:
            payoff = -premium * amount * 100
        return payoff
        
class ShortPut:
    def calculate_payoff(self, strike, premium, price, amount):
        if price <= strike:
            payoff = (price - strike + premium) * amount * 100
        else:
            payoff = premium * amount * 100
        return payoff
        
if __name__ == "__main__":
    long_underlying = LongUnderlying()
    assert (long_underlying.calculate_payoff(0, 50, 60, 100) == 1000), "Expected value: 1000"
    short_underlying = ShortUnderlying()
    assert (short_underlying.calculate_payoff(0, 50, 60, 100) == -1000), "Expected value: -1000"
    long_call = LongCall()
    assert (long_call.calculate_payoff(50, 5, 60, 1) == 500), "Expected value: 500"
    short_call = ShortCall()
    assert (short_call.calculate_payoff(50, 5, 60, 2) == -1000), "Expected value: -1000"
    long_put = LongPut()
    assert (long_put.calculate_payoff(50, 5, 60, 2) == -1000), "Expected value: -1000"
    short_put = ShortPut()
    assert (short_put.calculate_payoff(50, 5, 60, 1) == 500), "Expected value: 500"
    