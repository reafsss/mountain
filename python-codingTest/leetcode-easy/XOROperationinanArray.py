# Test
n = 1 #Input
start = 7 #Input
XOR=0
for i in range(0, n):
    XOR = XOR ^ (start+i*2)
print(XOR) #Output

# class Solution:
#     def xorOperation(self, n: int, start: int) -> int:
#         XOR=0
#         for i in range(0, n):
#             XOR = XOR ^ (start+i*2)
#         return XOR