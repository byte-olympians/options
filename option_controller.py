from calculator import CalculatorBC 
from calculator import CalculatorSC
from calculator import CalculatorBP
from calculator import CalculatorSP
from option_plotter import Plotter

class Leg:
    def __init__(self, type, side, strike, premium):
        self.type = type
        self.side = side
        self.strike = strike
        self.premium = premium

    def get_strategy(self):
        my_strategy = self.side + "ing a " + self.type + " Option"
        return(my_strategy)


class Coordinates:
    def __init__(self):
        pass

    def get_x_axis(self): 
        stk_price = []  ## stk_price (our dictionary keys) will be our x axis
        for i in range(101):
            stk_price.append(i)
        return(stk_price)

    def get_y_axis(self,payoff):
        gain_loss = []   ## gain_loss will contain our dictionary values and will be the Y axis
        pay2=payoff
        for x in range(101):
            gain_loss.append(pay2[x])
        return(gain_loss)   


## RUNNER 
##  BUY CALL SECTION 

leg_bc = Leg("Call", "Buy", 35, 15)
strategy_bc = leg_bc.get_strategy()
print()
print(strategy_bc)
calculator_bc = CalculatorBC()
bc_payoff = calculator_bc.calculate_payoff(leg_bc, 52)
print()
print(bc_payoff)
print()

c=Coordinates()
xaxis=c.get_x_axis()
#print(xaxis)
yaxis=c.get_y_axis(bc_payoff)
#print(yaxis)

plt1 = Plotter()
plt1.plot_single_line(xaxis,yaxis)




## SELL CALL SECTION
leg_sc = Leg("Call", "Sell", 35, 12)
strategy_sc = leg_sc.get_strategy()
print()
print(strategy_sc)
calculator_sc = CalculatorSC()
sc_payoff = calculator_sc.calculate_payoff(leg_sc, 38)
print()
print(sc_payoff)
print()

d=Coordinates()
xaxis=d.get_x_axis()
#print(xaxis)
yaxis=d.get_y_axis(sc_payoff)
#print(yaxis)

plt2 = Plotter()
plt2.plot_single_line(xaxis,yaxis)




## BUY PUT SECTION
leg_bp = Leg("Put", "Buy", 25, 3)
strategy_bp = leg_bp.get_strategy()
print()
print(strategy_bp)
calculate_bp = CalculatorBP()
bp_payoff = calculate_bp.calculate_payoff(leg_bp, 15)
print()
##print(bp_payoff)
print()


e=Coordinates()
xaxis=e.get_x_axis()
#print(xaxis)
yaxis=e.get_y_axis(bp_payoff)
#print(yaxis)

plt3 = Plotter()
plt3.plot_single_line(xaxis,yaxis)



## SELL PUT SECTION
leg_sp = Leg("Put", "Sell", 25, 3)
strategy_sp = leg_sp.get_strategy()
print()
print(strategy_sp)
calculate_sp = CalculatorSP()
sp_payoff = calculate_sp.calculate_payoff(leg_sp, 15)
print()
##print(sp_payoff)
print()

f=Coordinates()
xaxis=f.get_x_axis()
#print(xaxis)
yaxis=f.get_y_axis(sp_payoff)
#print(yaxis)

plt4 = Plotter()
plt4.plot_single_line(xaxis,yaxis)




