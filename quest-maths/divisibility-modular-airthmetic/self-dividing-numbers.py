## https://leetcode.com/problems/self-dividing-numbers/?envType=problem-list-v2&envId=maths-m2-divisibility-modular-arithmetic

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for n in range(left, right+1):
            
            if n<10:
                result.append(n)
                continue

            if n%10==0 or ( n%10==5 and n%2==0):
                continue

            flag = True
            temp = n
            while temp>0:
                digit = temp%10
                if digit==0 or n%digit != 0:
                    flag = False
                    break
                temp = temp//10

            if flag:
                result.append(n)
        return result
        
