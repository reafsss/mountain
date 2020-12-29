#Q3_벌집이 형성되는 규칙에 따라 벌집의 위치를 구하는 문제

N = int(input())
first = 1
plus = 6
room = 1
if N == 1:
    print(1)
else:
    while True:
        first = first + plus
        room+= 1
        if N <= first:
            print(room)
            break
        plus += 6