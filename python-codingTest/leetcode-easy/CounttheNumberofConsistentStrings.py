# Test
import re
allowed = "ab" #Input
words = ["ad","bd","aaab","baa","badab"] #Input
combination_allowed=list(allowed)
count=0
test=[]
for j in words:
    test.append(list(set(list(j)) - set(combination_allowed)))
    #count+=1
for i in test:
    if i == []:
        count+=1
print(count)

# import re
# class Solution:
#     def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
#         combination_allowed=list(allowed)
#         count=0
#         test=[]
#         for j in words:
#             test.append(list(set(list(j)) - set(combination_allowed)))
#         for i in test:
#             if i == []:
#                 count+=1
#         return count

# Applied Concept
# 두 리스트를 비교해서 서로 없는 원소만 return받는 concept
# 집합으로 변환해서 차집합 구하기, 순서보존x
# list1=['a','d']
# list2=['a','d']
# list3 = list(set(list1) - set(list2))
# len(list3)