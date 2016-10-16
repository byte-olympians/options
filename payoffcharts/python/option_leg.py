class Option_Leg:
    def __init__(self, side, typ, strike, premium):
        self.premium = premium 
        self.strike = strike
        self.typ = typ
        self.side = side
        
    def get_key(self):
        return self.side + self.typ
        
class Underlying:
    def __init__(self, side, entry):
        self.entry = entry
        self.side = side
        
    def get_key(self):
        return self.side + "Underlying"
    
if __name__ == "__main__":
    leg1 = Option_Leg("Long", "Call", 50, 5)
    leg2 = Underlying("Short", 80)
    assert (leg1.get_key() == "LongCall"), "Expected value: LongCall"
    assert (leg2.get_key() == "ShortUnderlying"), "Expected value: ShortUnderlying"



