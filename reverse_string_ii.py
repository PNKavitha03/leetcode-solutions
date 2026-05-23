# LeetCode - Reverse String II
# https://leetcode.com/problems/reverse-string-ii/

class Solution(object):
    def reverseStr(self, s, k):
        result = ""

        for i in range(0, len(s), 2 * k):
            result += s[i:i+k][::-1] + s[i+k:i+2*k]

        return result
