# Test
# Input: nums = [3,4,5,2]
# Output: 12 
# Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.
nums = [3,4,5,2] #Input
num_1=max(nums)
nums.pop(nums.index(max(nums)))
num_2=max(nums)
print((num_1-1)*(num_2-1)) #Output

# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         num_1=max(nums)
#         nums.pop(nums.index(max(nums)))
#         num_2=max(nums)
#         return (num_1-1)*(num_2-1)