# Test
nums = [1,2,3,1,1,3] #Input
count=0
index=1
for i in nums:
    for j in range(index,len(nums)):
        if i == nums[j]:
            count+=1
    index+=1
print(count) #Output

# class Solution:
#     def numIdenticalPairs(self, nums: List[int]) -> int:
#         count=0
#         index=1
#         for i in nums:
#             for j in range(index,len(nums)):
#                 if i == nums[j]:
#                     count+=1
#             index+=1
#         return count