# Test
# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]] #Input
count=0
for i in grid:
    for j in i:
        if j <0:
            count+=1
print(count) #Output

# class Solution:
#     def countNegatives(self, grid: List[List[int]]) -> int:
#         count=0
#         for i in grid:
#             for j in i:
#                 if j <0:
#                     count+=1
#         return (count)