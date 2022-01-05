#클래스 상속
from FourCal import FourCal

class MoreFourCal(FourCal) :
    pass

    def pow(self):
        result = self.first ** self.second
        return result