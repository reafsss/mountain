#Q4_점이 어느 사분면에 있는지 알아내는 문제
#흔한 수학 문제 중 하나는 주어진 점이 어느 사분면에 속하는지 알아내는 것이다
a,b=[int(input()) for _ in range(2)]
if a >0:
    if b>0:
        print(1)
    else:
        print(4)
else :
    if b>0:
        print(2)
    else :
        print(3)