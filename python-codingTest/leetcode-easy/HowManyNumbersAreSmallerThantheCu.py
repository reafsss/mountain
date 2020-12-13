# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]

# Test
nums = [8,1,2,2,3] #Input
nums_small=[]
for i in nums:
    count=0
    for j in nums:
        if i > j:
            count+=1
    nums_small.append(count)
print(nums_small) #Output

# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#         nums_small=[]
#         for i in nums:
#             count=0
#             for j in nums:
#                 if i > j:
#                     count+=1
#             nums_small.append(count)
#         return nums_small