#s,t 입력값
s = str(input())
t = str(input())

if len(s) <= len(t):
    a = len(t) // len(s) # a는 길이로 나눈 몫
    b = len(t) % len(s) # b는 길이로 나눈 나머지
    if b == 0: 
        if s * a == t:
            print(1)
        else:           # s * a != t
            print(0)
    else:               # b != 0
            print(0)
else:
    a = len(s) // len(t)
    b = len(s) % len(t)
    if b == 0: 
        if t * a == s:
            print(1)
        else:
            print(0)
    else:
            print(0)
