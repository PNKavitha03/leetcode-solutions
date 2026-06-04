class Solution:
    def sortedSquares(self, nums):
        result = []

        # Square each element
        for num in nums:
            result.append(num * num)

        # Sort the squared numbers
        result.sort()

        return result
