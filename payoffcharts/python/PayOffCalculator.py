from OptionLeg import *
from Calculators import *
from Viwe import * 

class Payoffcalculator:
    
    def __init__(self):
        
        self.strategymap = {"LongCall" : LongCall(),
                            "ShortCall": ShortCall(),
                            "LongPut": LongPut(),
                            "ShortPut": ShortPut()
                            }
    
    def regis_strat(self):
        pass
    
    def calculate(self, legs):
        pass