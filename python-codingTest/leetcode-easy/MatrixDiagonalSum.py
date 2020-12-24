# test
mat = [[1,2,3],[4,5,6],[7,8,9]]
summ=0
for i,j in enumerate(mat):
    summ+=(j[i])

for i,j in enumerate(mat):
    summ+=j[-(i+1)]

if len(mat[0])%2 == 1:
    summ = summ - mat[int(len(mat[0])/2)][int(len(mat[0])/2)]
print(summ)

# class Solution:
#     def diagonalSum(self, mat: List[List[int]]) -> int:
#         summ=0
#         for i,j in enumerate(mat):
#             summ+=(j[i])

#         for i,j in enumerate(mat):
#             summ+=j[-(i+1)]

#         if len(mat[0])%2 == 1:
#             summ = summ - mat[int(len(mat[0])/2)][int(len(mat[0])/2)]
#         return summ