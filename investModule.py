class investCalculator:
    global rate
    rate = 0.25

    def __init__(self) -> None:
        pass

    def rOd(self, initAmt , finalAmt) :
      self.finalAmt = initAmt + (initAmt * rate)
    
    def rOy(self, initAmt , finalAmt) :
        pass