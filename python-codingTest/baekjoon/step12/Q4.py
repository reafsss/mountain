# Q4
# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이

# collections 모듈의 Counter 클래스 사용_최빈값

N = int(input())
num=[]
for i in range(N):
    num.append(int(input()))

num.sort()

from collections import Counter
def many_value(v):
    if N==1 : return v[0]
    c = Counter(v).most_common(2)
    return (c[1][0] if c[0][1] == c[1][1] else c[0][0])

statistics=[]
statistics.append(round(sum(num)/N))
statistics.append(num[int((N-1)/2)])
statistics.append(many_value(num))
statistics.append(max(num)-min(num))

for i in statistics:
    print(i)
