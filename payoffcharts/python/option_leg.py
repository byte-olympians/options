class Leg:
    def __init__(self, side, typ, strike, premium, amount):
        self.entry_price = premium 
        self.strike = strike
        self.typ = typ
        self.side = side
        self.amount = amount
        
    def get_key(self):
        return self.side + self.typ
        
    
if __name__ == "__main__":
    leg1 = Leg("Long", "Call", 50, 5, 1)
    leg2 = Leg("Short", "Underlying", 0, 80, 1)
    leg3 = Leg("Long", "Underlying", 0, 50, 1)
    leg4 = Leg("Short", "Put", 50, 5, 1)
    leg5 = Leg("Short", "Call", 50, 5, 1)
    leg6 = Leg("Long", "Put", 50, 5, 1)
    assert (leg1.get_key() == "LongCall"), "Expected value: LongCall"
    assert (leg2.get_key() == "ShortUnderlying"), "Expected value: ShortUnderlying"
    assert (leg3.get_key() == "LongUnderlying"), "Expected value: LongUnderlying"
    assert (leg4.get_key() == "ShortPut"), "Expected value: ShortPut"
    assert (leg5.get_key() == "ShortCall"), "Expected value: ShortCall"
    assert (leg6.get_key() == "LongPut"), "Expected value: LongPut"

