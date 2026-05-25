## https://leetcode.com/problems/palindrome-number/?envType=problem-list-v2&envId=maths-m1-arithmetic-basic-reasoning

class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = str(x)
        rev = n[::-1]
        return n==rev
