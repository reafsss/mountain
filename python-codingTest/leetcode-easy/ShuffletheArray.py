# Test
nums = [2,5,1,3,4,7] #Input
n = 3 #Input
newnums=[]
for i in range(0,n):
    newnums.append(nums[i])
    newnums.append(nums[n+i])
print(newnums) #Output

# class Solution:
#     def shuffle(self, nums: List[int], n: int) -> List[int]:
#         newnums=[]
#         for i in range(0,n):
#             newnums.append(nums[i])
#             newnums.append(nums[n+i])
#         return newnums