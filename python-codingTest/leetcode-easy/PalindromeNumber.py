class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x>=0:
            a = str(x)
            a = list(a)
            b = list(reversed(a))
            return a == b

# list(reversed(list)) -> 리스트를 거꾸로 배열시켜 반환시킨다는것을 배움