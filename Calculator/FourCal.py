class FourCal :
    def setdata(self , first , second) :
        self.first = first
        self.second = second

    def add(self) :
        result = self.first + self.second
        return result

    def sub(self) :
        result = self.first - self.second
        return result

    def mult(self) :
        result = self.first * self.second
        return result

    def div(self) :
        result = self.first / self.second
        return result