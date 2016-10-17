import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

class GraphView:
    def drawgraph(self, payoffs):
        x_axis = [i for i in payoffs]
        y_axis = [payoffs[i] for i in payoffs]
        x_ticks = [i for i in range(0, 100, 10)]
        y_ticks = [i for i in range(-1000, 1200 ,200)]
        plt.plot(x_axis, y_axis)
        plt.xticks(x_ticks)
        plt.yticks(y_ticks)
        plt.xlabel('Underlying Price')
        plt.ylabel('Payoff')
        plt.title('Strategy Payoff')
        plt.savefig('Strategy_Payoff.jpg')

class View:
    def input_entry(self):
        while True:
            try: 
                entry = float(input("Please enter the entry price: "))
                break
            except:
                print ("Please input numbers! ")
                continue
        return entry
        
    def input_strike(self):
        while True:
            try: 
                strike = int(input("Please enter the option strike: "))
                break
            except:
                print ("Please input integers! ")
                continue
        return strike
    
    def input_amount(self):
        while True:
            try: 
                amount = int(input("Please enter the trading amount: "))
                break
            except:
                print ("Please input integers! ")
                continue
        return amount
    
    def input_type(self):
        while True:
            typ = input("Is it a Call option, Put option or the Underlying? ")
            if typ in ["Call", "Put", "Underlying"]:
                break
            else:
                print ("Please enter 'Call', 'Put' or 'Underlying': ")
                continue
        return typ    
        
    def input_side(self):
        while True:
            side = input("Do you want to Long or Short? ")
            if side in ["Long", "Short"]:
                break
            else:
                print ("Please enter either 'Long' or 'Short': ")
                continue
        return side
        
    def register_leg(self):
        response = input("Enter 'Y' to register a leg? ")
        if response in ['Y', 'y']:
            return True
            
    def print_legs(self, legs):
        for leg in legs:
            if leg.typ == "Underlying":
                print ("Strategy Leg:\n%s %d share(s) %s for $%0.2f" %(leg.side, leg.amount, leg.typ, leg.entry_price))
            else:
                print ("Strategy Leg:\n%s %d share(s) $%d %s for $%0.2f" %(leg.side, leg.amount, leg.strike, leg.typ, leg.entry_price))
        
if __name__ == "__main__":
    # graph = GraphView()
    # graph.drawgraph({0: 1, 1: 2, 2: 3})
    view = View()
    print (view.register_leg())
    print (view.input_entry())
    print (view.input_strike())
    print (view.input_side())
    print (view.input_type())