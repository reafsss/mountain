class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x>=0:
            a = str(x)
            a = list(a)
            b = list(reversed(a))
            return a == b