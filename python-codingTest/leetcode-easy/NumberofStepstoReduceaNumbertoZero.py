# Test
num = 14 #Input
count=0
while num != 0:
    if num % 2 != 0:
        num -= 1
        count+=1
        print(count)
    else :
        num = num/2
        count+=1
        print(count)
print(count) #Output

# class Solution:
#     def numberOfSteps (self, num: int) -> int:
#         count=0
#         while num != 0:
#             if num % 2 != 0:
#                 num -= 1
#                 count+=1
#             else :
#                 num = num/2
#                 count+=1
#         return count