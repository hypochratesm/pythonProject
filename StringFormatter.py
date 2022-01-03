# #이스케이프 문자 관리
# from builtins import len
# from datetime import date
#
# str = 'i\'m joon'
# print(str)
#
# #멀티라인 출력
# multiLine = ''' Life is too short you need python '''
# print(multiLine)
#
# #문자열 곱하기
# a= "python"
# print(a*2)
#
# #문자열 곱하기 응용
# equal = "="
# print(equal * 50)
# print("HelloWorld")
# print(equal * 50)
#
# #문자열 길이 구하기
# print(len(equal))
# print(len(a))
#
# #문자열 인덱싱
# print(multiLine[-2])
#
# #문자열 슬라이싱
# b = a[0] + a[1] +a[2]
# print(b)
# print(b[0:2])
# print(multiLine[10:])
# print(multiLine[:10])

#Formatter

# str = "I eat %d%% apples." %3
# print(str)
# str = "I eat %s apples." % "5"
# print(str)
#
# day = "it \'s good day today %s%s" %("2022" , "0104")
# print(day)

#공백처리
# str = "%10s" % "hi"
# print(str)
#
# #역순 공백처리
# str = "%-10s" % "hi"
# print(str)
# print(len(str))
#
# #포매팅 함수(문자열)
# str = "I eat {0} apples".format("five")
# print(str)
#
# #포매팅 함수(숫자)
# str = "I eat {0} apples".format(3)
# print(str)
#
# #이름으로 넣기
# str = "I eat {0} apples. per {1} days".format(3,3)
# print(str)

#왼쪽정렬
str = "{0:<10}".format("hi")
print(str)
print(len(str))

#오른쪽정렬
str = "{0:>10}".format("hi")
print(str)

#중앙정렬
str = "{0:^10}".format("hi")
print(str)

#공백채우기
str = "{0:=^10}".format("hi")
print(str)
str = "{0:=>10}".format("hi")
print(str)
str = "{0:=<10}".format("hi")
print(str)

#f 문자열 포매팅


