class Solution:
    def topKFrequent(self, nums, k):
        freq = {}

        # Count frequency of each number
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Sort by frequency in descending order
        sorted_nums = sorted(freq, key=freq.get, reverse=True)

        # Return first k elements
        return sorted_nums[:k]
