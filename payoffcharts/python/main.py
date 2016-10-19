from view import *
from option_leg import *
from payoffcalculator import *

class Controller:
    def __init__(self):
        self.calculator = Calculator()
        self.plotter = GraphView()
        self.view = View()
        
    def get_strategy_payoff(self):
        legs = self.view.register_legs()
        self.view.print_legs(legs)
        payoff = self.calculator.calculate(legs)
        self.plotter.drawgraph(payoff)

if __name__ == "__main__":
    strategy = Controller()
    strategy.get_strategy_payoff()