import sys
filepath = "C:/Users/qraft/Desktop/금융기관목록.txt"

with open(filepath , "r" , encoding='utf-8') as th :
    lines = th.read().splitlines()

for line in lines:
    print(line)    