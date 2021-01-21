# Q2
# 수 정렬하기-오름차순

N = int(input())
num=[]
for i in range(N):
    num.append(int(input()))

num.sort()

for i in num:
    print(i)