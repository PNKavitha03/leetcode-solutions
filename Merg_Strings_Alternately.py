class Solution:
    def mergeAlternately(self, word1, word2):
        result = ""
        i = 0

        # Add letters alternately
        while i < len(word1) and i < len(word2):
            result += word1[i]
            result += word2[i]
            i += 1

        # Add remaining letters
        result += word1[i:]
        result += word2[i:]

        return result
