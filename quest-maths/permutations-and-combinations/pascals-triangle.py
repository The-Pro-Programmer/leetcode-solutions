## https://leetcode.com/problems/pascals-triangle/?envType=problem-list-v2&envId=maths-m3-combinatorics-permutations

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        triangle = []

        for r in range(1, numRows+1):
            row = [1]
            current = 1

            for i in range(2, r+1):
                current = current * (r-i+1) // (i-1)
                row.append(current)

            triangle.append(row)

        return triangle
        
