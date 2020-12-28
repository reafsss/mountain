# Test
startTime = [1,2,3] #Input
endTime = [3,2,7] #Input
queryTime = 4 #Input
count=0
for i in range(len(startTime)):
    if startTime[i] <= queryTime <= endTime[i]:
        count+=1
print(count) #Output

# class Solution:
#     def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
#         count=0
#         for i in range(len(startTime)):
#             if startTime[i] <= queryTime <= endTime[i]:
#                 count+=1
#         return count