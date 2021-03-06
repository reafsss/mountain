# Test
candies = [2,3,5,1,3] #Input
extraCandies = 3 #Input
maxcandies = max(candies)
TrueorFalse=[]
for i in candies:
    TrueorFalse.append(i+extraCandies>=maxcandies)
print(TrueorFalse) #Output

# class Solution:
#     def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
#         maxcandies = max(candies)
#         TrueorFalse=[]
#         for i in candies:
#             TrueorFalse.append(i+extraCandies>=maxcandies)
#         return TrueorFalse

# Problem Analysis
# 1. find a child who have a lot of candies
# 2. compare number of candies+extraCandies with number of candies of the child who have a lot of candies
# 3. return True of False