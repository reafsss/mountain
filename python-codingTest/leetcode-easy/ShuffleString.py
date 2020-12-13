# Test
s = "codeleet" #Input
indices = [4,5,6,7,0,2,1,3] #Input

b={}
for i in indices:
    b[i]=s[indices.index(i)]

c=sorted(b.items())
final_list=[]
for i in c:
    final_list.append(i[1])

print(''.join(final_list)) #Output

# class Solution:
#     def restoreString(self, s: str, indices: List[int]) -> str:
#         b={}
#         for i in indices:
#             b[i]=s[indices.index(i)]

#         c=sorted(b.items())
#         final_list=[]
#         for i in c:
#             final_list.append(i[1])

#         return ''.join(final_list)