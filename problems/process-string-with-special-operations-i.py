## https://leetcode.com/problems/process-string-with-special-operations-i/

class Solution:
    def processStr(self, s: str) -> str:
        result = ""
        for ch in s:
            n = len(result)
            if ch != '#' and ch != '%' and ch != '*':
                result += ch
            elif ch == '#':
                if n>0 :
                    result += result
            elif ch == '*':
                if n>0:
                    result = result[:n-1]
                else:
                    result = ""
            elif ch == '%':
                result = result[::-1]

        return result
        
