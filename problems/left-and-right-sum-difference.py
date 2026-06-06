## https://leetcode.com/problems/left-and-right-sum-differences

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n<=1:
            return [0]
        leftSum = [0]*n
        rightSum = [0]*n
        for i in range(1, n):
            leftSum[i] = leftSum[i-1] + nums[i-1]
        for i in range(n-2, -1, -1):
            rightSum[i] = rightSum[i+1] + nums[i+1]

        for i in range(0, n):
            rightSum[i] = abs(rightSum[i]-leftSum[i])
        
        return rightSum


        
