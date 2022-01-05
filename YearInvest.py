#연환산수익률
# - 연환산수익률은 일정기간 발생한 수익률이 1년동안 지속되었을 경우 어떻게 변하는지 파악

#기하평균 
# case 1 100만원을 초기투자금으로 지정했지만 연속으로 두번 -25%수익률이 발생했다.
initAmt = 1000000
procAmt = 0
finalAmt = 0

ratePrice1 = 25 / 100
ratePrice2 = 25 / 100

procAmt = initAmt - (initAmt * ratePrice1)
print(procAmt)

finalAmt = procAmt - (procAmt * ratePrice1)
print(finalAmt)