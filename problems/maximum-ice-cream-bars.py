## https://leetcode.com/problems/maximum-ice-cream-bars

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        total = 0
        amount = 0
        costs.sort()
        for cost in costs:
            amount += cost
            if amount <= coins:
                total += 1
            else:
                break
        return total
        
