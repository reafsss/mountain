#Q11_정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력
import sys
a,b=map(int, input().split())
answer = [int(x) for x in input().split()]

for i in answer:
    if i < b:
        print(i,end=' ')