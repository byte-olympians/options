
class CalculatorBC:        
    def __init__(self):
        pass
 
    def calculate_payoff(self, leg_buy_call, stock_price):
        premium = leg_buy_call.premium        
        some_returns = {} 
        current_return = 0
        strike = leg_buy_call.strike 
        for i in range(101):
            current_return = i-strike-premium
            some_returns[i] = current_return
        #print(some_returns)
        #print()
        print("If you exercise the option at stock price " + str(stock_price) + " , your payoff will be : $" + str(some_returns[stock_price]))
        return(some_returns)



class  CalculatorSC:
    def __init__(self):
        pass

    def calculate_payoff(self, leg_sell_call, stock_price):
        premium = leg_sell_call.premium        
        sc_dict = {} 
        sc_return = 0
        strike = leg_sell_call.strike 
        for i in range(101):
            if i <= strike:
                sc_return = premium
                sc_dict[i] = sc_return
            elif i > strike:
                price_delta = i - strike 
                sc_return = premium - price_delta
                sc_dict[i] = sc_return
        print(sc_dict)
        print()
        print("If the buyer chose to exercise the option at stock price " + str(stock_price) + " , your payoff would be : $" + str(sc_dict[stock_price]))
        return(sc_dict)

class CalculatorBP:
    def __init__(self):
        pass

    def calculate_payoff(self, leg_buy_put, stock_price):
        premium = leg_buy_put.premium
        bp_dict = {}
        bp_return = 0
        strike = leg_buy_put.strike
        for i in range(101):
            if i <= strike:
                price_delta = strike-i
                bp_return = price_delta-premium 
                bp_dict[i] = bp_return
            elif i > strike:
                bp_dict[i] =- premium
        print(bp_dict)
        print() 
        print("At stock price " + str(stock_price) + ", your payoff would be: $" + str(bp_dict[stock_price]))
        return(bp_dict)
        


class  CalculatorSP:
    def __init__(self):
        pass

    def calculate_payoff(self, leg_sell_put, stock_price):
        premium = leg_sell_put.premium
        sp_dict = {}
        sp_return = 0
        strike = leg_sell_put.strike
        for i in range(101):
            if i >= strike:
                sp_return = premium
                sp_dict[i] = sp_return
            elif i < strike:
                price_delta = strike - i
                sp_return = premium - price_delta
                sp_dict[i] = sp_return
        print(sp_dict)
        print()
        print("At stock price " + str(stock_price) + ", your return is $ " + str(sp_dict[stock_price]))
        return(sp_dict)

        

