#Q4
#1/1 -> 1/2 -> 2/1 -> 3/1 -> 2/2 -> … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.
#X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.
X=int(input())
line=1
while X>line:
    X-=line
    line+=1
if line%2==0:
    a=X
    b=line-X+1
else:
    a=line-X+1
    b=X
print(a, '/', b, sep='')

# runtimeError
# n=int(input())
# k=2
# while True:
#     summ=0
#     for i in range(1,k):
#         summ+=i
#     if n<= summ:
#         break
#     k+=1
# difference = summ - n
# if (k-1)%2 == 0:  
#     print("%d/%d"%((k-1)-difference,1+difference))
# else :
#     print("%d/%d"%(1+difference,(k-1)-difference))