class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        if str(x[::-1])==str(x):
            return True
        else:
            return False
