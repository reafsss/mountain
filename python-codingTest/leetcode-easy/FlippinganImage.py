# Test
list1 = [[1,1,0],[1,0,1],[0,0,0]] #Input
list1_reverse=[]
for i in list1:
    list1_reverse.append(i[::-1])
for i in list1_reverse:
    for j,k in enumerate(i):
        if k == 0:
            i[j]=1
        else :
            i[j]=0
print(list1_reverse) #Output

# STEP: 1. reverse -> 2.invert
# class Solution:
#     def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
#         A_reverse=[]
#         for i in A:
#             A_reverse.append(i[::-1])
#         for i in A_reverse:
#             for j,k in enumerate(i):
#                 if k == 0:
#                     i[j]=1
#                 else :
#                     i[j]=0
#         return A_reverse