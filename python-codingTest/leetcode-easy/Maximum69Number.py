# Test
num = 9669 #Input
a=str(num)
original=list(a)
changed=[]
for i,j in enumerate(original):
    original_changing=list(a)
    if j == '9':
        original_changing[i]='6'
    else :
        original_changing[i]='9'
    changed.append(original_changing)
maxlist=[num]
for i in changed:
    maxlist.append(int(''.join(i)))
max(maxlist) #Output

# class Solution:
#     def maximum69Number (self, num: int) -> int:
#         a=str(num)
#         original=list(a)
#         changed=[]
#         for i,j in enumerate(original):
#             original_changing=list(a)
#             if j == '9':
#                 original_changing[i]='6'
#             else :
#                 original_changing[i]='9'
#             changed.append(original_changing)
#         maxlist=[num]
#         for i in changed:
#             maxlist.append(int(''.join(i)))
#         return max(maxlist)