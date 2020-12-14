# Test
nums = [0,1,2,3,4] #Input
index = [0,1,2,2,1] #Input
target=[]
count=0
for i in nums:
    target.insert(index[count],i)
    count+=1
print(target) #Output

# Applied function
# use insert(a, b) a is a target index and b is a target value

# class Solution:
#     def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
#         target=[]
#         count=0
#         for i in nums:
#             target.insert(index[count],i)
#             count+=1
#         return target