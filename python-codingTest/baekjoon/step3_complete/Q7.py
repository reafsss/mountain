#Q7_A+B를 조금 더 아름답게 출력하는 문제
import sys
a=int(sys.stdin.readline())
for i in range(a):
    b,c=map(int, sys.stdin.readline().rsplit())
    print("Case #%d: %d"%(i+1,b+c))