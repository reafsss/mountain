# Q7
# 첫 번째 줄에 Test case의 수 T가 주어진다. 그리고 각각의 케이스마다 입력으로 첫 번째 줄에 정수 k, 두 번째 줄에 정수 n이 주어진다.
T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    people = [ i for i in range(1, n+1)]
    for __ in range(k):
        for j in range(1,n):
            people[j] += people[j-1]
    print(people[-1])