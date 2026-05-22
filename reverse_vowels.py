class Solution(object):
    def reverseVowels(self, s):

        vowels = "aeiouAEIOU"
        chars = list(s)

        v = []

        for ch in chars:
            if ch in vowels:
                v.append(ch)

        v = v[::-1]

        j = 0

        for i in range(len(chars)):
            if chars[i] in vowels:
                chars[i] = v[j]
                j += 1

        return "".join(chars)
