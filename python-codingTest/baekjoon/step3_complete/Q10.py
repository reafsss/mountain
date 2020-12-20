#Q10_첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍고 오른쪽을 기준으로 정렬
import sys
a=int(sys.stdin.readline())
for i in range(1,a+1):
    print(str("*"*i).rjust(a))