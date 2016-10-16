import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

class GraphView:
    def __init__(self):
        pass  
    
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
        plt.savefig('Long_Underlying.jpg')
    

if __name__ == "__main__":
    graph = GraphView()
    graph.drawgraph({0: 1, 1: 2, 2: 3})

    
# class View:
#     def input_premium(self):
#         premium = input("Please enter the option premium: ")
#         return premium
        
#     def input_strike(self):
#         strike = input("Please enter the option strike: ")
#         return strike
    
#     def input_type(self):
#         typ = input("Is it a call option or a put option? ")
#         if typ.upper() in ["CALL","PUT"]:
#             return typ.upper()
#         else:
#             print ("Please enter either call or put: ")
#             self.input_type()
    
#     def input_action(self):
#         action = input("Do you want to buy or sell? ")
#         if action.upper() in ["BUY","SELL"]:
#             return action.upper()
#         else:
#             print ("Please enter either buy or sell: ")
#             self.input_action()
    
#     def input_entry(self):
#         price = input("Please enter your entry price: ")
#         return price
        
#     def input_underlying(self):
#         underlying = input("Please enter Y if you want to take positions in the option underlying: ")
#         if underlying in ["Y","y"]:
#             return True
    
#     def input_stratname(self):
#         name = input("Please enter the name of the strategy: ")
#         return name