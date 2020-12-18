#Q1_N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
import sys
number = int(sys.stdin.readline())
answer = [int(x) for x in sys.stdin.readline().rsplit()]
print(min(answer),max(answer))