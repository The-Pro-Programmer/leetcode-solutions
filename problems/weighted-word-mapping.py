## https://leetcode.com/problems/weighted-word-mapping

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        alphabets='abcdefghijklmnopqrstuvwxyz'
        result = []
        for word in words:
            charSum = 0
            for ch in word:
                charIndex = ord(ch) - ord('a')
                charSum += weights[charIndex]
            mappedIndex= 25 - (charSum%26)
            result.append(alphabets[mappedIndex])


        return "".join(result)


        
