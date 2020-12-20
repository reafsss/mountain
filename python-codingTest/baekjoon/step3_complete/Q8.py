#Q8_A+B를 바로 위 문제보다 아름답게 출력하는 문제
import sys
a=int(sys.stdin.readline())
for i in range(a):
    b,c=map(int, sys.stdin.readline().rsplit())
    print("Case #%d: %d + %d = %d"%(i+1,b,c,b+c))