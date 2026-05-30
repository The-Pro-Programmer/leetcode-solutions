## https://leetcode.com/problems/permutation-sequence/description/?envType=problem-list-v2&envId=maths-m3-combinatorics-permutations

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1, n+1)]
        result = []

        factorials = [1]*n
        for i in range(1, n):
            factorials[i] = factorials[i-1] * i

        k -= 1

        for i in range (n-1, -1, -1):
            blockSize = factorials[i]
            index = k//blockSize
            result.append(nums.pop(index))
            k = k%blockSize

        return "".join(result)
