## https://leetcode.com/problems/maximum-building-height

class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        
        if not restrictions:
            return n-1

        restrictions.append([1, 0])
        restrictions.sort()
        if restrictions[-1][0] != n:
            restrictions.append([n, n - 1])
        
        m = len(restrictions)

        # Step 2: Left-to-Right Pass
        for i in range(1, m):
            dist = restrictions[i][0] - restrictions[i-1][0]
            restrictions[i][1] = min(restrictions[i][1], restrictions[i-1][1] + dist)
            
        # Step 3: Right-to-Left Pass
        for i in range(m - 2, -1, -1):
            dist = restrictions[i+1][0] - restrictions[i][0]
            restrictions[i][1] = min(restrictions[i][1], restrictions[i+1][1] + dist)
            
        # Step 4: Find the maximum peak between consecutive restricted buildings
        max_height = 0
        for i in range(1, m):
            p1, h1 = restrictions[i-1]
            p2, h2 = restrictions[i]
            
            # Mathematical peak calculation between two constraints
            peak = (h1 + h2 + (p2 - p1)) // 2
            max_height = max(max_height, peak)
            
        return max_height
        

        
