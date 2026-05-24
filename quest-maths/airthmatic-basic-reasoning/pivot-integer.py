## https://leetcode.com/problems/find-the-pivot-integer/description/?envType=problem-list-v2&envId=maths-m1-arithmetic-basic-reasoning

class Solution:
    def pivotInteger(self, n: int) -> int:
        if n==1:
            return 1
        
        total = n*(n+1)//2
        pivot = int(math.isqrt(total))

        if pivot*pivot == total:
            return pivot
        
        return -1
        
