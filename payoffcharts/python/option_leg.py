from view import *

class Options:
    def __init__(self,action,typ,strike,premium):
        self.premium = premium 
        self.strike = strike
        self.typ = typ
        self.action = action
        
    def buy_call(self):
        payoff = {}
        i = 0
        while i <= 100:
            if i <= self.strike:
                payoff[i] = 0-self.premium
            else:
                payoff[i] = i - self.strike - self.premium
            i += 1
        return payoff
        
    def buy_put(self):
        payoff = {}
        i = 0
        while i <= 100:
            if i <= self.strike:
                payoff[i] = self.strike- i - self.premium
            else:
                payoff[i] = 0 - self.premium
            i += 1
        return payoff
        
    def sell_call(self):
        payoff = {}
        i = 0
        while i <= 100:
            if i <= self.strike:
                payoff[i] = self.premium
            else:
                payoff[i] = self.strike - i + self.premium
            i += 1
        return payoff
        
    def sell_put(self):
        payoff = {}
        i = 0
        while i <= 100:
            if i <= self.strike:
                payoff[i] = i - self.strike + self.premium
            else:
                payoff[i] = self.premium
            i += 1
        return payoff

buy_call = Options('buy','call',50,5)
print (buy_call.buy_call())

buy_put = Options('buy','put',50,5)
print (buy_put.buy_put())

sell_call = Options('sell','call',50,5)
print (sell_call.sell_call())

sell_put = Options('sell','put',50,5)
print (sell_put.sell_put())

