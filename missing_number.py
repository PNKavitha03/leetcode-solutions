class Solution:
    def missingNumber(self, nums):
        n = len(nums)

        # Sum of numbers from 0 to n
        total = n * (n + 1) // 2

        # Sum of array elements
        arr_sum = sum(nums)

        # Missing number
        return total - arr_sum
