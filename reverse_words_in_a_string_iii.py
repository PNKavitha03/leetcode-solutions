class Solution:
    def reverseWords(self, s):
        words = s.split()
        result = []

        # Reverse each word
        for word in words:
            result.append(word[::-1])

        # Join words with space
        return " ".join(result)
