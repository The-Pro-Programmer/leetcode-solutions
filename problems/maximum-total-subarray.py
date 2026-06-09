## https://leetcode.com/problems/maximum-total-subarray-value-i

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        maxNum = max(nums)
        minNum = min(nums)
        return k*(maxNum-minNum)
        
