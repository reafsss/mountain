# Input: points = [[1,1],[3,4],[-1,0]]
# Output: 7

# Test
points = [[1,1],[3,4],[-1,0]] #Input
list1=[]
for i in points:
    for j in i:
        list1.append(j)
time=0
for i in range(0,len(list1)-2,2):
    time+=max(abs(list1[i] - list1[i+2]),abs(list1[i+1] - list1[i+3]))
print(time) #Output

# class Solution:
#     def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
#         list1=[]
#         for i in points:
#             for j in i:
#                 list1.append(j)
#         time=0
#         for i in range(0,len(list1)-2,2):
#             time+=max(abs(list1[i] - list1[i+2]),abs(list1[i+1] - list1[i+3]))
            
#         return time