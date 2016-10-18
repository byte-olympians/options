from model.optionleg import OptionLeg
from calculators.longcallstrategy import LongCallStrategy
from calculators.longputstrategy import LongPutStrategy
from calculators.shortcallstrategy import ShortCallStrategy
from calculators.shortputstrategy import ShortPutStrategy
from calculators.longunderlying import LongUnderlying


class PayOffCalculator:
    """The class that keeps a store of registered strategies and
    orchestrates the calls to them to calculate the payoffs"""

    def __init__(self):
        self.strategy_map = {}

    def register_strategy(self, strategy):
        self.strategy_map[strategy.STRATEGY_NAME] = strategy

    def print_registered_strategies(self):
        for name in self.strategy_map.keys():
            print("Strategy " + name + " registered with value " +
                  self.strategy_map[name].STRATEGY_NAME)

    def calculate(self, legs):
        return None


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
