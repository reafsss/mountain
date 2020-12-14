# Test
word1 = ["ab", "c"] #Input
word2 = ["a", "bc"] #Input
word1_sum=''
word2_sum=''
for i in word1:
    word1_sum+=i
for i in word2:
    word2_sum+=i
check=False
if word1_sum == word2_sum:
    check=True
print(check) #Output

# class Solution:
#     def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
#         word1_sum=''
#         word2_sum=''
#         for i in word1:
#             word1_sum+=i
#         for i in word2:
#             word2_sum+=i
#         check=False
#         if word1_sum == word2_sum:
#             check=True
            
#         return check