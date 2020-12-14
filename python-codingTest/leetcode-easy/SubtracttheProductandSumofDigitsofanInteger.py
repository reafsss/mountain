# Test
n=234 #Input
n_str=list(str(n))
ProductofDigits=1
SumofDigits=0
for i in n_str:
    ProductofDigits=ProductofDigits*int(i)
for i in n_str:
    SumofDigits+=int(i) 
print(ProductofDigits, SumofDigits) #Output

# class Solution:
#     def subtractProductAndSum(self, n: int) -> int:
#         n_str=list(str(n))
#         ProductofDigits=1
#         SumofDigits=0
#         for i in n_str:
#             ProductofDigits=ProductofDigits*int(i)
#         for i in n_str:
#             SumofDigits+=int(i)
#         return ProductofDigits - SumofDigits