import matplotlib.pyplot as plt 


class Plotter:
    """Uses pyplot to plot out various graphs"""
   
    def __init__(self):
        counter = 1
    
    
    def plot_single_line(self, stk_price,gain_loss):
        xaxis = []
        yaxis = []
        xaxis = stk_price
        yaxis = gain_loss
        plt.plot(xaxis,yaxis) 
        plt.ylabel("Gain/Loss")
        plt.xlabel("Stock Price Range")
        plt.show() 

