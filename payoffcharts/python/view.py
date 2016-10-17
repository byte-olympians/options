import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

class GraphView:
    def drawgraph(self, points):
        x_axis = [i for i in points]
        y_axis = [points[i] for i in points]
        # x_ticks = [i for i in range(0, 100, 10)]
        # y_ticks = [i for i in range(-100, 120 ,10)]
        plt.plot(x_axis, y_axis)
        # plt.xticks(x_ticks)
        # plt.yticks(y_ticks)
        plt.xlabel('Underlying Price')
        plt.ylabel('Strateg Payoff')
        plt.title('Strategy Payoff')
        plt.savefig('Strategy_Payoff.jpg')

class View:
    def input_entry(self):
        while True:
            try: 
                entry = float(input("Please enter the entry price of the option or underlying: "))
                break
            except:
                print ("Please input numbers! ")
                continue
        return entry
        
    def input_strike(self):
        while True:
            try: 
                strike = float(input("Please enter the option strike: "))
                break
            except:
                print ("Please input numbers! ")
                continue
        return strike
    
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
        answer = input("Enter 'Y' to register a leg? ")
        if answer in ["Y", "y"]:
            return answer

        
if __name__ == "__main__":
    # graph = GraphView()
    # graph.drawgraph({0: 1, 1: 2, 2: 3})
    view = View()
    print (view.input_entry())
    print (view.input_strike())
    print (view.input_side())
    print (view.input_type())