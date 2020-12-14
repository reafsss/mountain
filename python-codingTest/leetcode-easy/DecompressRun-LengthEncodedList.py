# Test
nums = [1,2,3,4] #Input
nums_freq=nums[0::2]
nums_val=nums[1::2]
nums_Answer=[]
Index=0
for i in nums_freq:
    while i>0:
        nums_Answer.append(nums_val[Index])
        i-=1
    Index+=1
print(nums_Answer) #Output

# class Solution:
#     def decompressRLElist(self, nums: List[int]) -> List[int]:
#         nums_freq=nums[0::2]
#         nums_val=nums[1::2]
#         nums_Answer=[]
#         Index=0
#         for i in nums_freq:
#             while i>0:
#                 nums_Answer.append(nums_val[Index])
#                 i-=1
#             Index+=1
            
#         return nums_Answer