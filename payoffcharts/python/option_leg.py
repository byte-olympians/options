class Leg:
    def __init__(self, side, typ, strike, premium):
        self.entry_price = premium 
        self.strike = strike
        self.typ = typ
        self.side = side
        
    def get_key(self):
        return self.side + self.typ
        
    
if __name__ == "__main__":
    leg1 = Leg("Long", "Call", 50, 5)
    leg2 = Leg("Short", "Underlying", 0, 80)
    assert (leg1.get_key() == "LongCall"), "Expected value: LongCall"
    assert (leg2.get_key() == "ShortUnderlying"), "Expected value: ShortUnderlying"



