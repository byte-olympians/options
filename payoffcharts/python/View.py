
class View:
    
    def __init__(self):
        pass
    
    def welcome(self):
        print("Welcome! How may I help you with your investments today?")
    
    def type_input(self):
        type = input("What type of option would you like to buy?")
        type = type.lower()
        if type == "":
            self.type_input()
        
        return type
    
    def strike_input(self):
        strike = input("At what price would you like to purchase the strike? ")
        if strike <= 0:
            print("X_X! That is not a valid strike price! Please try again!")
            self.strike_input()
        
        return strike
    
    def premium_input(self):
        premium = 5
        print("For now, at any strike price, the premium cost will be $5.")
        
        return premium
    
    def sell_buy(self):
        sellbuy = input("With the chosen option, what would you like to do? Buy or Sell?")
        sellbuy = sellbuy.lower()
        if sellbuy == "":
            self.sell_buy()
        
        return sellbuy