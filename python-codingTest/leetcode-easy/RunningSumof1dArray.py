# Test
nums=[1,2,3,4,5] #Input
newlist=[]
for i in range(len(nums)):
    summm = 0
    for j in range(0,i+1):
        summm += nums[j]
    newlist.append(summm)
print(newlist) #Output

# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#             newlist=[]
#             for i in range(len(nums)):
#                 summ = 0
#                 for j in range(0,i+1):
#                     summ += nums[j]
#                 newlist.append(summ)
#             return newlist

# Other Solution
# just "return accumulate(nums)"

# Problem Analysis
# case1: len(list)=1
# newlist=[]
# newlist.append(nums[0])
# return newlist
# case2: len(list)=2
# newlist=[]
# newlist.append(nums[0])
# newlist.append(nums[0]+nums[1])
# return newlist
# case3: len(list)=3
# newlist=[]
# newlist.append(nums[0])
# newlist.append(nums[0]+nums[1])
# newlist.append(nums[0]+nums[1]+nums[2])
# return newlist
# case4: len(list)=n
# newlist=[]
# newlist.append(nums[0])
# newlist.append(nums[0]+nums[1])
# ...
# newlist.append(nums[0]+ ... +nums[n-1])
# return newlist