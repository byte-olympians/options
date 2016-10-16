from view import *
from option_leg import *
from payoffcalculator import *

class Controller:
    def __init__(self):
        self.calculator = Calculator()
        self.plotter = GraphView()
        # strategies = [LongUnderlying(),
        #               ShortUnderlying(),
        #               LongCall(),
        #               ShortCall()]

        # for strat in strategies:
        #     self.calculator.register_strategy(strat)
        
    def get_strategy_payoff(self):
        payoff = self.calculator.calculate(Underlying("Long", 40), Underlying("Long", 50))
        self.plotter.drawgraph(payoff)
        
        
    
    # def input_legs(self):
    #     action = self.view.input_action()
    #     typ = self.view.input_type()
    #     strike = self.view.input_strike()
    #     premium = self.view.input_premium()
    #     return Options(action,typ,strike,premium)
        
    # def input_underlying(self):
    #     action = self.view.input_action()
    #     entry = self.view.input_entry()
    #     return Underlying(action,entry)
        
    # def register_legs(self):
    #     if self.view.input_underlying():
    #         underlying = self.input_underlying()
if __name__ == "__main__":
    strategy = Controller()
    strategy.get_strategy_payoff()