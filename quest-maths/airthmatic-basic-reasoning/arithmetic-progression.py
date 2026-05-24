## https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/?envType=problem-list-v2&envId=maths-m1-arithmetic-basic-reasoning

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        n = len(arr)
        if n<=2:
            return True

        min_el = min(arr)
        max_el = max(arr)
        if min_el == max_el:
            return True
        
        d = max_el - min_el
        if d % (n-1) !=0 :
            return False

        d = d // (n-1)
        elements = set(arr)
        if len(elements)!=n:
            return False

        for i in range (n):
            num = min_el + i*d
            if  num not in elements:
                return False

        return True

        

        
        
