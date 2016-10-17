from view import *
from option_leg import *
from payoffcalculator import *

class Controller:
    def __init__(self):
        self.calculator = Calculator()
        self.plotter = GraphView()
        self.view = View()
    
    def input_legs(self):
        side = self.view.input_side()
        typ = self.view.input_type()
        if typ == "Underlying":
            strike = 0
        else:
            strike = self.view.input_strike()
        entry_price = self.view.input_entry()
        amount = self.view.input_amount()
        return Leg(side, typ, strike, entry_price, amount)    
        
    def register(self):
        legs = []
        while True:
            while True:
                if self.view.register_leg(): 
                    legs.append(self.input_legs())
                    continue
                else:
                    break
            if legs is not None:
                break
            else:
                continue
        return legs
        
    def get_strategy_payoff(self):
        legs = self.register()
        self.view.print_legs(legs)
        strats = self.calculator.register_strategy(legs)
        payoff = self.calculator.calculate(strats)
        self.plotter.drawgraph(payoff)

if __name__ == "__main__":
    strategy = Controller()
    strategy.get_strategy_payoff()