# Q3
# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 
# 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 
# 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 

number=str(input())
def difference(a,b):
    return int(a-b)

count1=0
count2=99
if len(number)>=3:
    for i in range(100,int(number)+1):
        if difference((i//10)%10, i%10) == difference(i//100, (i//10)%10):
            count2+=1
else :
    count2=0
    if len(number)==1:
        count1=int(number)
    elif len(number)==2:
        count1=int(number)      

print(count1+count2)

# num = int(input())
# hansu = 0

# for n in range(1, num+1) :
#     if n <= 99 : # 1부터 99까지는 모두 한수
#         hansu += 1 
    
#     else :     
#         nums = list(map(int, str(n))) # 숫자를 자릿수대로 분리 
#         if nums[0] - nums[1] == nums[1] - nums[2] : #등차수열 확인
#             hansu+=1