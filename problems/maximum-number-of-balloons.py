## https://leetcode.com/problems/maximum-number-of-balloons/

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freqStr = {c : text.count(c) for c in text}
        freqBalloon = {c: "balloon".count(c) for c in set("balloon")}
        return min(
            freqStr.get(ch, 0) // freqBalloon[ch]
            for ch in freqBalloon
        )


        
