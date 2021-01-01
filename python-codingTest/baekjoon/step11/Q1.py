# Q1_브루트 포스_세 장의 카드를 고르는 모든 경우를 고려하는 문제
n, maxnum = map(int, input().split())
alist=[int(x) for x in input().split()]
clist=[]
summ=0
for i,a in enumerate(alist):
    for j,b in enumerate(alist[i+1:]):
        blist=alist[i+1:]
        for k,c in enumerate(blist[j+1:]):
            summ = a + b + c
            if summ <= maxnum:
                clist.append(summ)
print(max(clist))