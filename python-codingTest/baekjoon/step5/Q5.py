#Q5
import sys
input= sys.stdin.readline
number=int(input())
scores=list(map(int, input().split()))

new_scores=[]
for i in scores:
    new_scores.append((i/max(scores))*100)

print(sum(new_scores)/number)