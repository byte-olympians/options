from option_leg import *

class LongUnderlying:
    def calculate_payoff(self, price, leg):
        payoff = (price - leg.entry) * leg.amount
        return payoff
        
class ShortUnderlying:
    def calculate_payoff(self, price, leg):
        payoff = (leg.entry - price) * leg.amount
        return payoff

class LongCall:
    def calculate_payoff(self, price, leg):
        if price <= leg.strike:
            payoff = - leg.entry * leg.amount * 100
        else:
            payoff = (price - leg.strike - leg.entry) * leg.amount * 100
        return payoff

class ShortCall:
    def calculate_payoff(self, price, leg):
        if price <= leg.strike:
            payoff = leg.entry * leg.amount * 100
        else:
            payoff = (leg.strike - price + leg.entry) * leg.amount * 100
        return payoff
        
class LongPut:
    def calculate_payoff(self, price, leg):
        if price <= leg.strike:
            payoff = (leg.strike - price - leg.entry) * leg.amount * 100
        else:
            payoff = -leg.entry * leg.amount * 100
        return payoff
        
class ShortPut:
    def calculate_payoff(self, price, leg):
        if price <= leg.strike:
            payoff = (price - leg.strike + leg.entry) * leg.amount * 100
        else:
            payoff = leg.entry * leg.amount * 100
        return payoff
        
if __name__ == "__main__":
    long_underlying = LongUnderlying()
    assert (long_underlying.calculate_payoff(60, Leg("Long", "Underlying", 0, 50, 100)) == 1000), "Expected value: 1000"
    short_underlying = ShortUnderlying()
    assert (short_underlying.calculate_payoff(60, Leg("Short", "Underlying", 0, 50, 100)) == -1000), "Expected value: -1000"
    long_call = LongCall()
    assert (long_call.calculate_payoff(60, Leg("Long", "Call", 50, 5, 1)) == 500), "Expected value: 500"
    short_call = ShortCall()
    assert (short_call.calculate_payoff(60, Leg("Short", "Call", 50, 5, 2)) == -1000), "Expected value: -1000"
    long_put = LongPut()
    assert (long_put.calculate_payoff(60, Leg("Long", "Put", 50, 5, 2)) == -1000), "Expected value: -1000"
    short_put = ShortPut()
    assert (short_put.calculate_payoff(60, Leg("Short", "Put", 50, 5, 1)) == 500), "Expected value: 500"
    