class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maximum = max(candies)
        result = []

        for i in candies:
            result.append(i + extraCandies >= maximum)

        return result
