# Test
heights = [1,2,3,4,5] #Input
target=heights.copy()
target.sort()
count=0
for i in range(len(heights)):
    if heights[i] != target[i]:
        count+=1
print(count) #Output

# class Solution:
#     def heightChecker(self, heights: List[int]) -> int:
#         target=heights.copy()
#         target.sort()

#         count=0
#         for i in range(len(heights)):
#             if heights[i] != target[i]:
#                 count+=1

#         return count