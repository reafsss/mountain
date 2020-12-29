#Q1_손익분기점을 구하는 프로그램을 작성하시오.
#A만원의 고정 비용, B만원의 가변 비용,노트북 가격이 C만원

A, B, C = list(map(int, input().split()))
BREAK_EVEN_POINT = 0
if(C <= B):
    BREAK_EVEN_POINT = -1
else:
    BREAK_EVEN_POINT = A // (C - B) + 1 
print(BREAK_EVEN_POINT)

# runTimeError
# a, b, c= map(int, input().split())
# n=a/(c-b)
# if n <=0:
#     print(-1)
# else :
#     print(int(n)+1)