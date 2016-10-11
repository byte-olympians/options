import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

class View:
    def input_premium(self):
        premium = input("Please enter the option premium: ")
        return premium
        
    def input_strike(self):
        strike = input("Please enter the option strike: ")
        return strike
    
    def input_type(self):
        typ = input("Is it a call option or a put option? ")
        if typ in ["call","put","Call","Put","CALL","PUT"]:
            return typ
        else:
            print ("Please enter either call or put: ")
            input_type()
    
    def input_action(self):
        action = input("Do you want to buy or sell? ")
        if action in ["buy","sell","Buy","Sell","BUY","SELL"]:
            return action
        else:
            print ("Please enter either buy or sell: ")
            input_action()
    
    def input_stratname(self):
        name = input("Please enter the name of the strategy: ")
        return name