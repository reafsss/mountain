# Test
n=7 #Input
teams = n
TotalNumberOfMatches=0
while teams > 1:
    matches = teams//2
    TotalNumberOfMatches += matches
    if teams%2 == 1:
        matches += 1
    teams = matches
print(TotalNumberOfMatches) #Output

# class Solution:
#     def numberOfMatches(self, n: int) -> int:
#         teams = n
#         TotalNumberOfMatches=0
#         while teams > 1:
#             matches = teams//2
#             TotalNumberOfMatches += matches
#             if teams%2 == 1:
#                 matches += 1
#             teams = matches
#         return TotalNumberOfMatches