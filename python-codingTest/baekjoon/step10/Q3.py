# Q3_프랙탈 도형을 그리는 문제
# 프랙탈 같은 경우는 최소 단위로 쪼갤 수 있기에 분할 정복 알고리즘(Divide and Conquer)을 이용해 풀 수 있다.
# 분할 정복 알고리즘의 단계를 분할, 정복, 합치기 세 개로 나누면 쉽게 기억할 수 있다.
# ***
# * *
# ***

def star():
    print('***')
    print('* *')
    print('***')
    return 

star()

def stars(n):
    return star()