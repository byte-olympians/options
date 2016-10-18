from OptionLeg import *

class Calculator(OptionLeg):
    
    def __init__(self, type, strike, premium, sellbuy, newstokprice, shares):
        OptionLeg.__init__(self, strike, premium, sellbuy, type)
        self.newstokprice = newstokprice
        self.shares = 100

class LongCall(Calculator):
    
    def calculate_payoff(self, strike, premium, newstokprice, shares):
        if newstokprice <= strike:
            payoff = premium * -1 * shares
        else:
            payoff = (newstokprice - strike - premium ) * shares
            

class ShortCall(Calculator):
    
    def calculate_payoff(self, strike, premium, newstokprice, shares):
        if newstokprice < strike:
            payoff = premium * shares
            
        else:
            payoff = (premium - strike - newstokprice) * shares
        
        return payoff

class LongPut(Calculator):
    
    def calculate_payoff(self, strike, premium, newstokprice, shares):
        if newstokprice < strike:
            payoff = (strike - premium - newstokprice) * shares

        else:
            payoff = premium * -1 * shares
        
        return payoff 

class ShortPut(Calculator):
    
    def calculate_payoff(self, strike, premium, newstokprice, shares):
        if newstokprice < strike:
            payoff = (premium - strike - newstokprice) * shares

        else:
            payoff = premium * shares
        
        return payoff