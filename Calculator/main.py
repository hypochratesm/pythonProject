#덧셈
import sys
from MoreFourCal import MoreFourCal
#sys.path.append('..')
#print(sys.path) 

from FourCal import FourCal
#print(dir(FourCal))
#a = FourCal(
#class 알아보기
#print(type(a))
#해쉬코드 조회
#print(id(a))

# a.setdata(4,2)
# print(a.add())
# print(a.sub())
# print(a.mult())
# print(a.div())
a = MoreFourCal();
MoreFourCal.setdata(a,4,2)
print(a.add())
print(a.sub())
print(a.mult())
print(a.div())
print(a.pow())
