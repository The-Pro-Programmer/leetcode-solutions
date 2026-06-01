## https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        if len(cost) <=2:
            return sum(cost)

        cost.sort(reverse=True)
        return sum(cost) - sum(cost[2::3])
        
