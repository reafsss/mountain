# Test
n="(()())(())(()(()))" #Input
count=0
firstindex=[0]
secondindex=[]
for i, j in enumerate(n):
    if j == "(":
        count+=1
    else :
        count-=1
    if count == 0:
        firstindex.append(i+1)
        secondindex.append(i)
firstindex=firstindex[:-1]
new=''
for i, j in zip(firstindex, secondindex):
    new+=n[i+1:j]
print(new) #Output

# class Solution:
#     def removeOuterParentheses(self, S: str) -> str:
#         count=0
#         firstindex=[0]
#         secondindex=[]
#         for i, j in enumerate(S):
#             if j == "(":
#                 count+=1
#             else :
#                 count-=1
#             if count == 0:
#                 firstindex.append(i+1)
#                 secondindex.append(i)
#         firstindex=firstindex[:-1]
#         new=''
#         for i, j in zip(firstindex, secondindex):
#             new+=S[i+1:j]
#         return new