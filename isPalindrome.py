class Solution(object):
    def isPalindrome(self, x):
        solo = str(x)
        if x < 0:
            return False
        else:
            return solo == solo[::-1] 
