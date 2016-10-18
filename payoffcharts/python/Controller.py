from view import *
from OptionLeg import *
from PayOffCalculator import *

class Controller:
    
    def __init__(self):
        self.view = View()
        self.optleg = OptionLeg()
        self.payoff = PayOffCalculator()
    
    def start(self):
        
        """
        not sure what to do after calling inputs
        """
        self.view.welcome()
        type = self.view.type_input()
        strike = self.view.strike_input()
        premium = self.view.premium_input()
        sellbuy = self.view.sell_buy()
    
    def get_strat_payoff(self):
        pass