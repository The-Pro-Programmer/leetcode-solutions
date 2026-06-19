## https://leetcode.com/problems/find-the-highest-altitude/

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
          maxGain = 0
          totalGain = 0
          for altitude in gain:
            totalGain += altitude
            if maxGain < totalGain:
                maxGain = totalGain
          return maxGain 
