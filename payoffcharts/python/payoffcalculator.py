from option_leg import *
from view import *

class PayOffCalculator:
    """The class that keeps a store of registered strategies and
    orchestrates the calls to them to calculate the payoffs"""

    def __init__(self):
        self.legs_map = {}
        self.strategy_map = {}
        self.view = View()

    def register_legs(self):
        self.legs_map["Buy Call"] = Options('buy', 'call', 50, 5)
        self.legs_map["Sell Call"] = Options('sell', 'call', 50, 5)
        self.legs_map["Buy Put"] = Options('buy', 'put', 50, 5)
        self.legs_map["Sell Call"] = Options('sell', 'put', 50, 5)
        self.legs_map["Long Underlying"] = Underlying('long',50)
        self.legs_map["Short Underlying"] = Underlying('short',50)
        
    def calculate(self, legs):
        self.strategy_map['Long Straddle'] = self.legs_map['Buy Call'].buy_call() +
                                            self.legs_map['Buy Put'].buy_put()


'''Runner script'''
p = PayOffCalculator()

strats = [LongPutStrategy(),
          LongCallStrategy(),
          ShortPutStrategy(),
          ShortCallStrategy(),
          LongUnderlying()]

for strat in strats:
    p.register_strategy(strat)

# p.print_registered_strategies()


# Test cases.
# Long a call
legs = [OptionLeg("Buy", "Call", 50, 10)]
payoff = p.calculate(legs)
assert payoff[0] == -10, "Long on a call, with the stock price below the \
    strike has a payoff of negative the price"
assert payoff[60] == 0, "Long on a call, with the stock price equal to \
    the (strike + price) has a payoff of zero"
assert payoff[90] == 30, "Long on a call, with the stock price above the \
    strike, has a payoff of the difference between the stock price and \
    the sum of the strike and price"


# Short a put
legs = [OptionLeg("Sell", "Put", 50, 10)]
payoff = p.calculate(legs)
assert payoff[0] == -40, "Short on a put, with the stock price below the \
    strike has a payoff of the difference between (strike + price of option) \
    and the stock price"
assert payoff[50] == 10, "Short on a put, with the stock price equal to the \
    strike, has a payoff that equals the sale price of the option"
assert payoff[90] == 10, "Short on a put, with the stock price above the \
    option strike price, has a payoff that equals the sale price of the \
    option"

# Straddle (Long a call and Long a put)
legs = [OptionLeg("Buy", "Call", 50, 10), OptionLeg("Buy", "Put", 50, 10)]
payoff = p.calculate(legs)
assert payoff[0] == 30, "Long a call and long a put, with the stock price \
    below strike price has a payoff that is the difference between the \
    strike and (the stock price + price of call + price of put)"
assert payoff[50] == -20, "Long a call and long a put, with the stock price \
    at the strike, has a payoff that is the sum of the price of both options"
assert payoff[90] == 20, "Long a call and long a put, with the stock price \
    above the strike has a payoff that is the difference between the stock \
    price and sum of the prices of the call and the put options"

# Clipped reverse strangle
legs = [OptionLeg("Sell", "Call", 60, 10), OptionLeg("Sell", "Put", 40, 10),
        OptionLeg("Buy", "Put", 20, 10), OptionLeg("Buy", "Call", 80, 10)]
payoff = p.calculate(legs)
assert payoff[0] == -20, "A Clipped reverse strangle at a stock price below \
    the lower strike, has a payoff that equals the sum of the difference \
    between the strikes and the difference between \
    the prices of the two put options"
assert payoff[45] == 0, "A Clipped reverse strangle at a stock price between \
    the higher strikes has a payoff equal to the difference between the sum \
    of the two shorted legs and the sum of the two long legs"
assert payoff[90] == -20, "A Clipped reverse strangle at a stock price above \
    the highest strike, has a payoff that equals the sum of the difference \
    between the strikes and the difference between \
    the prices of the two call options"
